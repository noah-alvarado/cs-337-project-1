import copy
import json
import re

import numpy as np


class Tweet(object):
    def __init__(self, data):
        self.id = data['_id']['$oid']
        self.timestamp = data['created_at']
        self.user = data['user']
        self.user_id = data['user_id']
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
        rtn += f'\ttimestamp: {self.timestamp}\n'
        rtn += f'\tuser: {self.user}\n'
        rtn += f'\tuser_id: {self.user_id}\n'
        rtn += f'\thashtags: {str(self.hashtags)}\n'
        rtn += f'\tmentions: {str(self.mentions)}\n'
        rtn += f'\twords: {str(self.words)}'
        return rtn


class GGData(object):
    def __init__(self, file=None):
        if file is None:
            file = 'tweets/gg2020.json'

        content = open(file, encoding='utf-8').read().splitlines()

        tweets = dict()
        for line in content:
            tweet = Tweet(json.loads(line))
            tweets[tweet.id] = tweet

        # print(len(list(tweets.keys())))

        self.__dict__ = copy.deepcopy(tweets)

    def random_split(self, fraction=0.3333):
        indices = list(self.__dict__.keys())
        indices_len = len(indices)

        if fraction > 1.0:
            raise ValueError('N cannot be bigger than number of examples!')

        if fraction == 1.0:
            return list(self.__dict__.keys()), list(self.__dict__.keys())

        N = int(indices_len * fraction)
        M = int(indices_len - N)
        used_indices = []

        train_indices = []
        test_indices = []

        i = 0
        j = 0
        while i < N or j < M:
            rand_idx = np.random.randint(0, high=indices_len)
            if i < N and rand_idx not in used_indices:
                train_indices.append(indices[rand_idx])
                used_indices.append(rand_idx)
                i += 1

            rand_idx = np.random.randint(0, high=indices_len)
            if j < M and rand_idx not in used_indices:
                test_indices.append(indices[rand_idx])
                used_indices.append(rand_idx)
                j += 1

        return train_indices, test_indices
