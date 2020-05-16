from framework.driver import get_nfl_json
from framework.table import Table
from objects.stat import Stat
from objects.player import Player
from objects.team import Team


class PlayerStat(Table):

    def __init__(self):
        nfl_json = get_nfl_json()

        stats = Stat()
        players = Player()
        teams = Team()

        playerstats = []

        for team_json in nfl_json.values():
            team_json = team_json.get("stats")
            team_json = team_json.get("page").get("content")
            team_json = team_json.get("stats")

            _team = team_json.get("team").get("uid")
            team = teams.find(_team)

            for statGroups in team_json.get("playerStats"):
                for statGroup in statGroups:

                    _player = statGroup.get("athlete").get("guid")
                    try:
                        player = players.find(_player)
                    except Exception:
                        continue

                    groups = statGroup.get("statGroups")

                    for group_stat in groups.get("stats"):
                        if "stats" in group_stat:
                            for group_substat in group_stat.get("stats"):
                                _ps_stat = group_substat.get("name")
                                ps_stat = stats.find(_ps_stat)

                                (ps_value, ps_string) = stats._eval_stat(group_substat)

                                playerstat = (ps_value, ps_string, ps_stat, player, team)
                                playerstats.append(playerstat)
                        else:
                            _ps_stat = group_stat.get("name")
                            ps_stat = stats.find(_ps_stat)

                            (ps_value, ps_string) = stats._eval_stat(group_stat)

                            playerstat = (ps_value, ps_string, ps_stat, player, team)
                            playerstats.append(playerstat)

        self.values = tuple(playerstats)
        self.keys = ("value", "string", "stat", "player", "team")
        self.model = "app.playerstat"
