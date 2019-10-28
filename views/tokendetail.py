"""
Base class for the 2 token detail scenes
"""
from asciimatics.widgets import Frame, Layout, Divider, Label, Text, Button
from asciimatics.exceptions import NextScene
from constants import scenes as S
from viewmodels.ethertoken.detail import Detail as VM
from widgets.popup import PopUpDialog

class TokenDetail(Frame):
    def inject_dividers(self, layout):
        for i in range(5):
            layout.add_widget(Divider(line_char='-'), i)

    def inject_common(self, layout):
        """
        common controls to both tokens
        """
        self.inject_get_address(layout)
        self.inject_dividers(layout)
        self.inject_get_owner(layout)
        self.inject_dividers(layout)
        self.inject_get_symbol(layout)
        self.inject_dividers(layout)
        self.inject_get_decimals(layout)
        self.inject_dividers(layout)
        self.inject_get_total_supply(layout)
        self.inject_dividers(layout)
        self.inject_get_balance_of(layout)
        self.inject_dividers(layout)
        self.inject_get_allowance(layout)
        self.inject_dividers(layout)
        self.inject_approve(layout)
        self.inject_dividers(layout)
        self.inject_increase_allowance(layout)
        self.inject_dividers(layout)
        self.inject_decrease_allowance(layout)
        self.inject_dividers(layout)
        self.inject_transfer(layout)
        self.inject_dividers(layout)
        self.inject_transfer_from(layout)
        self.inject_dividers(layout)

    def inject_get_address(self, layout):
        layout.add_widget(Label('Get Address'), 0)
        layout.add_widget(Label(' '), 1)
        layout.add_widget(Label(' '), 2)
        layout.add_widget(Label(' '), 3)
        layout.add_widget(Button('Call', self.get_address), 4)

    def get_address(self):
        # we'll use the viewmodel to relay commands
        res = self.vm.get_address()
        self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_get_owner(self, layout):
        layout.add_widget(Label('Get Owner'), 0)
        layout.add_widget(Label(' '), 1)
        layout.add_widget(Label(' '), 2)
        layout.add_widget(Label(' '), 3)
        layout.add_widget(Button('Call', self.get_owner), 4)

    def get_owner(self):
        # we'll use the viewmodel to relay commands
        res = self.vm.get_owner()
        self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_get_symbol(self, layout):
        layout.add_widget(Label('Get Symbol'), 0)
        layout.add_widget(Label(' '), 1)
        layout.add_widget(Label(' '), 2)
        layout.add_widget(Label(' '), 3)
        layout.add_widget(Button('Call', self.get_symbol), 4)

    def get_symbol(self):
        # we'll use the viewmodel to relay commands
        res = self.vm.get_symbol()
        self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_get_decimals(self, layout):
        layout.add_widget(Label('Get Decimals'), 0)
        layout.add_widget(Label(' '), 1)
        layout.add_widget(Label(' '), 2)
        layout.add_widget(Label(' '), 3)
        layout.add_widget(Button('Call', self.get_decimals), 4)

    def get_decimals(self):
        res = self.vm.get_decimals()
        self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_get_total_supply(self, layout):
        layout.add_widget(Label('Total Supply'), 0)
        layout.add_widget(Label(' '), 1)
        layout.add_widget(Label(' '), 2)
        layout.add_widget(Label(' '), 3)
        layout.add_widget(Button('Call', self.get_total_supply), 4)

    def get_total_supply(self):
        res = self.vm.total_supply()
        self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_get_balance_of(self, layout):
        """
        place the balance getter across the colums
        """
        layout.add_widget(Label('Balance Of'), 0)
        layout.add_widget(Text(label='Owner:', name='balance_of_owner', on_change=self.on_changed), 1)
        layout.add_widget(Label(' '), 2)
        layout.add_widget(Label(' '), 3)
        layout.add_widget(Button('Call', self.get_balance_of), 4)

    def get_balance_of(self):
        owner = self.data.get('balance_of_owner') # can be blank, will default to env
        res = self.vm.balance_of(owner)
        self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_get_allowance(self, layout):
        layout.add_widget(Label('Allowance'), 0)
        layout.add_widget(Text(label='Owner:', name='allowance_owner', on_change=self.on_changed), 1)
        layout.add_widget(Text(label='Spender:', name='allowance_spender', on_change=self.on_changed), 2)
        layout.add_widget(Label(' '), 3) # placeholders so that our borders don't shift around
        layout.add_widget(Button('Call', self.get_allowance), 4)

    def get_allowance(self):
        owner = self.data.get('allowance_owner')
        spender = self.data.get('allowance_spender')
        if spender: # owner will default if omitted
            res = self.vm.allowance(owner, spender)
            self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_approve(self, layout):
        layout.add_widget(Label('Approve'), 0)
        layout.add_widget(Text(label='Spender:', name='approve_spender', on_change=self.on_changed), 1)
        layout.add_widget(Text(label='Amount:', name='approve_amount', on_change=self.on_changed), 2)
        layout.add_widget(Label(' '), 3) # placeholders so that our borders don't shift around
        layout.add_widget(Button('Send', self.send_approve), 4)

    def send_approve(self):
        spender = self.data.get('approve_spender')
        amount = self.data.get('approve_amount')
        if spender and amount:
            res = self.vm.approve(spender, amount)
            self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_increase_allowance(self, layout):
        layout.add_widget(Label('Increase Allowance'), 0)
        layout.add_widget(Text(label='Spender:', name='increase_allowance_spender', on_change=self.on_changed), 1)
        layout.add_widget(Text(label='Amount:', name='increase_allowance_amount', on_change=self.on_changed), 2)
        layout.add_widget(Label(' '), 3) # placeholders so that our borders don't shift around
        layout.add_widget(Button('Send', self.send_increase_allowance), 4)

    def send_increase_allowance(self):
        spender = self.data.get('increase_allowance_spender')
        amount = self.data.get('increase_allowance_amount')
        if spender and amount:
            res = self.vm.increase_allowance(spender, amount)
            self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_decrease_allowance(self, layout):
        layout.add_widget(Label('Decrease Allowance'), 0)
        layout.add_widget(Text(label='Spender:', name='decrease_allowance_spender', on_change=self.on_changed), 1)
        layout.add_widget(Text(label='Amount:', name='decrease_allowance_amount', on_change=self.on_changed), 2)
        layout.add_widget(Label(' '), 3) # placeholders so that our borders don't shift around
        layout.add_widget(Button('Send', self.send_decrease_allowance), 4)

    def send_decrease_allowance(self):
        spender = self.data.get('decrease_allowance_spender')
        amount = self.data.get('decrease_allowance_amount')
        if spender and amount:
            res = self.vm.decrease_allowance(spender, amount)
            self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_transfer(self, layout):
        layout.add_widget(Label('Transfer'), 0)
        layout.add_widget(Text(label='To:', name='transfer_to', on_change=self.on_changed), 1)
        layout.add_widget(Text(label='Amount:', name='transfer_amount', on_change=self.on_changed), 2)
        layout.add_widget(Label(' '), 3) # placeholders so that our borders don't shift around
        layout.add_widget(Button('Send', self.send_transfer), 4)

    def send_transfer(self):
        to = self.data.get('transfer_to')
        amount = self.data.get('transfer_amount')
        if to and amount:
            res = self.vm.transfer(to, amount)
            self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_transfer_from(self, layout):
        layout.add_widget(Label('Transfer From'), 0)
        layout.add_widget(Text(label='Source:', name='transfer_from_source', on_change=self.on_changed), 1)
        layout.add_widget(Text(label='To:', name='transfer_from_to', on_change=self.on_changed), 2)
        layout.add_widget(Text(label='Amount:', name='transfer_from_amount', on_change=self.on_changed), 3)
        layout.add_widget(Button('Send', self.send_transfer_from), 4)

    def send_transfer_from(self):
        source = self.data.get('transfer_from_source')
        to = self.data.get('transfer_from_to')
        amount = self.data.get('transfer_from_amount')
        if source and to and amount:
            res = self.vm.transfer_from(source, to, amount)
            self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def on_changed(self):
        self.save()

    def dashboard(self):
        raise NextScene(S['DASHBOARD'])
