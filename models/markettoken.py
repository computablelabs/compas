"""
Class meant to have the ability to fetch any and all data for the Computable MarketToken,
which is primarily:
    total_supply: N
    ( balances: Mapping )
    ( allowances: Mapping )

We can abstract some details here, as well as have a buffer in case things are not
implemented exactly as we need for our viewmodels
"""
import os
from computable.contracts import MarketToken as MT
from computable.helpers.transaction import call
from constants import MARKET_TOKEN_CONTRACT_ADDRESS
from .helpers import get_w3

class MarketToken:
    def __init__(self):
        self.w3 = get_w3()
        account = self.w3.toChecksumAddress(os.environ.get('public_key'))
        self.contract = MT(account)
        self.contract.at(self.w3, MARKET_TOKEN_CONTRACT_ADDRESS)

    def total_supply(self):
        return call(self.contract.total_supply())

    def balance_of(self, owner=None):
        """
        Our balance method is simply balance_of the stated user
        """
        if owner == None:
            owner = self.contract.account

        return call(self.contract.balance_of(owner))

    def allowance(self, owner=None, spender=None):
        """
        Given that we know the 'owner' of an allowance return the correct one
        for a given 'spender'
        """
        if owner == None:
            owner = self.contract.account
        return call(self.contract.allowance(owner, spender))
