import os
from .helpers import set_gas_prices
from computable.helpers.transaction import send
"""
All of our models implement the transact method
"""
class Model:
    def transact(self, args):
        """
        once the computable HOC args tuple is assembled this method is the same everywhere
        """
        private_key = os.environ.get('private_key')
        if private_key:
            set_gas_prices(self.w3, args)
            tx = send(self.w3, private_key, args)
            return self.w3.toHex(tx)
