from asciimatics.widgets import Label, Divider, Text
from viewmodels.parameterizer.state import State
"""
Our subviews simply take a layout and inject their content into it
"""
def inject_parameterizer_state(layout, col=0):
    layout.add_widget(Label('Parameterizer'), col)
    layout.add_widget(Divider(line_char='-'), col)
    layout.add_widget(Text('Cost Per Byte:', 'p11r_cost_per_byte'), col)
    layout.add_widget(Text('Stake:', 'p11r_stake'), col)
    layout.add_widget(Text('Price Floor:', 'p11r_price_floor'), col)
    layout.add_widget(Text('Spread:', 'p11r_spread'), col)
    layout.add_widget(Text('List Reward:', 'p11r_list_reward'), col)
    layout.add_widget(Text('Plurality:', 'p11r_plurality'), col)
    layout.add_widget(Text('Vote By:', 'p11r_vote_by'), col)
    layout.add_widget(Text('Maker Payment:', 'p11r_maker_payment'), col)
    layout.add_widget(Text('Datatrust Payment:', 'p11r_backend_payment'), col)
    layout.add_widget(Text('Reserve Payment:', 'p11r_reserve_payment'), col)

def hydrate_parameterizer_state(data={}):
    """
    Given a dictionary, allow the viewmodel to hydrate the data needed by this view
    """
    vm = State()
    return vm.hydrate(data)
