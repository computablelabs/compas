import os
from computable.helpers.transaction import call, send
from computable.contracts import Voting as V
from constants import VOTING_CONTRACT_ADDRESS
from .model import Model
from .helpers import get_w3

class Voting(Model):
    def __init__(self):
        self.w3 = get_w3()
        account = self.w3.toChecksumAddress(os.environ.get('public_key'))
        self.contract = V(account)
        self.contract.at(self.w3, VOTING_CONTRACT_ADDRESS)

    def set_privileged(self, parameterizer, datatrust, listing, gas_price):
        args = self.contract.set_privileged(parameterizer, datatrust,
            listing, {'gas_price': self.gwei_to_wei(int(gas_price))})
        return self.transact(args)

    def get_privileged(self):
        return call(self.contract.get_privileged())

    def has_privilege(self, addr):
        return call(self.contract.has_privilege(addr))

    def candidate_is(self, hash, kind):
        return call(self.contract.candidate_is(hash, int(kind)))

    def is_candidate(self, hash):
        return call(self.contract.is_candidate(hash))

    def get_candidate(self, hash):
        return call(self.contract.get_candidate(hash))

    def did_pass(self, hash, plurality):
        return call(self.contract.did_pass(hash, plurality))

    def poll_closed(self, hash):
        return call(self.contract.poll_closed(hash))

    def vote(self, hash, option, gas_price):
        args = self.contract.vote(hash, int(option), {'gas_price': self.gwei_to_wei(int(gas_price))})
        return self.transact(args)

    def get_stake(self, hash, addr=None):
        # we'll default to the env user if omitted
        if addr == None:
            addr = self.contract.account

        return call(self.contract.get_stake(hash, addr))

    def unstake(self, hash, gas_price):
        args = self.contract.unstake(hash, {'gas_price': self.gwei_to_wei(int(gas_price))})
        return self.transact(args)

    # this is not an actual contract method, but the application of a helper to grep logs...
    def get_candidates(self, addr=None):
        if addr == None:
            addr = self.contract.account

        # a placeholder return until get_candidates_by_address is implemented in V2
        return ['0xFoO', '0xbAR', '0xBaZ']
