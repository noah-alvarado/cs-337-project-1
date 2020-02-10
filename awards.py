import re
import nltk
import operator

def get_awards(tweets):
    possible_award = 'Best'
    helpers = ['in', 'a', '-', '--', 'by', 'or', 'an', 'In', 'A', 'By', 'Or', 'An', ',']
    stop_words = ['For', 'From']
    wrong_words = ['Dressed', 'Advice', 'Moments', 'Looks', 'Reactions', 'Worst', 'Golden', 'Host', 'Party', 'Part']
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
                elif (tweetObj.words[i] in stop_words):
                    break;
                elif (tweetObj.words[i] in wrong_words):
                    possible_award = 'Best'
                    break;
                elif (tweetObj.words[i] in helpers) or (re.match(award_re, tweetObj.words[i])):
                    if (tweetObj.words[i] != '-') or (tweetObj.words[i] != ','): # so we don't have duplicates, but need to remove if dashes are needed for formatting
                        possible_award = possible_award + ' ' + tweetObj.words[i]
                elif (tweetObj.words[i - 1] in helpers):
                    possible_award = 'Best'
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
