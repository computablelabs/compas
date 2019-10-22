import os
from computable.helpers.transaction import call, send
from computable.contracts import Reserve as Res
from constants import RESERVE_CONTRACT_ADDRESS
from .model import Model
from .helpers import get_w3

class Reserve(Model):
    def __init__(self):
        self.w3 = get_w3()
        account = self.w3.toChecksumAddress(os.environ.get('public_key'))
        self.contract = Res(account)
        self.contract.at(self.w3, RESERVE_CONTRACT_ADDRESS)

    def get_support_price(self):
        return call(self.contract.get_support_price())

    def get_withdrawal_proceeds(self, addr=None):
        # we can default to the env key if omitted
        if addr == None:
            addr = self.contract.account

        return call(self.contract.get_withdrawal_proceeds(addr))

    def support(self, offer):
        args = self.contract.support(int(offer))
        return self.transact(args)

    def withdraw(self):
        args = self.contract.withdraw()
        return self.transact(args)
