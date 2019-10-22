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
from .token import Token
from .helpers import get_w3

class MarketToken(Token):
    def __init__(self):
        self.w3 = get_w3()
        account = self.w3.toChecksumAddress(os.environ.get('public_key'))
        self.contract = MT(account)
        self.contract.at(self.w3, MARKET_TOKEN_CONTRACT_ADDRESS)

    def set_privileged(self, reserve, listing):
        args = self.contract.set_privileged(reserve, listing)
        return self.transact(args)

    def get_privileged(self):
        return call(self.contract.get_privileged())

    def has_privilege(self, addr):
        return call(self.contract.has_privilege(addr))
