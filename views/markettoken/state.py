from asciimatics.widgets import Label, Divider, Text, Button
from viewmodels.markettoken.state import State
"""
Our subviews simply take a layout and inject their content into it
"""
def inject_market_token_state(layout, col=0):
    layout.add_widget(Label('Market Token'), col)
    layout.add_widget(Divider(line_char='-'), col)
    supply_box = Text('Total Supply:', 'market_token_total_supply')
    supply_box.disabled = True
    layout.add_widget(supply_box, col)
    bal_box = Text('Balance:', 'market_token_balance')
    bal_box.disabled = True
    layout.add_widget(bal_box, col)

def hydrate_market_token_state(data={}):
    """
    Given a dictionary, allow the viewmodel to hydrate the data needed by this view
    """
    vm = State()
    return vm.hydrate(data)
