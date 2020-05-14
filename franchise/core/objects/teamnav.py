from framework.table import Table
from objects.team import Team


class TeamNav(Table):

    def __init__(self):
        teams = Team()
        self.values = tuple(teams.teamnavs)
        self.keys = (
            "home", "stats", "schedule",
            "roster", "depthchart", "injuries",
            "transactions", "blog", "logo"
        )
        self.model = "app.teamnav"
