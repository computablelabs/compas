"""
Abstraction of common functionality for all contract detail views
"""
from asciimatics.widgets import Frame, Layout, Divider, Label, Button
from asciimatics.exceptions import NextScene
from constants import scenes as S
from models.ui import UI
from widgets.popup import PopUpDialog

class Detail(Frame):
    def check_theme(self):
        ui = UI()
        self.set_theme(ui.get_current_theme())

    def inject_get_address_and_owner(self, layout, n):
        self.inject_get_address(layout, n)
        self.inject_dividers(layout, n)
        self.inject_get_owner(layout, n)
        self.inject_dividers(layout, n)

    def inject_get_address(self, layout, n):
        last = n-1
        layout.add_widget(Label('Get Address'), 0)
        # fill any spaces between...
        for c in range(1, last):
            layout.add_widget(Label(' '), c)
        layout.add_widget(Button('Call', self.get_address), last)

    def get_address(self):
        # we'll use the viewmodel to relay commands
        res = self.vm.get_address()
        self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_get_owner(self, layout, n):
        last = n-1
        layout.add_widget(Label('Get Owner'), 0)
        for c in range(1, last):
            layout.add_widget(Label(' '), c)
        layout.add_widget(Button('Call', self.get_owner), last)

    def get_owner(self):
        # we'll use the viewmodel to relay commands
        res = self.vm.get_owner()
        self._scene.add_effect(PopUpDialog(self._screen, res, ['OK'], has_shadow=True))

    def inject_footer(self):
        """
        Every detail has at least the <Dashboard> control in it.
        The other 4 slots are open for use...
        """
        br = Layout([100])
        self.add_layout(br)
        br.add_widget(Divider())
        # create a row of controls
        controls = Layout([1,1,1,1,1])
        self.add_layout(controls)
        controls.add_widget(Button('Dashboard', self.dashboard), 4)

    def inject_dividers(self, layout, n):
        for i in range(n):
            layout.add_widget(Divider(line_char='-'), i)

    def on_changed(self):
        self.save()

    def dashboard(self):
        raise NextScene(S['DASHBOARD'])
