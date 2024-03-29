"""
Entry point for the Computable ASCII text-user-interface
"""
import sys
# from asciimatics.widgets import Frame, Layout, Widget, Divider, Text
from asciimatics.scene import Scene
from asciimatics.screen import Screen
# from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication
from asciimatics.exceptions import ResizeScreenError
from constants import scenes as S
from views.dashboard import Dashboard
from views.ethertoken.detail import Detail as EtherToken
from views.markettoken.detail import Detail as MarketToken
from views.voting.detail import Detail as Voting
from views.parameterizer.detail import Detail as Parameterizer
from views.reserve.detail import Detail as Reserve
from views.datatrust.detail import Detail as Datatrust
from views.listing.detail import Detail as Listing

last_scene = None

def app(screen, scene):
    scenes = [
        Scene([Dashboard(screen)], -1, name=S['DASHBOARD']),
        Scene([EtherToken(screen)], -1, name=S['ETHER_TOKEN']),
        Scene([MarketToken(screen)], -1, name=S['MARKET_TOKEN']),
        Scene([Voting(screen)], -1, name=S['VOTING']),
        Scene([Parameterizer(screen)], -1, name=S['PARAMETERIZER']),
        Scene([Reserve(screen)], -1, name=S['RESERVE']),
        Scene([Datatrust(screen)], -1, name=S['DATATRUST']),
        Scene([Listing(screen)], -1, name=S['LISTING']),
    ]

    screen.play(scenes, stop_on_resize=True, start_scene=scene, allow_int=True)

if __name__ == '__main__':
    while True:
        try:
            Screen.wrapper(app, catch_interrupt=True, arguments=[last_scene])
            sys.exit(0)
        except ResizeScreenError as e:
            last_scene = e.scene
