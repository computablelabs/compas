from models.markettoken import MarketToken
"""
This class creates a simple interface for the markettoken state widget to get
what it needs from the model
"""

class State:
    def __init__(self):
        self.model = MarketToken()

    def total_supply(self):
        return str(self.model.total_supply())

    def balance_of(self, owner=None):
        """
        NOTE: we assume the public key is set in the environment
        """
        return str(self.model.balance_of(owner))

    def allowances(self):
        """
        There are only certain contracts that are kept in the ether token's
        allowance mapping. Fetch them here and return a dictionary
        """
        pass

    def hydrate(self, data):
        """
        Return an object suitable to use for a view's `data` property
        TODO: fetch the allowances
        """
        data['market_token_total_supply'] = self.total_supply()
        data['market_token_balance'] = self.balance_of()

        return data
