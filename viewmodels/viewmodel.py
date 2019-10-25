"""
Base class for all ViewModels

Notes:
    Viewmodels understand they are serving as the 'presenter' for a view. As such it is the responsibility
    of the viewmodel to translate/transform types and arguments as it hands them off to a view.

    Viewmodels know about models, but not about contracts (computable.py).

    There may be many view models that interact with one model in different ways - state and detail
    viewmodels for example.

    Views know about viewmodels, but not about models.
"""
class ViewModel:
    def transact(self, tx_hash):
        if tx_hash == None:
            tx_hash = ''

        return tx_hash
