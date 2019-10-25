import os
from computable.helpers.transaction import call, send
from computable.contracts import Parameterizer as P
from constants import PARAMETERIZER_CONTRACT_ADDRESS
from .model import Model
from .helpers import get_w3

class Parameterizer(Model):
    def __init__(self):
        self.w3 = get_w3()
        account = self.w3.toChecksumAddress(os.environ.get('public_key'))
        self.contract = P(account)
        self.contract.at(self.w3, PARAMETERIZER_CONTRACT_ADDRESS)

    def get_backend_payment(self):
        return call(self.contract.get_backend_payment())

    def get_maker_payment(self):
        return call(self.contract.get_maker_payment())

    def get_reserve_payment(self):
        return call(self.contract.get_reserve_payment())

    def get_cost_per_byte(self):
        return call(self.contract.get_cost_per_byte())

    def get_stake(self):
        return call(self.contract.get_stake())

    def get_price_floor(self):
        return call(self.contract.get_price_floor())

    def get_spread(self):
        return call(self.contract.get_spread())

    def get_list_reward(self):
        return call(self.contract.get_list_reward())

    def get_plurality(self):
        return call(self.contract.get_plurality())

    def get_vote_by(self):
        return call(self.contract.get_vote_by())

    def get_hash(self, param, value):
        hash = call(self.contract.get_hash(int(param), int(value)))
        # its actuall y byte array at this point, return the hexstring
        return self.w3.toHex(hash)

    def get_reparam(self, hash):
        return call(self.contract.get_reparam(hash))

    def reparameterize(self, param, value):
        args = self.contract.reparameterize(int(param), int(value))
        return self.transact(args)

    def resolve_reparam(self, hash):
        args = self.contract.resolve_reparam(hash)
        return self.transact(args)
