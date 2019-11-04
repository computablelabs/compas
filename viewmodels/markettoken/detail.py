from models.markettoken import MarketToken
from viewmodels.tokendetail import TokenDetail

class Detail(TokenDetail):
    def __init__(self):
        self.model = MarketToken()

    def set_privileged(self, reserve, listing, gas_price):
        return self.transact(self.model.set_privileged(reserve, listing, gas_price))

    def get_privileged(self):
        priv = self.model.get_privileged()
        if len(priv) > 0:
            return '\n'.join(priv)
        else:
            return 'None'

    def has_privilege(self, addr):
        return str(self.model.has_privilege(addr))
