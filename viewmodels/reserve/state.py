from models.reserve import Reserve
from viewmodels.viewmodel import ViewModel

class State(ViewModel):
    def __init__(self):
        self.model = Reserve()

    def get_support_price(self):
        return str(self.model.get_support_price())

    def get_withdrawal_proceeds(self, addr=None):
        # assure was not set to empty str...
        if addr == '':
            addr = None

        return str(self.model.get_withdrawal_proceeds(addr))

    def hydrate(self, data):
        data['reserve_address'] = self.get_address()
        data['reserve_owner'] = self.get_owner()
        data['reserve_support_price'] = self.get_support_price()
        data['reserve_withdrawal_proceeds'] = self.get_withdrawal_proceeds()
        return data
