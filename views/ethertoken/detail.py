from asciimatics.widgets import Layout, Label, Text, Button
from viewmodels.ethertoken.detail import Detail as VM
from views.tokendetail import TokenDetail
from widgets.popup import PopUpDialog

class Detail(TokenDetail):
    def __init__(self, screen):
        super(Detail, self).__init__(screen, screen.height, screen.width,
            hover_focus=True, can_scroll = False, title='::EtherToken::', reduce_cpu=True)

        # if a theme has been persisted, set it
        self.check_theme()
        # keep a pointer to the viewmodel so my super methods work correctly
        self.vm = VM()
        # first add the header
        self.inject_header()
        # create a 5 col layout minus any dividers for main
        main = Layout([11,28,28,28,5], fill_frame=True)
        self.add_layout(main)
        # add contract methods, common first
        self.inject_common(main, 5)

        self.inject_deposit(main)
        self.inject_dividers(main, 5)
        self.inject_withdraw(main)
        self.inject_dividers(main, 5)

        self.inject_footer()

        self.fix()

    def inject_deposit(self, layout):
        layout.add_widget(Label('Deposit'), 0)
        layout.add_widget(Text(label='Amount:', name='deposit_amount', on_change=self.on_changed), 1)
        layout.add_widget(Label(' '), 2)
        layout.add_widget(Label(' '), 3)
        layout.add_widget(Button('Send', self.deposit), 4)

    def deposit(self):
        amount = self.data.get('deposit_amount')
        gas_price = self.data.get('gas_price')
        if amount and gas_price:
            res = self.vm.deposit(amount, gas_price)
            self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_withdraw(self, layout):
        layout.add_widget(Label('Withdraw'), 0)
        layout.add_widget(Text(label='Amount:', name='withdraw_amount', on_change=self.on_changed), 1)
        layout.add_widget(Label(' '), 2)
        layout.add_widget(Label(' '), 3)
        layout.add_widget(Button('Send', self.withdraw), 4)

    def withdraw(self):
        amount = self.data.get('withdraw_amount')
        gas_price = self.data.get('gas_price')
        if amount and gas_price:
            res = self.vm.withdraw(amount, gas_price)
            self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))
