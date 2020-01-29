def get_presenters(tweets):
    keyphrases = [
        ['will', 'be', 'presenting'],
        ['will', 'present'],
        ['presents'],
        ['present'],
        ['to', 'present'],
        ['presented', 'by'],
        ['presenting'],
        ['presenting', 'with'],
        ['presents', 'with'],
        ['presenters'],
        ['golden', 'globes', 'presenter']
    ]

    presenters = []

    for tweet in tweets:
        for phrase in keyphrases:
            # iterate from 0 to the end of the list minus the amount of positions we have to look ahead
            for i in range(len(tweet.words) - (len(phrase) - 1)):
                # get current sequence of words in tweet
                seq = tweet.words[i:len(phrase)]

                # try to match tweet elements to phrase elements
                match = True
                for p, s in zip(phrase, seq):
                    if p.lower() != s.lower():
                        match = False
                        break

                # if no match, onto the next sequence
                if not match:
                    continue

                # get a presenter's name
                print(tweet)

    return 'no presenters yet, but i have some tweets'
