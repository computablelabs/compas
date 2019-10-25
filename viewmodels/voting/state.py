from models.voting import Voting

class State:
    def __init__(self):
        self.model = Voting()

    def get_candidates(self, addr=None):
        # assure was not set to empty str...
        if addr == '':
            addr = None

        return(self.model.get_candidates(addr))

    def hydrate(self, data):
        data['voting_candidates'] = self.get_candidates()
        return data
