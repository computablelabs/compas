from models.ethertoken import EtherToken

class Detail:
    def __init__(self):
        self.model = EtherToken()

    def allowance(self, owner, spender):
        return str(self.model.allowance(owner, spender))

    def balance_of(self, owner):
        return str(self.model.balance_of(owner))

    def approve(self, spender, amount):
        tx_hash = self.model.approve(spender, amount)
        if tx_hash == None:
            tx_hash = ''

        return tx_hash
