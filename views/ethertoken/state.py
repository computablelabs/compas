from asciimatics.widgets import Label, Divider, Text, Button
from viewmodels.ethertoken.state import State
"""
Our subviews simply take a layout and inject their content into it
"""
def inject_ether_token_state(layout, col=0):
    layout.add_widget(Label('Ether Token'), col)
    layout.add_widget(Divider(line_char='-'), col)
    layout.add_widget(Text('Total Supply:', 'ether_token_total_supply'), col)
    layout.add_widget(Text('Balance:', 'ether_token_balance'), col)
    layout.add_widget(Label('Allowances: {'), col)
    layout.add_widget(Text('  Reserve:', 'ether_token_reserve_allowance'), col)
    layout.add_widget(Text('  Datatrust:', 'ether_token_datatrust_allowance'), col)
    layout.add_widget(Label('}'), col)

def hydrate_ether_token_state(data={}):
    """
    Given a dictionary, allow the viewmodel to hydrate the data needed by this view
    """
    vm = State()
    return vm.hydrate(data)
