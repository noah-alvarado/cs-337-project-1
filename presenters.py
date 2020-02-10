import re

from reference import PRESENTER_NOISE


def get_presenters(tweets, awards):
    keyphrases = [
        ['presenting'],
        ['to', 'present'],
        ['presented', 'by'],
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

                    presenters = '+'.join(presenters)
                    if presenters not in presenter_votes[award]:
                        presenter_votes[award][presenters] = 0

                    if award != 'ignore':
                        print('\n', award, presenters, '\n')
                    presenter_votes[award][presenters] += 1

                break

    return 'no presenters yet, but i have some tweets'


def extract_presenters(tweet, phrase, awards):
    lowercase = list(map(lambda x: x.lower(), tweet.words))

    try:
        start = ' '.join(lowercase).index(phrase)
    except ValueError:
        # print(f'\ncouldn\'t find: {phrase}')
        # print(lowercase, '\n')
        return [['ignore'], 'ignore']

    # split into halves to search for correlation
    # keep presenter_part with capitalization to match names
    # lowercase awards to just match strings
    if phrase == ['presented', 'by']:
        presenter_part = ' '.join(tweet.words)[(start + len(phrase)):]
        award_part = ' '.join(lowercase)[:start]
    else:
        presenter_part = ' '.join(tweet.words)[:start]
        award_part = ' '.join(lowercase)[(start + len(phrase)):]

    # print(award_part)

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
        all_presenters = [p for p in map(lambda x: x.lower(), all_presenters)]

        presenters = []
        for p in all_presenters:
            for nw in PRESENTER_NOISE:
                if nw not in p:
                    presenters.append(p)

        if len(presenters) > 0:
            yield presenters, award
        else:
            print('\n', award)
            print(presenter_part, '\n')

    # always return something, even if no possible awards
    yield ['ignore'], 'ignore'
