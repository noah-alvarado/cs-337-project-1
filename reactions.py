


class Borg:
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state


class Reactions(Borg):
    def __init__(self):
        Borg.__init__(self)
        self.reactions = {
            'hosts': {},
            'nominees': {},
            'winners': {},
            'presenters': {}
        }

    def __str__(self): return str(self.reactions)

    def extract_reaction(self, kind, item, text):
