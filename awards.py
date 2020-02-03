import re
import nltk

def get_awards(tweets):
    starts_with = 'best'
    end_in = ['picture',
              'musical',
              'television',
              'drama',
              'animated']
    host_re = re.compile('best [A-z]* picture')
    award_re_arr = []
    for ending in end_in:
        award_re_arr.append(re.compile('best [A-z, ,-]* ' + ending))
    all_awards = dict()
    tweets = tweets.__dict__
    for key, tweetObj in tweets.items():
        # nltk.download('punkt')
        # words = nltk.word_tokenize(tweet)
        # host_index = words.index("host")
        # return words[host_index + 1] + " " + words[host_index + 2]
        if 'won' in  tweetObj.words:
            possible_start = tweetObj.words.index('won') + 1
            possible_award = ' '.join(tweetObj.words[possible_start:])
            tweet = ' '.join(tweetObj.words)
            for award_re in award_re_arr:
                possible_award = award_re.search(tweet)
                if possible_award:
                        possible_award = possible_award.string[possible_award.start():possible_award.end()]
                        possible_award = possible_award.lower()
                        possible_award.split(' and ')
                        for individual_possible_award in possible_award:
                            if possible_award in all_awards:
                                all_awards[possible_award] = all_awards[possible_award] + 1
                            else:
                                all_awards[possible_award] = 1
                                tweet = ' '.join(tweetObj.words)


    return all_awards
