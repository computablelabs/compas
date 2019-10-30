from asciimatics.widgets import Frame, Layout, Divider, Label, Text, Button
from asciimatics.exceptions import NextScene
from constants import scenes as S
from models.ui import UI
from viewmodels.listing.detail import Detail as VM
from widgets.popup import PopUpDialog

class Detail(Frame):
    def __init__(self, screen):
        super(Detail, self).__init__(screen, screen.height, screen.width,
            hover_focus=True, can_scroll = False, title='FFA::Reserve', reduce_cpu=True)

        ui = UI()
        self.set_theme(ui.get_current_theme())

        # keep a pointer to the viewmodel so my super methods work correctly
        self.vm = VM()
        # create a 4 col layout minus any dividers for main
        main = Layout([15,40,40,5], fill_frame=True)
        self.add_layout(main)

        self.inject_get_address(main)
        self.inject_dividers(main)
        self.inject_get_owner(main)
        self.inject_dividers(main)

        self.inject_is_listed(main)
        self.inject_dividers(main)
        self.inject_get_listing(main)
        self.inject_dividers(main)
        self.inject_list(main)
        self.inject_dividers(main)
        self.inject_withdraw_from_listing(main)
        self.inject_dividers(main)
        self.inject_resolve_application(main)
        self.inject_dividers(main)
        self.inject_claim_access_reward(main)
        self.inject_dividers(main)
        self.inject_challenge(main)
        self.inject_dividers(main)
        self.inject_resolve_challenge(main)
        self.inject_dividers(main)
        self.inject_exit(main)
        self.inject_dividers(main)


        # divide the two layout sections
        br = Layout([100])
        self.add_layout(br)
        br.add_widget(Divider())
        # create a row of controls
        controls = Layout([1,1,1,1,1])
        self.add_layout(controls)
        controls.add_widget(Button('Dashboard', self.dashboard), 4)

        self.fix()

    def inject_get_address(self, layout):
        layout.add_widget(Label('Get Address'), 0)
        layout.add_widget(Label(' '), 1)
        layout.add_widget(Label(' '), 2)
        layout.add_widget(Button('Call', self.get_address), 3)

    def get_address(self):
        # we'll use the viewmodel to relay commands
        res = self.vm.get_address()
        self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_get_owner(self, layout):
        layout.add_widget(Label('Get Owner'), 0)
        layout.add_widget(Label(' '), 1)
        layout.add_widget(Label(' '), 2)
        layout.add_widget(Button('Call', self.get_owner), 3)

    def get_owner(self):
        # we'll use the viewmodel to relay commands
        res = self.vm.get_owner()
        self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_is_listed(self, layout):
        layout.add_widget(Label('Is Listed'), 0)
        layout.add_widget(Text(label='Hash:', name='is_listed_hash', on_change=self.on_changed), 1)
        layout.add_widget(Label(' '), 2)
        layout.add_widget(Button('Call', self.is_listed), 3)

    def is_listed(self):
        hash = self.data.get('is_listed_hash')
        res = self.vm.is_listed(hash)
        self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_get_listing(self, layout):
        layout.add_widget(Label('Get Listing'), 0)
        layout.add_widget(Text(label='Hash:', name='get_listing_hash', on_change=self.on_changed), 1)
        layout.add_widget(Label(' '), 2)
        layout.add_widget(Button('Call', self.get_listing), 3)

    def get_listing(self):
        hash = self.data.get('get_listing_hash')
        res = self.vm.get_listing(hash)
        self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_list(self, layout):
        layout.add_widget(Label('List'), 0)
        layout.add_widget(Text(label='Hash:', name='list_hash', on_change=self.on_changed), 1)
        layout.add_widget(Label(' '), 2)
        layout.add_widget(Button('Send', self.list), 3)

    def list(self):
        hash = self.data.get('list_hash')
        if hash:
            res = self.vm.list(hash)
            self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_withdraw_from_listing(self, layout):
        layout.add_widget(Label('Withdraw from Listing'), 0)
        layout.add_widget(Text(label='Hash:', name='withdraw_hash', on_change=self.on_changed), 1)
        layout.add_widget(Text(label='Amount:', name='withdraw_amount', on_change=self.on_changed), 2)
        layout.add_widget(Button('Send', self.withdraw_from_listing), 3)

    def withdraw_from_listing(self):
        hash = self.data.get('withdraw_hash')
        amount = self.data.get('withdraw_amount')
        if hash and amount:
            res = self.vm.withdraw_from_listing(hash, amount)
            self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_resolve_application(self, layout):
        layout.add_widget(Label('Resolve Application'), 0)
        layout.add_widget(Text(label='Hash:', name='resolve_application_hash', on_change=self.on_changed), 1)
        layout.add_widget(Label(' '), 2)
        layout.add_widget(Button('Send', self.resolve_application), 3)

    def resolve_application(self):
        hash = self.data.get('resolve_application_hash')
        if hash:
            res = self.vm.resolve_application(hash)
            self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_claim_access_reward(self, layout):
        layout.add_widget(Label('Claim Access Reward'), 0)
        layout.add_widget(Text(label='Hash:', name='claim_hash', on_change=self.on_changed), 1)
        layout.add_widget(Label(' '), 2)
        layout.add_widget(Button('Send', self.claim_access_reward), 3)

    def claim_access_reward(self):
        hash = self.data.get('claim_hash')
        if hash:
            res = self.vm.claim_access_reward(hash)
            self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_challenge(self, layout):
        layout.add_widget(Label('Challenge'), 0)
        layout.add_widget(Text(label='Hash:', name='challenge_hash', on_change=self.on_changed), 1)
        layout.add_widget(Label(' '), 2)
        layout.add_widget(Button('Send', self.challenge), 3)

    def challenge(self):
        hash = self.data.get('challenge_hash')
        if hash:
            res = self.vm.challenge(hash)
            self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_resolve_challenge(self, layout):
        layout.add_widget(Label('Resolve Challenge'), 0)
        layout.add_widget(Text(label='Hash:', name='resolve_challenge_hash', on_change=self.on_changed), 1)
        layout.add_widget(Label(' '), 2)
        layout.add_widget(Button('Send', self.resolve_challenge), 3)

    def resolve_challenge(self):
        hash = self.data.get('resolve_challenge_hash')
        if hash:
            res = self.vm.resolve_challenge(hash)
            self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_exit(self, layout):
        layout.add_widget(Label('Exit'), 0)
        layout.add_widget(Text(label='Hash:', name='exit_hash', on_change=self.on_changed), 1)
        layout.add_widget(Label(' '), 2)
        layout.add_widget(Button('Send', self.exit), 3)

    def exit(self):
        hash = self.data.get('exit_hash')
        if hash:
            res = self.vm.exit(hash)
            self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_dividers(self, layout):
        for i in range(4):
            layout.add_widget(Divider(line_char='-'), i)

    def on_changed(self):
        self.save()

    def dashboard(self):
        raise NextScene(S['DASHBOARD'])
