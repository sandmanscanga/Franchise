from framework.driver import get_nfl_json
from framework.table import Table
from objects.team import Team
from objects.position import Position


class Player(Table):

    def __init__(self):
        self.playernavs = []

        nfl_json = get_nfl_json()

        positions = Position()
        teams = Team()

        players = []

        for team_json in nfl_json.values():
            team_json = team_json.get("roster")
            team_json = team_json.get("page").get("content")
            team_json = team_json.get("roster")

            _player_team = team_json.get("team").get("uid")
            player_team = teams.find(_player_team)

            groups = team_json.get("groups")
            for group in groups:
                athletes = group.get("athletes")
                for athlete in athletes:
                    playernav_home = athlete.get("href")
                    playernav_headshot = athlete.get("headshot")
                    playernav = (playernav_home, playernav_headshot)
                    self.playernavs.append(playernav)

                    player_uid = athlete.get("uid")
                    player_guid = athlete.get("guid")
                    player_name = athlete.get("name")

                    if "nophoto" in playernav_headshot:
                        player_headshot = "/static/app/nophoto.jpg"
                    else:
                        player_headshot = f"/static/app/headshots/{player_guid}.png"

                    _player_position = athlete.get("position")
                    player_position = positions.find(_player_position)

                    players.append((
                        player_uid,
                        player_guid,
                        player_headshot,
                        player_name,
                        player_position,
                        player_team
                    ))

        self.values = tuple(players)
        self.keys = ("uid", "guid", "headshot", "name", "position", "team")
        self.model = "app.player"
        self.key = "guid"
