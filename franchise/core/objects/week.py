from framework.table import Table
from framework.driver import get_nfl_json
from objects.season import Season
from objects.seasontype import SeasonType
# from objects.eventstatus import EventStatus
import datetime
import json


class Week(Table):

    def __init__(self):
        seasontypes = SeasonType()
        seasons = Season()

        preseason = [
            "Hall of Fame Weekend",
            "Preseason Week 1",
            "Preseason Week 2",
            "Preseason Week 3",
            "Preseason Week 4"
        ]
        regular_season = [
            "Week 1",
            "Week 2",
            "Week 3",
            "Week 4",
            "Week 5",
            "Week 6",
            "Week 7",
            "Week 8",
            "Week 9",
            "Week 10",
            "Week 11",
            "Week 12",
            "Week 13",
            "Week 14",
            "Week 15",
            "Week 16",
            "Week 17"
        ]
        playoffs = [
            "Wild Card",
            "Divisional Round",
            "Conference Championship",
            "Pro Bowl",
            "Super Bowl"
        ]

        weeks = []

        _season = 2020
        season = seasons.find(_season)
        _weeks = (preseason, regular_season, playoffs)
        _seasontypes = ("Preseason", "Regular Season", "Playoffs")
        for _week_group, _seasontype in zip(_weeks, _seasontypes):
            seasontype = seasontypes.find(_seasontype)
            for _week in _week_group:
                week = (_week, seasontype, season)
                weeks.append(week)

        self.values = tuple(weeks)
        self.keys = ("name", "seasontype", "season")
        self.model = "app.week"
