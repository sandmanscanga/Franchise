from framework.table import Table
from objects.teamstat import TeamStat


class OppStat(Table):

    def __init__(self):
        teamstats = TeamStat()
        self.values = tuple(teamstats.oppstats)
        self.keys = ("value", "string")
        self.model = "app.oppstat"
