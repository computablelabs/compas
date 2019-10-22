from models.ethertoken import EtherToken
import constants as C
"""
This class creates a simple interface for the ethertoken state widget to get
what it needs from the model.
NOTE: Owner is always the env public key on the dashboard
"""

class State:
    def __init__(self):
        self.model = EtherToken()

    def total_supply(self):
        return str(self.model.total_supply())

    def balance_of(self):
        """
        NOTE: we assume the public key is set in the environment
        """
        return str(self.model.balance_of())

    def allowance(self, spender):
        return str(self.model.allowance(None, spender))

    def hydrate(self, data):
        """
        Return an object suitable to use for a view's `data` property
        """
        data['ether_token_total_supply'] = self.total_supply()
        data['ether_token_balance'] = self.balance_of()

        # contracts that may have approved CET allowance: Reserve, Datatrust
        data['ether_token_reserve_allowance'] = self.allowance(C.RESERVE_CONTRACT_ADDRESS)
        data['ether_token_datatrust_allowance'] = self.allowance(C.DATATRUST_CONTRACT_ADDRESS)

        return data
