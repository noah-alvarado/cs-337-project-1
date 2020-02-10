import re
import nltk
import urllib.request
from reference import AWARDS_LISTS

def get_nominees(tweets):
    nltk.download('averaged_perceptron_tagger')
    nltk.download('maxent_ne_chunker')
    nltk.download('words')
    nltk.download('names')

    male_names = [name for name in nltk.corpus.names.words('male.txt')]
    female_names = [name for name in nltk.corpus.names.words('female.txt')]
    year = 2020
    year = year - 1
    # link for web scraping for movies:
    movies_wiki = 'https://en.wikipedia.org/w/api.php?action=parse&format=json&page=' + str(year) + '%20in%20film&prop=wikitext&formatversion=2'
    request_url = urllib.request.urlopen(movies_wiki)
    scrape_result = str(request_url.read())
    list_of_movies = []
    while scrape_result.find('(film)') > -1:
        loc = scrape_result.find('(film)')
        end = scrape_result.find(']]', loc)
        movie = scrape_result[loc + 7:end]
        scrape_result = scrape_result[end:]
        if movie not in list_of_movies:
            list_of_movies.append(movie)

    list_of_movies = map(lambda x: x.lower(), list_of_movies)
    all_nominees = dict()
    for category, details in AWARDS_LISTS.items():
        all_nominees[category] = dict()
    tweets = tweets.__dict__
    for key, tweetObj in tweets.items():
        for category, details in AWARDS_LISTS.items():
            include = True
            tweet = ' '.join(tweetObj.words).lower()
            for word in details[0]:
                if word not in tweet:
                    include = False
            if include:
                for word in details[1]:
                    if word in tweet:
                        include = False
            if include:
                print (category)
                print (tweet)
                possible_nominees = []
                # tweet_sentences = nltk.sent_tokenize(tweet)
                # tweet_sentences = [nltk.word_tokenize(t_sent) for t_sent in tweet_sentences]
                # tweet_sentences = [nltk.pos_tag(t_sent) for t_sent in tweet_sentences]
                # for tagged_sentence in tweet_sentences:
                #     for chunk in nltk.ne_chunk(tagged_sentence):
                #         if type(chunk) == nltk.tree.Tree:
                #             if chunk.label() == 'PERSON':
                #                 possible_nominees.append(' '.join([c[0] for c in chunk]))
                if 'actor' in category or 'actress' in category or 'director' in category:
                #     possible_names = list(nltk.bigrams(tweetObj.words))
                #     for possible_name in possible_names:
                #         f_name = possible_name[0]
                #         l_name = possible_name[1]
                #         if f_name in male_names and (l_name in male_names or l_name in female_names):
                #             possible_nominees.append(possible_name[0] + ' ' + possible_name[1])
                # elif 'actress' in category:
                #     possible_names = list(nltk.bigrams(tweetObj.words))
                #     for possible_name in possible_names:
                #         f_name = possible_name[0]
                #         l_name = possible_name[1]
                #         if f_name in female_names and (l_name in male_names or l_name in female_names):
                #             possible_nominees.append(possible_name[0] + ' ' + possible_name[1])
                # elif 'director' in category:
                    possible_names = list(nltk.bigrams(tweetObj.words))
                    for possible_name in possible_names:
                        f_name = possible_name[0]
                        l_name = possible_name[1]
                        if (f_name in male_names or f_name in female_names) and (l_name in male_names or l_name in female_names):
                            possible_nominees.append(possible_name[0] + ' ' + possible_name[1])
                else:
                    for movie in list_of_movies:
                        if movie in tweet:
                            possible_nominees.append(movie)

                for possible_nominee in possible_nominees:
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
    return all_nominees