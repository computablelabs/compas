from models.reserve import Reserve

class State:
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
        data['reserve_support_price'] = self.get_support_price()
        data['reserve_withdrawal_proceeds'] = self.get_withdrawal_proceeds()
        return data
