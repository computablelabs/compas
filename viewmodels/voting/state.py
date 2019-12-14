from models.voting import Voting
from viewmodels.viewmodel import ViewModel

class State(ViewModel):
    def __init__(self):
        self.model = Voting()

    def get_candidates(self, addr=None):
        # assure was not set to empty str...
        if not addr or addr == '':
            addr = self.model.contract.account

        return(self.model.get_candidates(None, addr))

    def hydrate(self, data):
        data['voting_address'] = self.get_address()
        data['voting_owner'] = self.get_owner()
        data['voting_candidates'] = self.get_candidates()
        return data
