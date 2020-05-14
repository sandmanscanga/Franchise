from framework.table import Table
from objects.player import Player


class PlayerNav(Table):

    def __init__(self):
        players = Player()
        self.values = tuple(players.playernavs)
        self.keys = ("home", "headshot")
        self.model = "app.playernav"
