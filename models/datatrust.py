import os
from computable.helpers.transaction import call, send
from computable.contracts import Datatrust as DT
from constants import DATATRUST_CONTRACT_ADDRESS
from .model import Model
from .helpers import get_w3

class Datatrust(Model):
    def __init__(self):
        self.w3 = get_w3()
        account = self.w3.toChecksumAddress(os.environ.get('public_key'))
        self.contract = DT(account)
        self.contract.at(self.w3, DATATRUST_CONTRACT_ADDRESS)

    def get_reserve(self):
        return call(self.contract.get_reserve())

    def get_hash(self, url):
        # use web3 to send back hex string
        hashed = call(self.contract.get_hash(url))
        return self.w3.toHex(hashed)

    def get_backend_address(self):
        return call(self.contract.get_backend_address())

    def set_backend_url(self, url, gas_price):
        args = self.contract.set_backend_url(url, {'gas_price': self.gwei_to_wei(int(gas_price))})
        return self.transact(args)

    def get_backend_url(self):
        return call(self.contract.get_backend_url())

    # NOTE that the msg.sender can only be the the registered datatrust address
    def set_data_hash(self, listing, data, gas_price):
        args = self.contract.set_data_hash(listing, data, {'gas_price': self.gwei_to_wei(int(gas_price))})
        return self.transact(args)

    def get_data_hash(self, listing):
        return call(self.contract.get_data_hash(listing))

    def register(self, url, gas_price):
        args = self.contract.register(url, {'gas_price': self.gwei_to_wei(int(gas_price))})
        return self.transact(args)

    def resolve_registration(hash, gas_price):
        args = self.contract.resolve_registration(hash, {'gas_price': self.gwei_to_wei(int(gas_price))})
        return self.transact(args)

    def request_delivery(self, hash, amount, gas_price):
        args = self.contract.request_delivery(hash, int(amount), {'gas_price': self.gwei_to_wei(int(gas_price))})
        return self.transact(args)

    def get_bytes_purchased(self, addr):
        return call(self.contract.get_bytes_purchased(addr))

    def get_delivery(self, hash):
        """
        returns (owner, bytes_requested, bytes_delivered)
        """
        return call(self.contract.get_delivery(hash))

    # NOTE that the msg.sender can only be the the registered datatrust address
    def listing_accessed(self, listing, delivery, amount, gas_price):
        args = self.contract.listing_accessed(listing, delivery, int(amount), {'gas_price': self.gwei_to_wei(int(gas_price))})
        return self.transact(args)

    def get_access_reward_earned(self, hash):
        return call(self.contract.get_access_reward_earned(hash))

    # NOTE that the msg.sender can only be the the registered datatrust address
    def delivered(self, delivery, url, gas_price):
        args = self.contract.delivered(delivery, url, {'gas_price': self.gwei_to_wei(int(gas_price))})
        return self.transact(args)

    def set_privileged(self, listing, gas_price):
        args = self.contract.set_privileged(listing, {'gas_price': self.gwei_to_wei(int(gas_price))})
        return self.transact(args)

    def get_privileged(self):
        return call(self.contract.get_privileged())
