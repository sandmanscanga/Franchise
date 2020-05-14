from framework.table import Table
from objects.team import Team


class Profile(Table):

    def __init__(self):
        teams = Team()
        self.values = tuple(teams.profiles)
        self.keys = (
            "abbr", "location", "name",
            "fullname", "divrank"
        )
        self.model = "app.profile"
