def get_presenters(tweets):
    keyphrases = [
        ['presents'],
        ['presenting'],
        ['to', 'present'],
        ['presented', 'by'],
        ['will', 'present'],
        ['will', 'be', 'presenting']
    ]

    presenters = []

    for tweet in tweets.__dict__.values():
        for phrase in keyphrases:
            # iterate from 0 to the end of the list minus the amount of positions we have to look ahead
            for i in range(len(tweet.words) - (len(phrase) - 1)):
                # get current sequence of words in tweet
                seq = tweet.words[i:(i + len(phrase))]

                # try to match tweet elements to phrase elements
                match = True
                for p, s in zip(phrase, seq):
                    if p.lower() != s.lower():
                        match = False
                        break

                # if no match, onto the next sequence
                if not match:
                    continue

                # get a presenter's name based on the phrase
                presenters.append(extract_presenters(tweet, phrase))
                break

    return 'no presenters yet, but i have some tweets'


def extract_presenters(tweet, phrase):
    presenters = []
    lowercase = list(map(lambda w: w.lower(), tweet.words))
    start = lowercase.index(phrase[0])

    # split into halves to search for correlation
    if phrase == ['presented', 'by']:
        presenter_part = tweet.words[(start + len(phrase)):]
        award_part = tweet.words[:start]
    else:
        presenter_part = tweet.words[:start]
        award_part = tweet.words[(start + len(phrase)):]

    print(phrase)
    print(presenter_part)
    print(award_part)
    print('\n\n')

    return presenters, tweet
