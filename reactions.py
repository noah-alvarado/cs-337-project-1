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
        for r, v in self.reactions[kind][item].items():
            if v > best_match[1]:
                best_match = (r, v)

        if best_match[0] == 'nothing':
            return random.choice(list(self.reactions[kind][item].keys()))

        return best_match[0]

    def extract_reaction(self, kind, item, text):
        if item not in self.reactions[kind]:
            self.reactions[kind][item] = {key: 0 for key in REACTIONS}

        for r in REACTIONS:
            if r in text.lower():
                self.reactions[kind][item][r] += 1


gg_reactions = Reactions()
