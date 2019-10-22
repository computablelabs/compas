from models.reserve import Reserve
from viewmodels.viewmodel import ViewModel

class Detail(ViewModel):
    def __init__(self):
        self.model = Reserve()

    def get_support_price(self):
        return str(self.model.get_support_price())

    def get_withdrawal_proceeds(self, addr=None):
        # assure was not set to empty str...
        if addr == '':
            addr = None

        return str(self.model.get_withdrawal_proceeds(addr))

    def support(self, offer):
        return self.transact(self.model.support(offer))

    def withdraw(self):
        return self.transact(self.model.withdraw())
