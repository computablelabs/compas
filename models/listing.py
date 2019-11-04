import os
from computable.helpers.transaction import call, send
from computable.contracts import Listing as L
from constants import LISTING_CONTRACT_ADDRESS
from .model import Model
from .helpers import get_w3

class Listing(Model):
    def __init__(self):
        self.w3 = get_w3()
        account = self.w3.toChecksumAddress(os.environ.get('public_key'))
        self.contract = L(account)
        self.contract.at(self.w3, LISTING_CONTRACT_ADDRESS)

    def is_listed(self, hash):
        return call(self.contract.is_listed(hash))

    def get_listing(self, hash):
        return call(self.contract.get_listing(hash))

    def list(self, hash, gas_price):
        args = self.contract.list(hash, {'gas_price': self.gwei_to_wei(int(gas_price))})
        return self.transact(args)

    def withdraw_from_listing(self, hash, amount, gas_price):
        args = self.contract.withdraw_from_listing(hash, int(amount), {'gas_price': self.gwei_to_wei(int(gas_price))})
        return self.transact(args)

    def resolve_application(self, hash, amount, gas_price):
        args = self.contract.resolve_application(hash, {'gas_price': self.gwei_to_wei(int(gas_price))})
        return self.transact(args)

    def claim_access_reward(self, hash, gas_price):
        args = self.contract.claim_access_reward(hash, {'gas_price': self.gwei_to_wei(int(gas_price))})
        return self.transact(args)

    def challenge(self, hash, gas_price):
        args = self.contract.challenge(hash, {'gas_price': self.gwei_to_wei(int(gas_price))})
        return self.transact(args)

    def resolve_challenge(self, hash, gas_price):
        args = self.contract.resolve_challenge(hash, {'gas_price': self.gwei_to_wei(int(gas_price))})
        return self.transact(args)

    def exit(self, hash, gas_price):
        args = self.contract.exit(hash, {'gas_price': self.gwei_to_wei(int(gas_price))})
        return self.transact(args)

    # this is not an actual contract method, but the application of a helper to grep logs...
    def get_listings(self, addr=None):
        if addr == None:
            addr = self.contract.account

        # a placeholder return until get_candidates_by_address is implemented in V2
        return ['0x5PaM', '0x3gg5', '0xV1k1ng5']
