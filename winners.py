import re

from reactions import gg_reactions
from reference import WINNER_NOISE


def get_winners(tweets, awards):
    phrases = [
        ['wins'],
        ['won'],
        ['Wins'],
        ['Won'],
        ['won by'],
        ['wins', 'Golden', 'Globe', 'for'],
        ['won', 'Golden', 'Globe', 'for'],
        ['wins', 'a', 'Golden', 'Globe', 'for'],
        ['won', 'a', 'Golden', 'Globe', 'for'],
        ['won', 'the', 'Golden', 'Globe', 'for'],
        ['wins', 'the', 'Golden', 'Globe', 'for']
    ]

    winner_votes = dict()
    winner_votes['ignore'] = dict()
    for category in awards.keys():
        winner_votes[category] = dict()

    for tweetObj in tweets.__dict__.values():
        lowercase = ' '.join([lw for lw in map(lambda x: x.lower(), tweetObj.words)])
        for phrase in map(lambda x: ' '.join(x), phrases):
            if phrase in lowercase:
                for winners, award in extract_winners(tweetObj, phrase, awards):
                    winners.sort()
                    w = '+'.join(winners)
                    if w not in winner_votes[award]:
                        winner_votes[award][w] = 0

                    winner_votes[award][w] += 1
                break

    winners = dict()
    for a in awards.keys():
        if a not in winner_votes:
            winners[a] = ['%unknown%']
            continue
        best_match = ('%unknown%', -1)
        for w in winner_votes[a].keys():
            if winner_votes[a][w] > best_match[1] and w != 'ignore':
                best_match = (w, winner_votes[a][w])
        winners[a] = ' '.join(best_match[0].split('+'))

    # for a, w in winners.items():
    #     print('award: ', a, 'winner: ', w)

    return winners


def extract_winners(tweet, phrase, awards):
    # winners = []
    lowercase = list(map(lambda y: y.lower(), tweet.words))
    # print(phrase)
    # print(lowercase)
    # start = lowercase.index(phrase[0])

    try:
        start = ' '.join(lowercase).index(phrase)
    except ValueError:
        return [['ignore'], 'ignore']

    if phrase == ['won', 'by']:
        winner_part = ' '.join(tweet.words)[(start + len(phrase)):]
        award_part = ' '.join(lowercase)[:start]
    else:
        winner_part = ' '.join(tweet.words)[:start]
        award_part = ' '.join(lowercase)[(start + len(phrase)):]

    possible_awards = []
    for award_name, properties in list(awards.items()):
        inclusions = properties[0]
        exclusions = properties[1]
        plus = properties[2]

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

    title_awards = ['best motion picture - drama', 'best motion picture - comedy or musical', 'best animated feature film', 'best foreign language film', 'best screenplay - motion picture', 'best original score - motion picture', 'best original song - motion picture', 'best television series - drama', 'best television series - comedy or musical', 'best mini-series or motion picture made for television']

    for award in possible_awards:
        name_match = re.compile("[A-Z][A-z-]* [A-Z][A-z-]*")
        title_match = re.compile("[[A-Z][A-z-]*[ ]*]*")

        if award in title_awards:
            # match for movie
            all_winner = re.findall(title_match, winner_part)
            all_winner = [p for p in map(lambda z: z.lower(), all_winner)]
        else:
            # match for person
            all_winner = re.findall(name_match, winner_part)
            all_winner = [p for p in map(lambda z: z.lower(), all_winner)]

        winners = []
        for w in all_winner:
            noisy = False
            for nw in WINNER_NOISE:
                if nw in w:
                    noisy = True
                    break

            if not noisy:
                if w not in winners:
                    winners.append(w.strip())

        if len(winners) > 0:
            gg_reactions.extract_reaction('winners', award, ' '.join(tweet.words))
            yield winners, award

    # always return something, even if no possible awards
    yield ['ignore'], 'ignore'

# problems:
# best animated feature film winner:  ['link', 'missing'] real: missing link
# best original score - motion picture winner:  ['gunadttir', 'hildur'] real: hildur gudnad'ottir
# best original song - motion picture winner:  ['eltonofficial'] real: 'i'm gonna love me again' by elton john
# best screenplay - motion picture winner:  ['quentin', 'tarantino'] just the +
# best performance by an actress in a motion picture - comedy or musical winner:  ['congratulations awkwafina'] real: awkwafina
# best motion picture - comedy or musical winner:  ['hollywood', 'once', 'time', 'upon'] real: once upon a time in hollywood
# best motion picture - drama winner:  ['latest', 'the'] real: 1917
