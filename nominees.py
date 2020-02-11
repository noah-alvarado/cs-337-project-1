import re
from reference import AWARDS_LISTS
import warnings

warnings.filterwarnings('ignore')

def get_nominees_helper(tweets):
    all_nominees = dict()
    for category in AWARDS_LISTS.keys():
        all_nominees[category] = dict()
    tweets = tweets.__dict__
    for key, tweetObj in tweets.items():
        for category, details in AWARDS_LISTS.items():
            include = True
            tweet = ' '.join(tweetObj.words).lower()

            if len(details[2]) > 0:
                include = False
                for word in details[2]:
                    if word in tweet:
                        include = True
                        break

            for word in details[0]:
                if word not in tweet:
                    include = False
                    break

            for word in details[1]:
                if word in tweet:
                    include = False
                    break

            if include:
                possible_nominees = []
                if 'actor' in category or 'actress' in category or 'director' in category:
                    name_casing = re.compile('[A-Z][a-z]* [A-Z][a-z]*')
                    possible_names = name_casing.findall(' '.join(tweetObj.words))
                    for possible_name in possible_names:
                        include_name = True
                        stop_words = ['Golden', 'Globe', "Globes", 'Best', 'Actor', 'Supporting', "Movie", "Motion", 'Picture', 'Drama', 'Television', 'Musical', "T",
                                      "V", "Limited", "TV", "Actress", "The", "Animated", "Comedy", "In", "Act", "Award", "A", "An", "By", "Series", "Film", "Congrats",
                                      "Congratulations", "Feature"]
                        for word in stop_words:
                            if word in possible_name.split():
                                include_name = False
                        if include_name:
                            possible_nominees.append(possible_name.lower())
                else:
                    movie_matcher = re.compile('[[A-Z][A-z]*[ ]*]*')
                    possible_movies = re.findall(movie_matcher, ' '.join(tweetObj.words))
                    stop_words = ['Golden', 'Globe', "Globes", 'Best', 'Actor', 'Supporting', "Movie", "Motion",
                                  'Picture', 'Drama', 'Television', 'Musical', "T",
                                  "V", "Limited", "TV", "Actress", "The", "Animated", "Comedy", "In", "Act", "Award",
                                  "A"]

                    for m in possible_movies:
                        bad = False
                        for sw in stop_words:
                            if sw.lower() in m.lower():
                                bad = True
                                break
                        if not bad:
                            possible_nominees.append(m.strip().lower())

                for possible_nominee in possible_nominees:
                    if possible_nominee in all_nominees[category]:
                        all_nominees[category][possible_nominee] = all_nominees[category][possible_nominee] + 1
                    else:
                        all_nominees[category][possible_nominee] = 1

    for award, nominees in all_nominees.items():
        all_nominees[award] = sorted(nominees.items(), key=lambda x: x[1], reverse=True)[:5]
        nominees_list = []
        for each_nom in all_nominees[award]:
            nominees_list.append(each_nom[0])
        all_nominees[award] = nominees_list
    return all_nominees