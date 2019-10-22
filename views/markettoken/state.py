from asciimatics.widgets import Label, Divider, Text, Button
from viewmodels.markettoken.state import State
"""
Our subviews simply take a layout and inject their content into it
"""
def inject_market_token_state(layout, col=0):
    layout.add_widget(Label('Market Token'), col)
    layout.add_widget(Divider(line_char='-'), col)
    layout.add_widget(Text('Total Supply:', 'market_token_total_supply'), col)
    layout.add_widget(Text('Balance:', 'market_token_balance'), col)
    layout.add_widget(Label('Allowances: {'), col)
    layout.add_widget(Text('  Voting :', 'market_token_voting_allowance'), col)
    layout.add_widget(Text('  Listing:', 'market_token_listing_allowance'), col)
    layout.add_widget(Label('}'), col)

def hydrate_market_token_state(data={}):
    """
    Given a dictionary, allow the viewmodel to hydrate the data needed by this view
    """
    vm = State()
    return vm.hydrate(data)
