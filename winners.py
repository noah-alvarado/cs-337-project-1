
def get_winners(tweets, awards):
    phrases = [['wins'],
               ['won'],
               ['Wins'],
               ['Won'],
               ['won by'],
               ['wins', 'Golden', 'Globe', 'for'],
               ['won', 'Golden', 'Globe', 'for'],
               ['wins', 'a', 'Golden', 'Globe', 'for'],
               ['won', 'a', 'Golden', 'Globe', 'for'],
               ['won', 'the', 'Golden', 'Globe', 'for']
               ['wins', 'the', 'Golden', 'Globe', 'for']]

    all_winners = dict()
    for category in awards.keys():
        all_winners[category] = dict()

    for tweetObj in tweets.__dict__.items():
        for phrase in phrases:
            found_items = [False] * len(phrase)
            for i in range(len(tweetObj.words) - len(phrase)):
                seq = tweetObj.words[i:(i + len(phrase))]
                for p in range(len(phrase)):
                    if phrase[p].lower() == seq[p].lower():
                        found_items[p] = True
                    else:
                        found_items = [False] * len(phrase)
                        break
                if all(found_items):
                    break

            if all(found_items):
                winners, award = extract_winners(tweetObj, phrase, awards)

                winners = '+'.join(winners)
                if winners not in all_winners[award]:
                    all_winners[award][winners] = 0

                all_winners[award][winners] += 1
                break

    return "we're trying here"

def extract_winners(tweet, phrase, awards):
    winners = []
    lowercase = list(map(lambda w: w.lower(), tweet.words))
    print(phrase)
    print(lowercase)
    start = lowercase.index(phrase[0])

    # split into halves to search for correlation
    if phrase == ['won', 'by']:
        winner_part = tweet.words[(start + len(phrase)):]
        award_part = tweet.words[:start]
    else:
        winner_part = tweet.words[:start]
        award_part = tweet.words[(start + len(phrase)):]

    possible_awards = []
    for award_name, properties in list(awards.items()):
        inclusions = properties[0]
        exclusions = properties[1]
        plus = properties[2]

        is_included = [False] * len(inclusions)
        is_excluded = False
        has_plus = len(plus) == 0

        for w in award_part:
            for e in exclusions:
                if e == w.lower():
                    is_excluded = True
                    break
            if is_excluded:
                break

            for i in range(inclusions):
                if inclusions[i] == w.lower():
                    is_included[i] = True

            if not has_plus:
                for p in plus:
                    if p == w.lower():
                        has_plus = True
                        break

        if is_excluded or not has_plus or not all(is_included):
            continue

        possible_awards.append(award_name)


    award = max(possible_awards, key=len)
    print(award)

    return winners, award
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
