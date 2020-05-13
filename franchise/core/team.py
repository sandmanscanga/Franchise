from rsync import get_nfl_json
from table import Table
from division import Division
from region import Region

class Team(Table):

    def __init__(self):
        teams = []

        divisions = Division()
        regions = Region()

        nfl_json = get_nfl_json()
        for json_data in nfl_json.values():
            team_json = json_data.get("roster")
            team_json = team_json.get("page").get("content")
            profile = team_json.get("roster").get("team")

            uid = profile.get("uid")
            abbrev = profile.get("abbrev")
            logo = f"/static/app/logos/{abbrev}.png"

            standingSummary = profile.get("standingSummary")
            div_reg = standingSummary.split(" in ")[-1]
            (_div, _reg) = div_reg.split()
            div = divisions.find(_div)
            reg = regions.find(_reg)

            team = (uid, logo, div, reg)
            teams.append(team)

        self.values = tuple(teams)
        self.keys = ("uid", "logo", "division", "region")
        self.model = "app.team"
