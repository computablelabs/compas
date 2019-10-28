from asciimatics.widgets import Label, Divider, Text
from viewmodels.reserve.state import State
"""
Our subviews simply take a layout and inject their content into it
"""
def inject_reserve_state(layout, col=0):
    layout.add_widget(Label('Reserve'), col)
    layout.add_widget(Divider(line_char='-'), col)
    layout.add_widget(Text('Address:', 'reserve_address'), col)
    layout.add_widget(Text('Owner:', 'reserve_owner'), col)
    layout.add_widget(Text('Support Price:', 'reserve_support_price'), col)
    layout.add_widget(Text('Withdrawal Proceeds:', 'reserve_withdrawal_proceeds'), col)

def hydrate_reserve_state(data={}):
    """
    Given a dictionary, allow the viewmodel to hydrate the data needed by this view
    """
    vm = State()
    return vm.hydrate(data)
