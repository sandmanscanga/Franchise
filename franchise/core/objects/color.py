from framework.table import Table
from objects.team import Team


class Color(Table):

    def __init__(self):
        teams = Team()
        self.values = tuple(teams.colors)
        self.keys = ("main", "alt")
        self.model = "app.color"
