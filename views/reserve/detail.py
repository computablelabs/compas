from asciimatics.widgets import Layout, Label, Text, Button
from viewmodels.reserve.detail import Detail as VM
from views.detail import Detail
from widgets.popup import PopUpDialog

class Detail(Detail):
    def __init__(self, screen):
        super(Detail, self).__init__(screen, screen.height, screen.width,
            hover_focus=True, can_scroll = False, title='::Reserve::', reduce_cpu=True)

        self.check_theme()
        # keep a pointer to the viewmodel so my super methods work correctly
        self.vm = VM()
        # create a 3 col layout minus any dividers for main
        main = Layout([1,1,1], fill_frame=True)
        self.add_layout(main)

        self.inject_get_address_and_owner(main, 3)

        self.inject_get_support_price(main)
        self.inject_dividers(main, 3)
        self.inject_get_withdrawal_proceeds(main)
        self.inject_dividers(main, 3)
        self.inject_support(main)
        self.inject_dividers(main, 3)
        self.inject_withdraw(main)

        self.inject_footer()

        self.fix()

    def inject_get_support_price(self, layout):
        layout.add_widget(Label('Support Price'), 0)
        layout.add_widget(Label(' '), 1) # placeholders so that our borders don't shift around
        layout.add_widget(Button('Call', self.get_support_price), 2)

    def get_support_price(self):
        res = self.vm.get_support_price()
        self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_get_withdrawal_proceeds(self, layout):
        layout.add_widget(Label('Withdrawal Proceeds'), 0)
        layout.add_widget(Text(label='Address:', name='withdrawal_proceeds_address', on_change=self.on_changed), 1)
        layout.add_widget(Button('Call', self.get_withdrawal_proceeds), 2)

    def get_withdrawal_proceeds(self):
        addr = self.data.get('withdrawal_proceeds_address')
        res = self.vm.get_withdrawal_proceeds(addr)
        self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_support(self, layout):
        layout.add_widget(Label('Support'), 0)
        layout.add_widget(Text(label='Offer:', name='support_offer', on_change=self.on_changed), 1)
        layout.add_widget(Button('Send', self.support), 2)

    def support(self):
        offer = self.data.get('support_offer')
        if offer:
            res = self.vm.support(offer)
            self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_withdraw(self, layout):
        layout.add_widget(Label('Withdraw'), 0)
        layout.add_widget(Label(' '), 1) # placeholders so that our borders don't shift around
        layout.add_widget(Button('Send', self.withdraw), 2)

    def withdraw(self):
        res = self.vm.withdraw()
        self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))
