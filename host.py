# import nltk
import re

def get_hosts(tweets):
    host_re = re.compile('host [A-z]* [A-z]*')
    tweet = "welcome host Thingy Bob"
    # nltk.download('punkt')
    # words = nltk.word_tokenize(tweet)
    # host_index = words.index("host")
    # return words[host_index + 1] + " " + words[host_index + 2]
    possible_host_match = host_re.match(tweet)
    possible_host = tweet[possible_host_match.start() + 5, possible_host_match.end()]
    return possible_host