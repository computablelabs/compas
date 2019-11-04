from asciimatics.widgets import Layout, Label, Text, Button
from viewmodels.listing.detail import Detail as VM
from views.detail import Detail
from widgets.popup import PopUpDialog

class Detail(Detail):
    def __init__(self, screen):
        super(Detail, self).__init__(screen, screen.height, screen.width,
            hover_focus=True, can_scroll = False, title='::Listing::', reduce_cpu=True)

        self.check_theme()
        # keep a pointer to the viewmodel so my super methods work correctly
        self.vm = VM()

        self.inject_header()

        # create a 4 col layout minus any dividers for main
        main = Layout([15,40,40,5], fill_frame=True)
        self.add_layout(main)

        self.inject_get_address_and_owner(main, 4)

        self.inject_is_listed(main)
        self.inject_dividers(main, 4)
        self.inject_get_listing(main)
        self.inject_dividers(main, 4)
        self.inject_list(main)
        self.inject_dividers(main, 4)
        self.inject_withdraw_from_listing(main)
        self.inject_dividers(main, 4)
        self.inject_resolve_application(main)
        self.inject_dividers(main, 4)
        self.inject_claim_access_reward(main)
        self.inject_dividers(main, 4)
        self.inject_challenge(main)
        self.inject_dividers(main, 4)
        self.inject_resolve_challenge(main)
        self.inject_dividers(main, 4)
        self.inject_exit(main)

        self.inject_footer()

        self.fix()

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
        gas_price = self.data.get('gas_price')
        if hash and gas_price:
            res = self.vm.list(hash, gas_price)
            self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_withdraw_from_listing(self, layout):
        layout.add_widget(Label('Withdraw from Listing'), 0)
        layout.add_widget(Text(label='Hash:', name='withdraw_hash', on_change=self.on_changed), 1)
        layout.add_widget(Text(label='Amount:', name='withdraw_amount', on_change=self.on_changed), 2)
        layout.add_widget(Button('Send', self.withdraw_from_listing), 3)

    def withdraw_from_listing(self):
        hash = self.data.get('withdraw_hash')
        amount = self.data.get('withdraw_amount')
        gas_price = self.data.get('gas_price')
        if hash and amount and gas_price:
            res = self.vm.withdraw_from_listing(hash, amount, gas_price)
            self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_resolve_application(self, layout):
        layout.add_widget(Label('Resolve Application'), 0)
        layout.add_widget(Text(label='Hash:', name='resolve_application_hash', on_change=self.on_changed), 1)
        layout.add_widget(Label(' '), 2)
        layout.add_widget(Button('Send', self.resolve_application), 3)

    def resolve_application(self):
        hash = self.data.get('resolve_application_hash')
        gas_price = self.data.get('gas_price')
        if hash and gas_price:
            res = self.vm.resolve_application(hash, gas_price)
            self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_claim_access_reward(self, layout):
        layout.add_widget(Label('Claim Access Reward'), 0)
        layout.add_widget(Text(label='Hash:', name='claim_hash', on_change=self.on_changed), 1)
        layout.add_widget(Label(' '), 2)
        layout.add_widget(Button('Send', self.claim_access_reward), 3)

    def claim_access_reward(self):
        hash = self.data.get('claim_hash')
        gas_price = self.data.get('gas_price')
        if hash and gas_price:
            res = self.vm.claim_access_reward(hash, gas_price)
            self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_challenge(self, layout):
        layout.add_widget(Label('Challenge'), 0)
        layout.add_widget(Text(label='Hash:', name='challenge_hash', on_change=self.on_changed), 1)
        layout.add_widget(Label(' '), 2)
        layout.add_widget(Button('Send', self.challenge), 3)

    def challenge(self):
        hash = self.data.get('challenge_hash')
        gas_price = self.data.get('gas_price')
        if hash and gas_price:
            res = self.vm.challenge(hash, gas_price)
            self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_resolve_challenge(self, layout):
        layout.add_widget(Label('Resolve Challenge'), 0)
        layout.add_widget(Text(label='Hash:', name='resolve_challenge_hash', on_change=self.on_changed), 1)
        layout.add_widget(Label(' '), 2)
        layout.add_widget(Button('Send', self.resolve_challenge), 3)

    def resolve_challenge(self):
        hash = self.data.get('resolve_challenge_hash')
        gas_price = self.data.get('gas_price')
        if hash and gas_price:
            res = self.vm.resolve_challenge(hash, gas_price)
            self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_exit(self, layout):
        layout.add_widget(Label('Exit'), 0)
        layout.add_widget(Text(label='Hash:', name='exit_hash', on_change=self.on_changed), 1)
        layout.add_widget(Label(' '), 2)
        layout.add_widget(Button('Send', self.exit), 3)

    def exit(self):
        hash = self.data.get('exit_hash')
        gas_price = self.data.get('gas_price')
        if hash and gas_price:
            res = self.vm.exit(hash, gas_price)
            self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))
