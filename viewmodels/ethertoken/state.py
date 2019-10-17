from models.ethertoken import EtherToken
"""
This class creates a simple interface for the ethertoken state widget to get
what it needs from the model
"""

class State:
    def __init__(self):
        self.model = EtherToken()

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
        data['ether_token_total_supply'] = self.total_supply()
        data['ether_token_balance'] = self.balance_of()

        return data
