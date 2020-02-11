import re
import math

from reference import PRESENTER_NOISE


def get_presenters(tweets, awards):
    keyphrases = [
        ['presenting'],
        ['to', 'present'],
        ['presented', 'by'],
        ['presented'],
        ['will', 'present'],
        ['will', 'be', 'presenting'],
        ['present', 'the'],
        ['presents'],
        ['present']
    ]

    presenter_votes = dict()
    presenter_votes['ignore'] = dict()
    for a in awards.keys():
        presenter_votes[a] = dict()

    for tweet in tweets.__dict__.values():
        lowercase = ' '.join([lw for lw in map(lambda x: x.lower(), tweet.words)])
        for phrase in map(lambda x: ' '.join(x), keyphrases):
            if phrase in lowercase:
                for presenters, award in extract_presenters(tweet, phrase, awards):
                    presenters.sort()
                    p = '+'.join(presenters)
                    if p not in presenter_votes[award]:
                        presenter_votes[award][p] = 0

                    presenter_votes[award][p] += 1

                break

    # key : <award-name>
    # value: <presenter>[]
    presenters = dict()
    for a in awards.keys():
        if a not in presenter_votes:
            presenters[a] = '%hosts%'
            continue

        best_match = ('%hosts%', -1)
        for p in presenter_votes[a].keys():
            if presenter_votes[a][p] > best_match[1] and p != 'ignore':
                best_match = (p, presenter_votes[a][p])
        presenters[a] = best_match[0].split('+')

    print('\n\n--------------------------------------------\n\n')
    for a, p in presenters.items():
        print(f'{a}: {p}\n')

    return presenters


def extract_presenters(tweet, phrase, awards):
    lowercase = list(map(lambda y: y.lower(), tweet.words))

    try:
        start = ' '.join(lowercase).index(phrase)
    except ValueError:
        return [['ignore'], 'ignore']

    # split into halves to search for correlation
    # keep presenter_part capitalized to match names
    # lowercase awards to so we can match any common string
    if phrase == ['presented', 'by']:
        presenter_part = ' '.join(tweet.words)[(start + len(phrase)):]
        award_part = ' '.join(lowercase)[:start]
    else:
        presenter_part = ' '.join(tweet.words)[:start]
        award_part = ' '.join(lowercase)[(start + len(phrase)):]

    # find associated award
    possible_awards = []
    for award_name, properties in list(awards.items()):
        inclusions = properties[0]
        exclusions = properties[1]
        plus = properties[2]

        # find probable awards
        is_excluded = False

        # no exclusions
        for exl in exclusions:
            if exl in award_part:
                is_excluded = True
                break

        if is_excluded:
            continue

        # all inclusions
        for inc in inclusions:
            if inc not in award_part:
                is_excluded = True
                break

        if is_excluded:
            continue

        # at least one plus
        if len(plus) > 0:
            is_excluded = True
            for p in plus:
                if p in award_part:
                    is_excluded = False
                    break

        if is_excluded:
            continue

        possible_awards.append(award_name)

    # yield vote for presenter and award
    for award in possible_awards:
        # find presenter
        name_match = re.compile("[A-Z][A-z-]* [A-Z][A-z-]*")
        all_presenters = re.findall(name_match, presenter_part)
        all_presenters = [p for p in map(lambda z: z.lower(), all_presenters)]

        presenters = []
        for p in all_presenters:
            noisy = False
            for nw in PRESENTER_NOISE:
                if nw in p:
                    noisy = True
                    break
            if not noisy:
                if p not in presenters:
                    presenters.append(p)

        if len(presenters) > 0:
            yield presenters, award
        else:
            print(award)
            print(award_part)
            print(presenter_part, '\n')

    # always return something, even if no possible awards
    yield ['ignore'], 'ignore'
