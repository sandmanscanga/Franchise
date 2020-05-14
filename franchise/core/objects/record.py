from framework.table import Table
from objects.team import Team


class Record(Table):

    def __init__(self):
        teams = Team()
        self.values = tuple(teams.records)
        self.keys = ("win", "loss", "draw")
        self.model = "app.record"
