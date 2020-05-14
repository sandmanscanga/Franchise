from framework.driver import get_nfl_json
from framework.table import Table
from objects.division import Division

class Team(Table):

    def __init__(self):
        teams = []

        divisions = Division()

        nfl_json = get_nfl_json()

        for json_data in nfl_json.values():
            team_json = json_data.get("roster")
            team_json = team_json.get("page").get("content")
            profile = team_json.get("roster").get("team")

            uid = profile.get("uid")
            abbrev = profile.get("abbrev")
            logo = f"/static/app/logos/{abbrev}.png"

            standingSummary = profile.get("standingSummary")
            _div = standingSummary.split(" in ")[-1]
            div = divisions.find(_div)

            team = (uid, logo, div)
            teams.append(team)

        self.values = tuple(teams)
        self.keys = ("uid", "logo", "division")
        self.model = "app.team"
