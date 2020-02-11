import copy
import json
import re
import pandas as pd


class Tweet(object):
    def __init__(self, data):
        self.id = data['id']
        self.hashtags = []
        self.mentions = []
        self.words = []

        # fill in lists for hashtags, mentions, and words
        text = data['text'].split(' ')
        regex = '[A-z|0-9|-]'
        for t in text:
            if len(t) == 0:
                continue

            # save hashtags
            if t[0] == '#':
                self.hashtags.append(t[1:])
            # save mentions
            elif t[0] == '@':
                self.mentions.append(t[1:])
            # don't save links
            elif t[0:4] != 'http':
                word = []
                for char in t:
                    if re.match(regex, char):
                        word.append(char)

                if len(word) > 0:
                    self.words.append(''.join(word))

    def __str__(self):
        rtn = f'<{self.__class__.__name__} at {id(self)}>\n'
        rtn += f'\tid: {self.id}\n'
        rtn += f'\thashtags: {str(self.hashtags)}\n'
        rtn += f'\tmentions: {str(self.mentions)}\n'
        rtn += f'\twords: {str(self.words)}'
        return rtn


class GGData(object):
    def __init__(self, year=2020):
        file = f'gg{year}.json'

        content = pd.read_json(file)

        tweets = dict()
        for index, row in content.iterrows():
            tweet = Tweet(row)
            tweets[tweet.id] = tweet

        self.__dict__ = copy.deepcopy(tweets)
        print(len(tweets.keys()))