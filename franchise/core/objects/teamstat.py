from framework.driver import get_nfl_json
from framework.table import Table
from objects.stat import Stat
from objects.team import Team


class TeamStat(Table):

    def __init__(self):
        self.oppstats = []

        nfl_json = get_nfl_json()

        stats = Stat()
        teams = Team()

        teamstats = []

        for team_json in nfl_json.values():
            team_json = team_json.get("stats")
            team_json = team_json.get("page").get("content")
            team_json = team_json.get("stats")

            _ts_team = team_json.get("team").get("uid")
            ts_team = teams.find(_ts_team)

            for ts_json in team_json.get("teamStats").get("team"):
                for ts_stat_json in ts_json.get("stats"):

                    _ts_stat = ts_stat_json.get("name")

                    if _ts_stat is not None:
                        ts_stat = stats.find(_ts_stat)

                        (ts_value, ts_string) = self._eval_stat(ts_stat_json)

                        teamstat = (ts_value, ts_string, ts_stat, ts_team)
                        teamstats.append(teamstat)
                    else:
                        for ts_substat_json in ts_stat_json.get("stats"):

                            _ts_stat = ts_substat_json.get("name")
                            ts_stat = stats.find(_ts_stat)

                            (ts_value, ts_string) = self._eval_stat(ts_substat_json)

                            teamstat = (ts_value, ts_string, ts_stat, ts_team)
                            teamstats.append(teamstat)

            for os_json in team_json.get("teamStats").get("opponent"):
                for os_stat_json in os_json.get("stats"):

                    _os_stat = os_stat_json.get("name")

                    if _os_stat is not None:

                        (os_value, os_string) = self._eval_stat(os_stat_json)

                        oppstat = (os_value, os_string)
                        self.oppstats.append(oppstat)
                    else:
                        for os_substat_json in os_stat_json.get("stats"):

                            (os_value, os_string) = self._eval_stat(os_substat_json)

                            oppstat = (os_value, os_string)
                            self.oppstats.append(oppstat)

        self.values = tuple(teamstats)
        self.keys = ("value", "string", "stat", "team")
        self.model = "app.teamstat"
        # for v in self.values:
        #     print(type(v[0]))

    def _eval_stat(self, json_dict):
        value = json_dict.get("value")
        string = json_dict.get("displayValue")

        if isinstance(value, int):
            value = float(value)
        elif isinstance(value, str):
            if string in ("0", ""):
                value = 0.0
                string = "0.0"
            elif "-" in string:
                (_points, _total) = string.split("-")
                if int(_total) == 0:
                    value = 0.0
                else:
                    value = int(_points) / int(_total)

        return (value, string)
