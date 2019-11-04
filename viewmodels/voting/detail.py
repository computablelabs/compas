from models.voting import Voting
from viewmodels.viewmodel import ViewModel

class Detail(ViewModel):
    def __init__(self):
        self.model = Voting()

    def set_privileged(self, parameterizer, datatrust, listing, gas_price):
        return self.transact(self.model.set_privileged(parameterizer, datatrust,
            listing, gas_price))

    def get_privileged(self):
        priv = self.model.get_privileged()
        if len(priv) > 0:
            return '\n'.join(priv)
        else:
            return 'None'

    def has_privilege(self, addr):
        return str(self.model.has_privilege(addr))

    def candidate_is(self, hash, kind):
        return str(self.model.candidate_is(hash, kind))

    def is_candidate(self, hash):
        return str(self.model.is_candidate(hash))

    def get_candidate(self, hash):
        cand = self.model.get_candidate(hash)
        if len(cand) > 0:
            # format a string to make sense in the view popup
            cand_str = 'Kind: {0}\nOwner: {1}\nStake: {2}\nVote by: {3}\nYea votes: {4}\nNay votes: {5}'
            return cand_str.format(*cand)
        else:
            return 'None'

    def did_pass(self, hash, plurality):
        return str(self.model.did_pass(hash, plurality))

    def poll_closed(self, hash):
        return str(self.model.poll_closed(hash))

    def vote(self, hash, option, gas_price):
        return self.transact(self.model.vote(hash, option, gas_price))

    def get_stake(self, hash, addr):
        if addr == '':
            addr = None

        return str(self.model.get_stake(hash, addr))

    def unstake(self, hash, gas_price):
        return self.transact(self.model.unstake(hash, gas_price))
