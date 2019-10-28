from models.parameterizer import Parameterizer
from viewmodels.viewmodel import ViewModel

class State(ViewModel):
    def __init__(self):
        self.model = Parameterizer()

    def get_backend_payment(self):
        payment = self.model.get_backend_payment()
        return f'{payment}%'

    def get_maker_payment(self):
        payment = self.model.get_maker_payment()
        return f'{payment}%'

    def get_reserve_payment(self):
        payment = self.model.get_reserve_payment()
        return f'{payment}%'

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

    def hydrate(self, data):
        data['p11r_address'] = self.get_address()
        data['p11r_owner'] = self.get_owner()
        data['p11r_backend_payment'] = self.get_backend_payment()
        data['p11r_maker_payment'] = self.get_maker_payment()
        data['p11r_reserve_payment'] = self.get_reserve_payment()
        data['p11r_cost_per_byte'] = self.get_cost_per_byte()
        data['p11r_stake'] = self.get_stake()
        data['p11r_price_floor'] = self.get_price_floor()
        data['p11r_spread'] = self.get_spread()
        data['p11r_list_reward'] = self.get_list_reward()
        data['p11r_plurality'] = self.get_plurality()
        data['p11r_vote_by'] = self.get_vote_by()

        return data
