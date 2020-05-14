from framework.driver import get_nfl_json
from framework.table import Table
from objects.division import Division


class Team(Table):

    def __init__(self):
        self.records = []
        self.profiles = []
        self.colors = []
        self.teamnavs = []

        teams = []

        nfl_json = get_nfl_json()

        divisions = Division()

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

            ## Record
            record_summary = profile.get("recordSummary")
            if not record_summary:
                self.records.append((0, 0, 0))
            else:
                wld = [int(_) for _ in record_summary.split("-")]
                (win, loss) = (wld[0], wld[1])
                draw = 0 if len(wld) == 2 else wld[2]
                self.records.append((win, loss, draw))

            ## Profiles
            self.profiles.append((
                abbrev,
                profile.get("location"),
                profile.get("shortDisplayName"),
                profile.get("displayName"),
                int(standingSummary.split(" in ")[0][0])
            ))

            ## Colors
            self.colors.append((
                profile.get("teamColor"),
                profile.get("altColor")
            ))

            ## TeamNavs
            subnav = team_json.get("subNavigation")

            teamnav_list = []
            for item in subnav.get("items")[:-1]:
                href = item.get("l").get("w").get("h")
                teamnav_list.append("https://www.espn.com" + href)

            logo_url = profile.get("logo")
            teamnav_list.append(logo_url)

            teamnav = tuple(teamnav_list)
            self.teamnavs.append(teamnav)

        self.values = tuple(teams)
        self.keys = ("uid", "logo", "division")
        self.model = "app.team"
