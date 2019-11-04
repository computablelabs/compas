"""
Class meant to have the ability to fetch any and all data for the Computable EtherToken,
which is primarily:
    total_supply: N
    ( balances: Mapping )
    ( allowances: Mapping )

We can abstract some details here, as well as have a buffer in case things are not
implemented exactly as we need for our viewmodels
"""
import os
from computable.contracts import EtherToken as ET
from constants import ETHER_TOKEN_CONTRACT_ADDRESS
from .token import Token
from .helpers import get_w3

class EtherToken(Token):
    def __init__(self):
        self.w3 = get_w3()
        account = self.w3.toChecksumAddress(os.environ.get('public_key'))
        self.contract = ET(account)
        self.contract.at(self.w3, ETHER_TOKEN_CONTRACT_ADDRESS)

    def deposit(self, amount, gas_price):
        args = self.contract.deposit(int(amount), {'gas_price': self.gwei_to_wei(int(gas_price))})
        return self.transact(args)

    def withdraw(self, amount, gas_price):
        args = self.contract.withdraw(int(amount), {'gas_price': self.gwei_to_wei(int(gas_price))})
        return self.transact(args)
