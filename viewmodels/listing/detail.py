from models.listing import Listing
from viewmodels.viewmodel import ViewModel

class Detail(ViewModel):
    def __init__(self):
        self.model = Listing()

    def is_listed(self, hash):
        return str(self.model.is_listed(hash))

    def get_listing(self, hash):
        l = self.model.get_listing(hash)
        if len(l) > 0:
            # format a string to make sense in the view popup
            l_str = 'Owner: {0}\nSupply: {1}'
            return l_str.format(*l)
        else:
            return 'None'

    def list(self, hash):
        return self.transact(self.model.list(hash))

    def withdraw_from_listing(self, hash, amount):
        return self.transact(self.model.withdraw_from_listing(hash, amount))

    def resolve_application(self, hash):
        return self.transact(self.model.resolve_application(hash))

    def claim_access_reward(self, hash):
        return self.transact(self.model.claim_access_reward(hash))

    def challenge(self, hash):
        return self.transact(self.model.challenge(hash))

    def resolve_challenge(self, hash):
        return self.transact(self.model.resolve_challenge(hash))

    def exit(self, hash):
        return self.transact(self.model.exit(hash))
