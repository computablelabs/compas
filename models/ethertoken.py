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
from computable.helpers.transaction import call, send
from constants import ETHER_TOKEN_CONTRACT_ADDRESS
from .helpers import get_w3, set_gas_prices

class EtherToken:
    def __init__(self):
        self.w3 = get_w3()
        account = self.w3.toChecksumAddress(os.environ.get('public_key'))
        self.contract = ET(account)
        self.contract.at(self.w3, ETHER_TOKEN_CONTRACT_ADDRESS)

    def total_supply(self):
        return call(self.contract.total_supply())

    def balance_of(self, owner=None):
        """
        balance method is simply balance_of the stated owner, or default to env user
        """
        if owner == None:
            owner = self.contract.account

        return call(self.contract.balance_of(owner))

    def allowance(self, owner=None, spender=None):
        """
        Given that we know the 'owner' of an allowance return the correct one
        for a given 'spender'
        """
        if owner == None or owner == '':
            owner = self.contract.account

        return call(self.contract.allowance(owner, spender))

    def approve(self, spender, amount):
        private_key = os.environ.get('private_key')
        if private_key:
            args = self.contract.approve(spender, int(amount))
            set_gas_prices(self.w3, args)
            tx = send(self.w3, private_key, args)
            return self.w3.toHex(tx)
