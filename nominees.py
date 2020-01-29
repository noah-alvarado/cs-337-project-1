import nltk
import re

def get_nominees(tweets):
    nltk.download('averaged_perceptron_tagger')
    nltk.download('maxent_ne_chunker')
    nltk.download('words')
    categories = ['best screenplay - motion picture',
                  'best director - motion picture',
                  'best performance by an actress in a television series - comedy or musical',
                  'best foreign language film',
                  'best performance by an actor in a supporting role in a motion picture',
                  'best performance by an actress in a supporting role in a series, mini-series or motion picture made for television',
                  'best motion picture - comedy or musical',
                  'best performance by an actress in a motion picture - comedy or musical',
                  'best mini-series or motion picture made for television',
                  'best original score - motion picture',
                  'best performance by an actress in a television series - drama"',
                  'best performance by an actress in a motion picture - drama',
                  'best motion picture - drama',
                  'best performance by an actor in a supporting role in a series, mini-series or motion picture made for television',
                  'best performance by an actress in a supporting role in a motion picture',
                  'best television series - drama',
                  'best performance by an actor in a mini-series or motion picture made for television',
                  'best performance by an actress in a mini-series or motion picture made for television',
                  'best animated feature film',
                  'best original song - motion picture',
                  'best performance by an actor in a motion picture - drama',
                  'best television series - comedy or musical',
                  'best performance by an actor in a television series - drama',
                  'best performance by an actor in a television series - comedy or musical']
    all_nominees = dict()
    for category in categories:
        all_nominees[category] = dict()
    tweets = tweets.__dict__
    for key, tweetObj in tweets.items():
        for category in categories:
            host_re = re.compile(category)
            tweet = ' '.join(tweetObj.words)
            possible_host_match = host_re.search(tweet)
            possible_nominees = []
            if possible_host_match:
                tweet_sentences = nltk.sent_tokenize(tweet)
                tweet_sentences = [nltk.word_tokenize(t_sent) for t_sent in tweet_sentences]
                tweet_sentences = [nltk.pos_tag(t_sent) for t_sent in tweet_sentences]
                for tagged_sentence in tweet_sentences:
                    for chunk in nltk.ne_chunk(tagged_sentence):
                        if type(chunk) == nltk.tree.Tree:
                            if chunk.label() == 'PERSON':
                                possible_nominees.append(' '.join([c[0] for c in chunk]))
                for possible_nominee in possible_nominees:
                    print(tweet)
                    print(possible_nominee)
                    if possible_nominee in all_nominees[category]:
                        all_nominees[category][possible_nominee] = all_nominees[category][possible_nominee] + 1
                    else:
                        all_nominees[category][possible_nominee] = 1
        max_appearance = 0
        most_likely_host = ''
        # for host, appearances in all_nominees.items():
            # if appearances > max_appearance:
                # max_appearance = appearances
                # most_likely_host = host
    print(all_nominees['best director - motion picture'])
    return 'julio jorge'