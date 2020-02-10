def get_presenters(tweets, awards):
    keyphrases = [
        ['presenting'],
        ['to', 'present'],
        ['presented', 'by'],
        ['will', 'present'],
        ['will', 'be', 'presenting'],
        ['present', 'the'],
        ['presents'],
    ]

    presenter_votes = dict()
    for a in awards.keys():
        presenter_votes[a] = dict()

    for tweet in tweets.__dict__.values():
        for phrase in keyphrases:
            # iterate from 0 to the end of the list minus the amount of positions we have to look ahead
            found_items = [False] * len(phrase)
            for i in range(len(tweet.words) - len(phrase)):
                # get current sequence of words in tweet
                seq = tweet.words[i:(i + len(phrase))]

                # try to match tweet elements to phrase elements
                for p in range(len(phrase)):
                    if phrase[p].lower() == seq[p].lower():
                        found_items[p] = True
                    else:
                        found_items = [False] * len(phrase)
                        break

                if all(found_items):
                    break

            # get a presenter's name based on the phrase
            if all(found_items):
                presenters, award = extract_presenters(tweet, phrase, awards)

                presenters = '+'.join(presenters)
                if presenters not in presenter_votes[award]:
                    presenter_votes[award][presenters] = 0

                presenter_votes[award][presenters] += 1

                break

    return 'no presenters yet, but i have some tweets'


def extract_presenters(tweet, phrase, awards):
    presenters = []
    lowercase = list(map(lambda w: w.lower(), tweet.words))
    print(phrase)
    print(lowercase)
    start = lowercase.index(phrase[0])

    # split into halves to search for correlation
    if phrase == ['presented', 'by']:
        presenter_part = tweet.words[(start + len(phrase)):]
        award_part = tweet.words[:start]
    else:
        presenter_part = tweet.words[:start]
        award_part = tweet.words[(start + len(phrase)):]

    # find associated award
    possible_awards = []
    for award_name, properties in list(awards.items()):
        inclusions = properties[0]
        exclusions = properties[1]
        plus = properties[2]

        is_included = [False] * len(inclusions)
        is_excluded = False
        has_plus = len(plus) == 0

        for w in award_part:
            # no exclusions
            for e in exclusions:
                if e == w.lower():
                    is_excluded = True
                    break

            if is_excluded:
                break

            # all inclusions
            for i in range(inclusions):
                if inclusions[i] == w.lower():
                    is_included[i] = True

            # at least one plus
            if not has_plus:
                for p in plus:
                    if p == w.lower():
                        has_plus = True
                        break

        # if there is an exclusion, no plus, or not every inclusion, skip this award
        if is_excluded or not has_plus or not all(is_included):
            continue

        possible_awards.append(award_name)

    # get most specific award possible
    award = max(possible_awards, key=len)
    print(award)
    # find presenter




    return presenters, award
