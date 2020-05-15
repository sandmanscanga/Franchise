from framework.driver import get_nfl_json
from framework.table import Table
from objects.category import Category
import json


class Stat(Table):

    def __init__(self):
        nfl_json = get_nfl_json()

        categories = Category()

        stats = []
        for team_json in nfl_json.values():
            team_json = team_json.get("stats")
            team_json = team_json.get("page").get("content")
            team_json = team_json.get("stats").get("dictionary")
            for stat_json in team_json.values():
                stat_abbr = stat_json.get("abbrev")
                stat_name = stat_json.get("statName")
                stat_shortdesc = stat_json.get("shortDesc")
                stat_fulldesc = stat_json.get("desc")
                _stat_category = stat_json.get("group")
                stat_category = categories.find(_stat_category)
                stat = (
                    stat_abbr,
                    stat_name,
                    stat_shortdesc,
                    stat_fulldesc,
                    stat_category
                )
                stats.append(stat)
            break

        self.values = tuple(stats)
        self.keys = ("abbr", "name", "shortdesc", "fulldesc", "category")
        self.model = "app.stat"
        self.key = "abbr"
