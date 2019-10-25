from asciimatics.widgets import Frame, Layout, Divider, Label, Text, Button
from asciimatics.exceptions import NextScene
from constants import scenes as S
from models.ui import UI
from viewmodels.voting.detail import Detail as VM
from widgets.popup import PopUpDialog

class Detail(Frame):
    def __init__(self, screen):
        super(Detail, self).__init__(screen, screen.height, screen.width,
            hover_focus=True, can_scroll = False, title='FFA::Reserve', reduce_cpu=True)

        ui = UI()
        self.set_theme(ui.get_current_theme())

        # keep a pointer to the viewmodel so my super methods work correctly
        self.vm = VM()
        # create a 5 col layout minus any dividers for main
        main = Layout([11,28,28,28,5], fill_frame=True)
        self.add_layout(main)

        self.inject_is_candidate(main)
        self.inject_dividers(main)
        self.inject_candidate_is(main)
        self.inject_dividers(main)
        self.inject_get_candidate(main)
        self.inject_dividers(main)
        self.inject_did_pass(main)
        self.inject_dividers(main)
        self.inject_poll_closed(main)
        self.inject_dividers(main)
        self.inject_vote(main)
        self.inject_dividers(main)
        self.inject_get_stake(main)
        self.inject_dividers(main)
        self.inject_unstake(main)
        self.inject_dividers(main)

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

    def inject_is_candidate(self, layout):
        layout.add_widget(Label('Is Candidate'), 0)
        layout.add_widget(Text(label='Hash:', name='is_candidate_hash', on_change=self.on_changed), 1)
        layout.add_widget(Label(' '), 2)
        layout.add_widget(Label(' '), 3)
        layout.add_widget(Button('Call', self.get_is_candidate), 4)

    def get_is_candidate(self):
        hash = self.data.get('is_candidate_hash')
        res = self.vm.is_candidate(hash)
        self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_candidate_is(self, layout):
        layout.add_widget(Label('Candidate Is'), 0)
        layout.add_widget(Text(label='Hash:', name='candidate_is_hash', on_change=self.on_changed), 1)
        layout.add_widget(Text(label='Kind:', name='candidate_is_kind', on_change=self.on_changed), 2)
        layout.add_widget(Label(' '), 3)
        layout.add_widget(Button('Call', self.get_candidate_is), 4)

    def get_candidate_is(self):
        hash = self.data.get('candidate_is_hash')
        kind = self.data.get('candidate_is_kind')
        res = self.vm.candidate_is(hash, kind)
        self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_get_candidate(self, layout):
        layout.add_widget(Label('Get Candidate'), 0)
        layout.add_widget(Text(label='Hash:', name='get_candidate_hash', on_change=self.on_changed), 1)
        layout.add_widget(Label(' '), 2)
        layout.add_widget(Label(' '), 3)
        layout.add_widget(Button('Call', self.get_candidate), 4)

    def get_candidate(self):
        hash = self.data.get('get_candidate_hash')
        res = self.vm.get_candidate(hash)
        self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_did_pass(self, layout):
        layout.add_widget(Label('Did Pass'), 0)
        layout.add_widget(Text(label='Hash:', name='did_pass_hash', on_change=self.on_changed), 1)
        layout.add_widget(Text(label='Plurality:', name='did_pass_plurality', on_change=self.on_changed), 2)
        layout.add_widget(Label(' '), 3)
        layout.add_widget(Button('Call', self.get_did_pass), 4)

    def get_did_pass(self):
        hash = self.data.get('did_pass_hash')
        pl = self.data.get('did_pass_plurality')
        res = self.vm.did_pass(hash, pl)
        self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_poll_closed(self, layout):
        layout.add_widget(Label('Poll Closed'), 0)
        layout.add_widget(Text(label='Hash:', name='poll_closed_hash', on_change=self.on_changed), 1)
        layout.add_widget(Label(' '), 2)
        layout.add_widget(Label(' '), 3)
        layout.add_widget(Button('Call', self.get_poll_closed), 4)

    def get_poll_closed(self):
        hash = self.data.get('poll_closed_hash')
        res = self.vm.poll_closed(hash)
        self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_vote(self, layout):
        layout.add_widget(Label('Vote'), 0)
        layout.add_widget(Text(label='Hash:', name='vote_hash', on_change=self.on_changed), 1)
        layout.add_widget(Text(label='Option:', name='vote_option', on_change=self.on_changed), 2)
        layout.add_widget(Label(' '), 3)
        layout.add_widget(Button('Send', self.send_vote), 4)

    def send_vote(self):
        hash = self.data.get('vote_hash')
        option = self.data.get('vote_option')
        if hash and option:
            res = self.vm.vote(hash, option)
            self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_get_stake(self, layout):
        layout.add_widget(Label('Get Stake'), 0)
        layout.add_widget(Text(label='Hash:', name='get_stake_hash', on_change=self.on_changed), 1)
        layout.add_widget(Text(label='Address:', name='get_stake_address', on_change=self.on_changed), 2)
        layout.add_widget(Label(' '), 3)
        layout.add_widget(Button('Call', self.get_stake), 4)

    def get_stake(self):
        hash = self.data.get('get_stake_hash')
        addr = self.data.get('get_stake_address')
        res = self.vm.get_stake(hash, addr)
        self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_unstake(self, layout):
        layout.add_widget(Label('Unstake'), 0)
        layout.add_widget(Text(label='Hash:', name='unstake_hash', on_change=self.on_changed), 1)
        layout.add_widget(Label(' '), 2)
        layout.add_widget(Label(' '), 3)
        layout.add_widget(Button('Send', self.send_unstake), 4)

    def send_unstake(self):
        hash = self.data.get('unstake_hash')
        if hash:
            res = self.vm.unstake(hash)
            self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_set_privileged(self, layout):
        layout.add_widget(Label('Set Privileged'), 0)
        layout.add_widget(Text(label='Parameterizer:', name='set_privileged_parameterizer', on_change=self.on_changed), 1)
        layout.add_widget(Text(label='Datatrust:', name='set_privileged_datatrust', on_change=self.on_changed), 2)
        layout.add_widget(Text(label='Listing:', name='set_privileged_listing', on_change=self.on_changed), 3)
        layout.add_widget(Button('Send', self.send_set_privileged), 4)

    def send_set_privileged(self):
        parameterizer = self.data.get('set_privileged_parameterizer')
        datatrust = self.data.get('set_privileged_datatrust')
        listing = self.data.get('set_privileged_listing')
        if parameterizer and datatrust and listing:
            res = self.vm.set_privileged(parameterizer, datatrust, listing)
            self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_get_privileged(self, layout):
        layout.add_widget(Label('Get Privileged'), 0)
        layout.add_widget(Label(' '), 1)
        layout.add_widget(Label(' '), 2)
        layout.add_widget(Label(' '), 3)
        layout.add_widget(Button('Call', self.get_privileged), 4)

    def get_privileged(self):
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

    def inject_dividers(self, layout):
        for i in range(5):
            layout.add_widget(Divider(line_char='-'), i)

    def on_changed(self):
        self.save()

    def dashboard(self):
        raise NextScene(S['DASHBOARD'])
