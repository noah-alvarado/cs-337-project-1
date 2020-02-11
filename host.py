
from nltk.metrics import edit_distance
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

    top_hosts = (sorted(all_hosts.items(), key=lambda x: x[1], reverse=True))[:2]
    most_likely_host = [top_hosts[0][0]]

    dist = edit_distance(most_likely_host[0].lower(), top_hosts[1][0].lower())
    relative_mention_amount = top_hosts[1][1] / top_hosts[0][1]

    if dist >= 5 and relative_mention_amount > 0.60:
        most_likely_host.append(top_hosts[1][0])

    return most_likely_host

