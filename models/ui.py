import os
"""
Since a singleton can't carry UI data across the app, write stuff
to a file and read it
"""

THEMES = ['default', 'monochrome', 'tlj256', 'green']
THEME_FILE = 'theme.txt'

class UI:
    current_theme = None

    def get_current_theme(self):
        if not self.current_theme:
            theme = self.read_theme()
            if not theme:
                theme = 'default'
            self.current_theme = theme

        return self.current_theme

    def next_theme(self):
        if not self.current_theme:
            self.get_current_theme()

        i = THEMES.index(self.current_theme)

        if i < 3:
            i += 1
        else:
            i = 0

        self.current_theme = THEMES[i]
        self.write_theme()

        return self.current_theme

    def prev_theme(self):
        if not self.current_theme:
            self.get_current_theme()

        i = THEMES.index(self.current_theme)

        if i > 0:
            i -= 1
        else:
            i = 3

        self.current_theme = THEMES[i]
        self.write_theme()

        return self.current_theme

    def read_theme(self):
        path = os.path.join(os.path.dirname(__file__), THEME_FILE)
        f = open(path, 'r')
        theme = f.read()
        f.close()
        return theme

    def write_theme(self):
        path = os.path.join(os.path.dirname(__file__), THEME_FILE)
        f = open(path, 'w')
        f.write(self.current_theme)
        f.close()
