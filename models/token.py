"""
abstraction of the common methods for both tokens
"""
import os
from computable.helpers.transaction import call, send
from .helpers import get_w3, set_gas_prices

class Token:
    def get_symbol(self):
        return call(self.contract.get_symbol())

    def get_decimals(self):
        return call(self.contract.get_decimals())

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
        if owner == None:
            owner = self.contract.account

        return call(self.contract.allowance(owner, spender))

    def approve(self, spender, amount):
        args = self.contract.approve(spender, int(amount))
        return self.transact(args)

    def increase_allowance(self, spender, amount):
        args = self.contract.increase_allowance(spender, int(amount))
        return self.transact(args)

    def decrease_allowance(self, spender, amount):
        args = self.contract.decrease_allowance(spender, int(amount))
        return self.transact(args)

    def transfer(self, to, amount):
        args = self.contract.transfer(to, int(amount))
        return self.transact(args)

    def transfer_from(self, source, to, amount):
        args = self.contract.transfer_from(source, to, int(amount))
        return self.transact(args)

    def transact(self, args):
        """
        once the computable HOC args tuple is assembled this method is the same everywhere
        """
        private_key = os.environ.get('private_key')
        if private_key:
            set_gas_prices(self.w3, args)
            tx = send(self.w3, private_key, args)
            return self.w3.toHex(tx)
