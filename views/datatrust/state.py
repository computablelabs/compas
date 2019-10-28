from asciimatics.widgets import Label, Divider, Text
from viewmodels.datatrust.state import State
"""
Our subviews simply take a layout and inject their content into it
"""
def inject_datatrust_state(layout, col=0):
    layout.add_widget(Label('Datatrust'), col)
    layout.add_widget(Divider(line_char='-'), col)
    layout.add_widget(Text('Address:', 'datatrust_address'), col)
    layout.add_widget(Text('Owner:', 'datatrust_owner'), col)
    layout.add_widget(Text('Backend Address:', 'datatrust_backend_address'), col)
    layout.add_widget(Text('Backend URL:', 'datatrust_backend_url'), col)

def hydrate_datatrust_state(data={}):
    """
    Given a dictionary, allow the viewmodel to hydrate the data needed by this view
    """
    vm = State()
    return vm.hydrate(data)
