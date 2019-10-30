from asciimatics.widgets import Label, Divider, Text, TextBox
from viewmodels.listing.state import State

def inject_listing_state(layout, col=0):
    layout.add_widget(Label('Listing'), col)
    layout.add_widget(Divider(line_char='-'), col)
    layout.add_widget(Text('Address:', 'listing_address'), col)
    layout.add_widget(Text('Owner:', 'listing_owner'), col)
    # TODO in the actual upcoming live implementation figure out how to dynamically set the height
    layout.add_widget(TextBox(3, label='Listings:', name='listings'), col)

def hydrate_listing_state(data={}):
    """
    Given a dictionary, allow the viewmodel to hydrate the data needed by this view
    """
    vm = State()
    return vm.hydrate(data)
