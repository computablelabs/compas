from asciimatics.widgets import Label, Divider, Text, Button
from viewmodels.ethertoken.state import State
"""
Our subviews simply take a layout and inject their content into it
"""
def inject_ether_token_state(layout, col=0):
    layout.add_widget(Label('Ether Token'), col)
    layout.add_widget(Divider(line_char='-'), col)
    supply_box = Text('Total Supply:', 'ether_token_total_supply')
    supply_box.disabled = True
    layout.add_widget(supply_box, col)
    bal_box = Text('Balance:', 'ether_token_balance')
    bal_box.disabled = True
    layout.add_widget(bal_box, col)

def hydrate_ether_token_state(data={}):
    """
    Given a dictionary, allow the viewmodel to hydrate the data needed by this view
    """
    vm = State()
    return vm.hydrate(data)
