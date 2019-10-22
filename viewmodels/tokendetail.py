from .viewmodel import ViewModel
"""
Abstraction of the common methods for token viewmodels
"""
class TokenDetail(ViewModel):
    def total_supply(self):
        return str(self.model.total_supply())

    def get_symbol(self):
        return self.model.get_symbol()

    def get_decimals(self):
        return str(self.model.get_decimals())

    def allowance(self, owner, spender):
        # the user may have set the owner to an empty string by interaction
        if owner == '':
            owner = None

        return str(self.model.allowance(owner, spender))

    def balance_of(self, owner):
        if owner == '':
            owner = None

        return str(self.model.balance_of(owner))

    def approve(self, spender, amount):
        return self.transact(self.model.approve(spender, amount))

    def increase_allowance(self, spender, amount):
        return self.transact(self.model.increase_allowance(spender, amount))

    def decrease_allowance(self, spender, amount):
        return self.transact(self.model.decrease_allowance(spender, amount))

    def transfer(self, to, amount):
        return self.transact(self.model.transfer(to, amount))

    def transfer_from(self, source, to, amount):
        return self.transact(self.model.transfer_from(source, to, amount))
