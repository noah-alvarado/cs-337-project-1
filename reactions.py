import random

from reference import REACTIONS


class Borg:
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state


class Reactions(Borg):
    def __init__(self):
        Borg.__init__(self)
        self.reactions = {
            'hosts': {},
            'winners': {}
        }

    def __str__(self): return str(self.reactions)

    def reset(self):
        self.reactions = {
            'hosts': {},
            'winners': {}
        }

    def get_reaction(self, kind, item):
        best_match = ('nothing', 0)
        for reacs in self.reactions[kind][item].items():
            for r in reacs:
                if r[1] > best_match[1]:
                    best_match = r

        if best_match[0] == 'nothing':
            return random.choice(list(self.reactions[kind][item].keys()))

        return best_match[0]

    def extract_reaction(self, kind, item, text):
        if item not in self.reactions[kind]:
            self.reactions[kind][item] = dict([(key, 0) for key in REACTIONS])

        for r in REACTIONS:
            if r in text.lower():
                self.reactions[kind][item][text] += 1
