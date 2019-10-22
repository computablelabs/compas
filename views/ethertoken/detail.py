from asciimatics.widgets import Frame, Layout, Divider, Label, Text, Button
from constants import scenes as S
from models.ui import UI
from viewmodels.ethertoken.detail import Detail as VM
from views.tokendetail import TokenDetail
from widgets.popup import PopUpDialog

class Detail(TokenDetail):
    def __init__(self, screen):
        super(Detail, self).__init__(screen, screen.height, screen.width,
            hover_focus=True, can_scroll = True, title='FFA::EtherToken', reduce_cpu=True)

        ui = UI()
        self.set_theme(ui.get_current_theme())

        # keep a pointer to the viewmodel so my super methods work correctly
        self.vm = VM()
        # create a 5 col layout minus any dividers for main
        main = Layout([1,1,1,1,1], fill_frame=True)
        self.add_layout(main)
        # add contract methods, common first
        self.inject_common(main)

        self.inject_deposit(main)
        self.inject_dividers(main)
        self.inject_withdraw(main)
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

    def inject_deposit(self, layout):
        layout.add_widget(Label('Deposit'), 0)
        layout.add_widget(Text(label='Amount:', name='deposit_amount', on_change=self.on_changed), 1)
        layout.add_widget(Label(' '), 2)
        layout.add_widget(Label(' '), 3)
        layout.add_widget(Button('Send', self.send_deposit), 4)

    def send_deposit(self):
        amount = self.data.get('deposit_amount')
        if amount:
            res = self.vm.deposit(amount)
            self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_withdraw(self, layout):
        layout.add_widget(Label('Withdraw'), 0)
        layout.add_widget(Text(label='Amount:', name='withdraw_amount', on_change=self.on_changed), 1)
        layout.add_widget(Label(' '), 2)
        layout.add_widget(Label(' '), 3)
        layout.add_widget(Button('Send', self.send_withdraw), 4)

    def send_withdraw(self):
        amount = self.data.get('withdraw_amount')
        if amount:
            res = self.vm.withdraw(amount)
            self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))
