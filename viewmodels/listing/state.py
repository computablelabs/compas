from models.listing import Listing
from viewmodels.viewmodel import ViewModel

class State(ViewModel):
    def __init__(self):
        self.model = Listing()

    def get_listings(self, addr=None):
        # assure was not set to empty str...
        if addr == '':
            addr = None

        return(self.model.get_listings(addr))

    def hydrate(self, data):
        data['listing_address'] = self.get_address()
        data['listing_owner'] = self.get_owner()
        data['listings'] = self.get_listings()
        return data
