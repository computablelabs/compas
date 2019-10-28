from asciimatics.widgets import Frame, Layout, Divider, Label, Text, Button
from asciimatics.exceptions import NextScene
from constants import scenes as S
from models.ui import UI
from viewmodels.parameterizer.detail import Detail as VM
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
        self.inject_get_cost_per_byte(main)
        self.inject_dividers(main)
        self.inject_get_stake(main)
        self.inject_dividers(main)
        self.inject_get_price_floor(main)
        self.inject_dividers(main)
        self.inject_get_spread(main)
        self.inject_dividers(main)
        self.inject_get_list_reward(main)
        self.inject_dividers(main)
        self.inject_get_plurality(main)
        self.inject_dividers(main)
        self.inject_get_vote_by(main)
        self.inject_dividers(main)
        self.inject_get_hash(main)
        self.inject_dividers(main)
        self.inject_get_maker_payment(main)
        self.inject_dividers(main)
        self.inject_get_backend_payment(main)
        self.inject_dividers(main)
        self.inject_get_reserve_payment(main)
        self.inject_dividers(main)
        self.inject_get_reparam(main)
        self.inject_dividers(main)

        self.inject_reparameterize(main)
        self.inject_dividers(main)
        self.inject_resolve_reparam(main)

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

    def inject_get_cost_per_byte(self, layout):
        layout.add_widget(Label('Get Cost Per Byte'), 0)
        layout.add_widget(Label(' '), 1)
        layout.add_widget(Label(' '), 2)
        layout.add_widget(Button('Call', self.get_cost_per_byte), 3)

    def get_cost_per_byte(self):
        res = self.vm.get_cost_per_byte()
        self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_get_stake(self, layout):
        layout.add_widget(Label('Get Stake'), 0)
        layout.add_widget(Label(' '), 1)
        layout.add_widget(Label(' '), 2)
        layout.add_widget(Button('Call', self.get_stake), 3)

    def get_stake(self):
        res = self.vm.get_stake()
        self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_get_price_floor(self, layout):
        layout.add_widget(Label('Get Price Floor'), 0)
        layout.add_widget(Label(' '), 1)
        layout.add_widget(Label(' '), 2)
        layout.add_widget(Button('Call', self.get_price_floor), 3)

    def get_price_floor(self):
        res = self.vm.get_price_floor()
        self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_get_spread(self, layout):
        layout.add_widget(Label('Get Spread'), 0)
        layout.add_widget(Label(' '), 1)
        layout.add_widget(Label(' '), 2)
        layout.add_widget(Button('Call', self.get_spread), 3)

    def get_spread(self):
        res = self.vm.get_spread()
        self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_get_list_reward(self, layout):
        layout.add_widget(Label('Get List Reward'), 0)
        layout.add_widget(Label(' '), 1)
        layout.add_widget(Label(' '), 2)
        layout.add_widget(Button('Call', self.get_list_reward), 3)

    def get_list_reward(self):
        res = self.vm.get_list_reward()
        self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_get_plurality(self, layout):
        layout.add_widget(Label('Get Plurality'), 0)
        layout.add_widget(Label(' '), 1)
        layout.add_widget(Label(' '), 2)
        layout.add_widget(Button('Call', self.get_plurality), 3)

    def get_plurality(self):
        res = self.vm.get_plurality()
        self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_get_vote_by(self, layout):
        layout.add_widget(Label('Get Vote By'), 0)
        layout.add_widget(Label(' '), 1)
        layout.add_widget(Label(' '), 2)
        layout.add_widget(Button('Call', self.get_vote_by), 3)

    def get_vote_by(self):
        res = self.vm.get_vote_by()
        self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_get_maker_payment(self, layout):
        layout.add_widget(Label('Get Maker Payment'), 0)
        layout.add_widget(Label(' '), 1)
        layout.add_widget(Label(' '), 2)
        layout.add_widget(Button('Call', self.get_maker_payment), 3)

    def get_maker_payment(self):
        res = self.vm.get_maker_payment()
        self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_get_backend_payment(self, layout):
        layout.add_widget(Label('Get Backend Payment'), 0)
        layout.add_widget(Label(' '), 1)
        layout.add_widget(Label(' '), 2)
        layout.add_widget(Button('Call', self.get_backend_payment), 3)

    def get_backend_payment(self):
        res = self.vm.get_backend_payment()
        self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_get_reserve_payment(self, layout):
        layout.add_widget(Label('Get Reserve Payment'), 0)
        layout.add_widget(Label(' '), 1)
        layout.add_widget(Label(' '), 2)
        layout.add_widget(Button('Call', self.get_reserve_payment), 3)

    def get_reserve_payment(self):
        res = self.vm.get_reserve_payment()
        self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_get_hash(self, layout):
        layout.add_widget(Label('Get Hash'), 0)
        layout.add_widget(Text(label='Param:', name='get_hash_param', on_change=self.on_changed), 1)
        layout.add_widget(Text(label='Value:', name='get_hash_value', on_change=self.on_changed), 2)
        layout.add_widget(Button('Call', self.get_hash), 3)

    def get_hash(self):
        param = self.data.get('get_hash_param')
        value = self.data.get('get_hash_value')
        res = self.vm.get_hash(param, value)
        self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_get_reparam(self, layout):
        layout.add_widget(Label('Get Reparam'), 0)
        layout.add_widget(Text(label='Hash:', name='get_reparam_hash', on_change=self.on_changed), 1)
        layout.add_widget(Label(' '), 2)
        layout.add_widget(Button('Call', self.get_reparam), 3)

    def get_reparam(self):
        hash = self.data.get('get_reparam_hash')
        res = self.vm.get_reparam(hash)
        self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_reparameterize(self, layout):
        layout.add_widget(Label('Reparameterize'), 0)
        layout.add_widget(Text(label='Param:', name='reparameterize_param', on_change=self.on_changed), 1)
        layout.add_widget(Text(label='Value:', name='reparameterize_value', on_change=self.on_changed), 2)
        layout.add_widget(Button('Send', self.send_reparameterize), 3)

    def send_reparameterize(self):
        param = self.data.get('reparameterize_param')
        value = self.data.get('reparameterize_value')
        if param and value:
            res = self.vm.reparameterize(param, value)
            self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_resolve_reparam(self, layout):
        layout.add_widget(Label('Resolve Reparam'), 0)
        layout.add_widget(Text(label='Hash:', name='resolve_reparam_hash', on_change=self.on_changed), 1)
        layout.add_widget(Label(' '), 2)
        layout.add_widget(Button('Send', self.send_resolve_reparam), 3)

    def send_resolve_reparam(self):
        hash = self.data.get('resolve_reparam_hash')
        if hash:
            res = self.vm.resolve_reparam(hash)
            self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_dividers(self, layout):
        for i in range(4):
            layout.add_widget(Divider(line_char='-'), i)

    def on_changed(self):
        self.save()

    def dashboard(self):
        raise NextScene(S['DASHBOARD'])
