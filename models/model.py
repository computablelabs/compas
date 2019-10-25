import os
from .helpers import set_gas_prices
from computable.helpers.transaction import send
"""
All of our models implement the transact method

Notes:
    Models are the raw data source used by Viewmodels that transform that data for consumption by views.

    There is only ever a single model for a contract.

    Models know about contracts.

    Models are ignorant of viewmodels and views
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
