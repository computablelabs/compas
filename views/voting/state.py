from asciimatics.widgets import Label, Divider, Text, TextBox
from viewmodels.voting.state import State

def inject_voting_state(layout, col=0):
    layout.add_widget(Label('Voting'), col)
    layout.add_widget(Divider(line_char='-'), col)
    layout.add_widget(Text('Address:', 'voting_address'), col)
    layout.add_widget(Text('Owner:', 'voting_owner'), col)
    # TODO in the actual upcoming live implementation figure out how to dynamically set the height
    layout.add_widget(TextBox(5, label='Candidates:', name='voting_candidates'), col)

def hydrate_voting_state(data={}):
    """
    Given a dictionary, allow the viewmodel to hydrate the data needed by this view
    """
    vm = State()
    return vm.hydrate(data)
