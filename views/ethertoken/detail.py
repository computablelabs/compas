from asciimatics.widgets import Frame, Layout, Divider, Label, Text, Button
from asciimatics.exceptions import NextScene
from constants import scenes as S
from viewmodels.ethertoken.detail import Detail as VM
from widgets.popup import PopUpDialog

class Detail(Frame):
    def __init__(self, screen):
        super(Detail, self).__init__(screen, screen.height, screen.width,
            hover_focus=True, can_scroll = True, title='FFA::EtherToken', reduce_cpu=True)

        # create a 5 col layout minus any dividers for main
        main = Layout([1,1,1,1,1], fill_frame=True)
        self.add_layout(main)
        # add contract methods
        self.inject_allowance(main)
        self.inject_dividers(main)
        self.inject_approve(main)
        self.inject_dividers(main)
        self.inject_balance_of(main)
        # divide the two layout sections
        br = Layout([100])
        self.add_layout(br)
        br.add_widget(Divider())
        # create a row of controls
        controls = Layout([1,1,1,1,1])
        self.add_layout(controls)
        controls.add_widget(Button('Dashboard', self.dashboard), 4)

        self.fix()

    def inject_dividers(self, layout):
        """
        seperates each method from the next
        """
        for i in range(5):
            layout.add_widget(Divider(line_char='-'), i)

    def inject_allowance(self, layout):
        """
        place the allowance getter across the colums
        """
        layout.add_widget(Label('Allowance'), 0)
        layout.add_widget(Text(label='Owner:', name='allowance_owner', on_change=self.on_changed), 1)
        layout.add_widget(Text(label='Spender:', name='allowance_spender', on_change=self.on_changed), 2)
        layout.add_widget(Label(' '), 3) # placeholders so that our borders don't shift around
        layout.add_widget(Button('Get', self.get_allowance), 4)

    def get_allowance(self):
        owner = self.data.get('allowance_owner')
        spender = self.data.get('allowance_spender')
        if spender: # owner will default if omitted
            vm = VM()
            res = vm.allowance(owner, spender)
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
            vm = VM()
            res = vm.approve(spender, amount)
            self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_balance_of(self, layout):
        """
        place the balance getter across the colums
        """
        layout.add_widget(Label('Balance Of'), 0)
        layout.add_widget(Text(label='Owner:', name='balance_of_owner', on_change=self.on_changed), 1)
        layout.add_widget(Button('Get', self.get_balance_of), 4)

    def get_balance_of(self):
        owner = self.data.get('balance_of_owner') # can be blank, will default to env
        # we'll use the viewmodel to relay commands
        vm = VM()
        res = vm.balance_of(owner)
        self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def on_changed(self):
        self.save()

    def dashboard(self):
        raise NextScene(S['DASHBOARD'])
