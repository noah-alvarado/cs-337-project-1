import re
import nltk
import operator

def get_awards(tweets):
    possible_award = 'Best'
    helpers = ['in', 'a', '-', '--', 'by', 'or', 'an', 'In', 'A', 'By', 'Or', 'An']
    award_re = '[A-Z][a-z]*'

    print(len(list(tweets.__dict__.keys())))

    all_awards = dict()

    for idx, tweetObj in enumerate(list(tweets.__dict__.values())):
        # print(idx)
        if 'Best' in tweetObj.words:

            for i in range(len(tweetObj.words)):
                if tweetObj.words[i] == 'Best':
                    tweetObj.words = tweetObj.words[i:]
                    break;
            for i in range(len(tweetObj.words)):
                # print(tweetObj.words[i])
                if i == 0:
                    continue;
                elif (tweetObj.words[i] in helpers) or (re.match(award_re, tweetObj.words[i])):
                    possible_award = possible_award + ' ' + tweetObj.words[i]
                else:
                    break;

            if possible_award == 'Best':
                continue;

            if possible_award in all_awards:
                all_awards[possible_award] = all_awards[possible_award] + 1
            else:
                all_awards[possible_award] = 1

            print(possible_award)
            possible_award = 'Best'

    top_awards = (sorted(all_awards.items(), key=lambda x: x[1], reverse=True))[:26]
    # top_awards = []
    # for i in range(26):
    #     maxi = max(all_awards.items(), key=operator.itemgetter(1))
    #     top_awards.append(maxi)
    #     all_awards[maxi[0]] = -1

    return top_awards
