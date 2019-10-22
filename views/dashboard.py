from functools import partial
from asciimatics.widgets import Frame, Layout, Divider, VerticalDivider, Button, Label
from asciimatics.exceptions import StopApplication, NextScene
from constants import scenes as S
from .ethertoken.state import inject_ether_token_state, hydrate_ether_token_state
from .markettoken.state import inject_market_token_state, hydrate_market_token_state
from models.ui import UI

class Dashboard(Frame):
    def __init__(self, screen):
        super(Dashboard, self).__init__(screen, screen.height, screen.width,
            hover_focus=True, can_scroll = True, title='FFA::Dashboard', reduce_cpu=True)

        ui = UI()
        self.set_theme(ui.get_current_theme())
        # create a 4 column layout for the dashboard main
        # nav | 1 | 2 | 3
        main = Layout([9,1,29,1,29,1,30], fill_frame=True)
        self.add_layout(main)
        # add the divider(s)
        main.add_widget(VerticalDivider(), 1)
        main.add_widget(VerticalDivider(), 3)
        main.add_widget(VerticalDivider(), 5)
        # add detail view controls to nav
        main.add_widget(Button('EtherToken', partial(self.detail, S['ETHER_TOKEN'])), 0)
        main.add_widget(Divider(line_char=''))
        main.add_widget(Button('MarketToken', partial(self.detail, S['MARKET_TOKEN'])), 0)
        # add the state widgets to the dashboard
        inject_ether_token_state(main, 2)
        inject_market_token_state(main, 4)
        # divide the two layout sections
        br = Layout([100])
        self.add_layout(br)
        br.add_widget(Divider())
        # create a row of controls
        controls = Layout([1,1,1,1,1])
        self.add_layout(controls)

        self.prev_theme_button = Button('Prev Theme', self.prev_theme)
        controls.add_widget(self.prev_theme_button, 0)

        self.next_theme_button = Button('Next Theme', self.next_theme)
        controls.add_widget(self.next_theme_button, 1)

        controls.add_widget(Button('Exit', self.exit), 4)

        self.fix()

    # TODO we _could_ have empty widgets if this mass reset takes too long...
    def reset(self):
        super(Dashboard, self).reset()

        self.data = hydrate_ether_token_state()
        self.data = hydrate_market_token_state(self.data)

    def next_theme(self):
        ui = UI()
        self.set_theme(ui.next_theme())

    def prev_theme(self):
        ui = UI()
        self.set_theme(ui.prev_theme())

    @staticmethod
    def detail(which):
        raise NextScene(which)

    @staticmethod
    def exit():
        raise StopApplication('User terminated session')
