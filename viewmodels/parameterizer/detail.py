from models.parameterizer import Parameterizer
from viewmodels.viewmodel import ViewModel

class Detail(ViewModel):
    def __init__(self):
        self.model = Parameterizer()

    def get_backend_payment(self):
        return str(self.model.get_backend_payment())

    def get_maker_payment(self):
        return str(self.model.get_maker_payment())

    def get_reserve_payment(self):
        return str(self.model.get_reserve_payment())

    def get_cost_per_byte(self):
        return str(self.model.get_cost_per_byte())

    def get_stake(self):
        return str(self.model.get_stake())

    def get_price_floor(self):
        return str(self.model.get_price_floor())

    def get_spread(self):
        return str(self.model.get_spread())

    def get_list_reward(self):
        return str(self.model.get_list_reward())

    def get_plurality(self):
        return str(self.model.get_plurality())

    def get_vote_by(self):
        return str(self.model.get_vote_by())

    def get_hash(self, param, value):
        return self.model.get_hash(param, value)

    def get_reparam(self, hash):
        rep = self.model.get_reparam(hash)
        if len(rep) > 0:
            # format a string to make sense in the view popup
            rep_str = 'Param: {0}\nValue: {1}'
            return rep_str.format(*rep)
        else:
            return 'None'

    def reparameterize(self, param, value):
        return self.transact(self.model.reparameterize(param, value))

    def resolve_reparam(self, hash):
        return self.transact(self.model.resolve_reparam(hash))
