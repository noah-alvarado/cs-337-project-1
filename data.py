import json
import re


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

        content = open(file).read().splitlines()

        self.tweets = dict()
        for line in content:
            try:
                tweet = Tweet(json.loads(line))
                self.tweets[tweet.id] = tweet
            except IndexError:
                print(line)
                return
