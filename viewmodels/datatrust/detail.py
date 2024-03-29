from models.datatrust import Datatrust
from viewmodels.viewmodel import ViewModel

class Detail(ViewModel):
    def __init__(self):
        self.model = Datatrust()

    def set_privileged(self, listing, gas_price):
        return self.transact(self.model.set_privileged(listing, gas_price))

    def get_privileged(self):
        return self.model.get_privileged()

    def get_reserve(self):
        return self.model.get_reserve()

    def get_hash(self, url):
        return self.model.get_hash(url)

    def get_backend_address(self):
        return self.model.get_backend_address()

    def get_backend_url(self):
        url = str(self.model.get_backend_url())
        if url == '':
            return 'None'
        else:
            return url

    def set_backend_url(self, url, gas_price):
        return self.transact(self.model.set_backend_url(url, gas_price))

    def get_data_hash(self, listing):
        return self.model.get_data_hash(listing)

    def set_data_hash(self, listing, data, gas_price):
        return self.transact(self.model.set_data_hash(listing, data, gas_price))

    def register(self, url, gas_price):
        return self.transact(self.model.register(url, gas_price))

    def resolve_registration(self, hash, gas_price):
        return self.transact(self.model.resolve_registration(hash, gas_price))

    def request_delivery(self, hash, amount, gas_price):
        return self.transact(self.model.request_delivery(hash, amount, gas_price))

    def get_bytes_purchased(self, addr):
        return str(self.model.get_bytes_purchased(addr))

    def get_delivery(self, hash):
        d = self.model.get_delivery(hash)
        if len(d) > 0:
            # format a string to make sense in the view popup
            d_str = 'Owner: {0}\nBytes requested: {1}\nBytes delivered: {2}'
            return d_str.format(*d)
        else:
            return 'None'

    def listing_accessed(self, listing, delivery, amount, gas_price):
        return self.transact(self.model.listing_accessed(listing, delivery, amount, gas_price))

    def get_access_reward_earned(self, hash):
        return str(self.model.get_access_reward_earned(hash))

    def delivered(self, delivery, url, gas_price):
        return self.transact(self.model.delivered(delivery, url, gas_price))
