"""
Abstraction of common functionality for all contract detail views
"""
from asciimatics.widgets import Frame

class Detail(Frame):
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
