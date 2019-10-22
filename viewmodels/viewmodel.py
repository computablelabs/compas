"""
Base class for all ViewModels
"""
class ViewModel:
    def transact(self, tx_hash):
        if tx_hash == None:
            tx_hash = ''

        return tx_hash
