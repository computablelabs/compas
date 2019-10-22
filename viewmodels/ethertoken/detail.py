from models.ethertoken import EtherToken
from viewmodels.tokendetail import TokenDetail

class Detail(TokenDetail):
    def __init__(self):
        self.model = EtherToken()

    def deposit(self, amount):
        return self.transact(self.model.deposit(amount))

    def withdraw(self, amount):
        return self.transact(self.model.withdraw(amount))
