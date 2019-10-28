from models.datatrust import Datatrust
from viewmodels.viewmodel import ViewModel

class State(ViewModel):
    def __init__(self):
        self.model = Datatrust()

    def get_backend_address(self):
        return(self.model.get_backend_address())

    def get_backend_url(self):
        return(self.model.get_backend_url())

    def hydrate(self, data):
        data['datatrust_address'] = self.get_address()
        data['datatrust_owner'] = self.get_owner()
        data['datatrust_backend_address'] = self.get_backend_address()
        data['datatrust_backend_url'] = self.get_backend_url()
        return data
