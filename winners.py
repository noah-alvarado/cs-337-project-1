
import re
import nltk
import urllib.request



def get_winners(tweets):
    #  nltk.download('punkt')
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

    male_names = [name for name in nltk.names.words('male.txt')]
    female_names = [name for name in nltk.names.words('female.txt')]
    year = 2020
    movies_wiki = 'https://en.wikipedia.org/w/api.php?action=parse&format=json&page=' + year + '%20in%20film&prop=wikitext&formatversion=2'

    all_winners = dict()
    for category in categories:
        all_winners[category] = dict()
    #  winners_re = re.compile('WINNER! [A-Z[a-z]* [A-Z][a-z]*' | 'Congratulations to [A-Z[a-z]* [A-Z][a-z]*' | '[A-Z[a-z]* [A-Z][a-z]* wins')
    tweets = tweets.__dict__
    for key, tweetObj in tweets.items():
        for category in categories:
            category_re = re.compile(category)
            tweet = ' '.join(tweetObj.words)
            possible_winner_match = category_re.search(tweet)
            possible_winners = []
            if possible_winner_match:
                tweet_sentences = nltk.sent_tokenize(tweet)
                tweet_sentences = [nltk.word_tokenize(t_sent) for t_sent in tweet_sentences]
                tweet_sentences = [nltk.pos_tag(t_sent) for t_sent in tweet_sentences]
                for tagged_sentence in tweet_sentences:
                    for chunk in nltk.ne_chunk(tagged_sentence):
                        if type(chunk) == nltk.tree.Tree:
                            if chunk.label() == 'PERSON':
                                possible_winners.append(' '.join([c[0] for c in chunk]))
                for possible_winner in possible_winners:
                    print(tweet)
                    print(possible_winner)
                    if possible_winner in all_winners[category]:
                        all_winners[category][possible_winner] = all_winners[category][possible_winner] + 1
                    else:
                        all_winners[category][possible_winner] = 1

        max_appearance = 0
        most_likely_winner = ''
        for winner, appearances in all_winners[category].items():
            if appearances > max_appearance:
                max_appearance = appearances
                most_likely_winner = winner

    print(all_winners['best director - motion picture'])


    return most_likely_winner
