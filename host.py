import nltk


def get_hosts(tweets):
    tweet = "welcome host thingy Bob"
    nltk.download('punkt')
    words = nltk.word_tokenize(tweet)
    host_index = words.index("host")
    return words[host_index + 1] + " " + words[host_index + 2]
