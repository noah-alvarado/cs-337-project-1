import re
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

    all_winners = dict()
    all_winners['ignore'] = dict()
    for category in awards.keys():
        all_winners[category] = dict()

    for tweetObj in tweets.__dict__.values():
        lowercase = ' '.join([lw for lw in map(lambda x: x.lower(), tweetObj.words)])
        for phrase in map(lambda x: ' '.join(x), phrases):
            if phrase in lowercase:
                for winners, award in extract_winners(tweetObj, phrase, awards):
                    winners = '+'.join(winners)
                    if winners not in all_winners[award]:
                        all_winners[award][winners] = 0
                    if award != 'ignore':
                        print('award: ', award, 'winner: ', winners)
                    all_winners[award][winners] += 1
                break

    return "we're trying here"

def extract_winners(tweet, phrase, awards):
    # winners = []
    lowercase = list(map(lambda w: w.lower(), tweet.words))
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
        title_match = re.compile("[A-Z][A-z-]*")
        all_winner = re.findall(name_match, winner_part)
        all_winner = [p for p in map(lambda x: x.lower(), all_winner)]
        winners = []
        for w in all_winner:
            for nw in WINNER_NOISE:
                if nw not in w.lower():
                    winners.append(w)
        if len(winners) > 0:
            yield winners, award
        else:
            print('\n', award)
            print(winner_part, '\n')
        # always return something, even if no possible awards
    yield ['ignore'], 'ignore'


    # award = max(possible_awards, key=len)
    # print(award)
    #
    # return winners, award
        #
        # for possible_winner in possible_winners:
        #     print(tweet)
        #     print(possible_winner)
        #     if possible_winner in all_winners[category]:
        #         all_winners[category][possible_winner] = all_winners[category][possible_winner] + 1
        #     else:
        #         all_winners[category][possible_winner] = 1

        # max_appearance = 0
        # most_likely_winner = ''
        # for winner, appearances in all_winners[category].items():
        #     if appearances > max_appearance:
        #         max_appearance = appearances
        #         most_likely_winner = winner
