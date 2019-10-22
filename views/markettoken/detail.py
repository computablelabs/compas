from asciimatics.widgets import Frame, Layout, Divider, Label, Text, Button
from constants import scenes as S
from models.ui import UI
from viewmodels.markettoken.detail import Detail as VM
from views.tokendetail import TokenDetail
from widgets.popup import PopUpDialog

class Detail(TokenDetail):
    def __init__(self, screen):
        super(Detail, self).__init__(screen, screen.height, screen.width,
            hover_focus=True, can_scroll = True, title='FFA::MarketToken', reduce_cpu=True)

        ui = UI()
        self.set_theme(ui.get_current_theme())

        # keep a pointer to the viewmodel so my super methods work correctly
        self.vm = VM()
        # create a 5 col layout minus any dividers for main
        main = Layout([1,1,1,1,1], fill_frame=True)
        self.add_layout(main)
        # add contract methods, common first
        self.inject_common(main)

        self.inject_set_privileged(main)
        self.inject_dividers(main)
        self.inject_get_privileged(main)
        self.inject_dividers(main)
        self.inject_has_privilege(main)

        # divide the two layout sections
        br = Layout([100])
        self.add_layout(br)
        br.add_widget(Divider())
        # create a row of controls
        controls = Layout([1,1,1,1,1])
        self.add_layout(controls)
        controls.add_widget(Button('Dashboard', self.dashboard), 4)

        self.fix()

    def inject_set_privileged(self, layout):
        layout.add_widget(Label('Set Privileged'), 0)
        layout.add_widget(Text(label='Reserve:', name='set_privileged_reserve', on_change=self.on_changed), 1)
        layout.add_widget(Text(label='Listing:', name='set_privileged_listing', on_change=self.on_changed), 2)
        layout.add_widget(Label(' '), 3) # placeholders so that our borders don't shift around
        layout.add_widget(Button('Send', self.set_privileged), 4)

    def set_privileged(self):
        reserve = self.data.get('set_privileged_reserve')
        listing = self.data.get('set_privileged_listing')
        if reserve and listing:
            res = self.vm.set_privileged(reserve, listing)
            self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_get_privileged(self, layout):
        layout.add_widget(Label('Get Privileged'), 0)
        layout.add_widget(Label(' '), 1)
        layout.add_widget(Label(' '), 2)
        layout.add_widget(Label(' '), 3)
        layout.add_widget(Button('Call', self.get_privileged), 4)


    def get_privileged(self):
        # we'll use the viewmodel to relay commands
        res = self.vm.get_privileged()
        self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_has_privilege(self, layout):
        layout.add_widget(Label('Has Privilege'), 0)
        layout.add_widget(Text(label='Address:', name='has_privilege_address', on_change=self.on_changed), 1)
        layout.add_widget(Label(' '), 2)
        layout.add_widget(Label(' '), 3)
        layout.add_widget(Button('Call', self.get_has_privilege), 4)

    def get_has_privilege(self):
        address = self.data.get('has_privilege_address')
        res = self.vm.has_privilege(address)
        self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

