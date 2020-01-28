
import nltk
import re

def get_hosts(tweets):
    host_re = re.compile('host [A-Z][a-z]* [A-Z][a-z]*')
    all_hosts = dict()
    tweets = tweets.__dict__
    for key, tweetObj in tweets.items():
        # nltk.download('punkt')
        # words = nltk.word_tokenize(tweet)
        # host_index = words.index("host")
        # return words[host_index + 1] + " " + words[host_index + 2]
        tweet = ' '.join(tweetObj.words)
        possible_host_match = host_re.search(tweet)
        possible_host = ''
        if possible_host_match:
            possible_host = tweet[possible_host_match.start() + 5 : possible_host_match.end()]
            if possible_host in all_hosts:
                all_hosts[possible_host] = all_hosts[possible_host] + 1
            else:
                all_hosts[possible_host] = 1
    max_appearance = 0
    most_likely_host = ''
    for host, appearances in all_hosts.items():
        if appearances > max_appearance:
            max_appearance = appearances
            most_likely_host = host
    return most_likely_host

