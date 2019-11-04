from models.ethertoken import EtherToken
from viewmodels.tokendetail import TokenDetail

class Detail(TokenDetail):
    def __init__(self):
        self.model = EtherToken()

    def deposit(self, amount, gas_price):
        return self.transact(self.model.deposit(amount, gas_price))

    def withdraw(self, amount, gas_price):
        return self.transact(self.model.withdraw(amount, gas_price))
