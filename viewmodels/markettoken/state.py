from models.markettoken import MarketToken
from viewmodels.viewmodel import ViewModel
import constants as C
"""
This class creates a simple interface for the markettoken state widget to get
what it needs from the model
"""

class State(ViewModel):
    def __init__(self):
        self.model = MarketToken()

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
        TODO: fetch the allowances
        """
        data['market_token_address'] = self.get_address()
        data['market_token_owner'] = self.get_owner()
        data['market_token_total_supply'] = self.total_supply()
        data['market_token_balance'] = self.balance_of()

        # contracts that may have CMT allowance: Voting, Listing
        data['market_token_voting_allowance'] = self.allowance(C.VOTING_CONTRACT_ADDRESS)
        data['market_token_listing_allowance'] = self.allowance(C.LISTING_CONTRACT_ADDRESS)

        return data
