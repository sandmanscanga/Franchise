from framework.driver import get_nfl_json
from framework.table import Table
from objects.team import Team
from objects.profile import Profile
from objects.eventstatus import EventStatus
from objects.week import Week


class Event(Table):

    def __init__(self):
        events = []

        nfl_json = get_nfl_json()

        teams = Team()
        profiles = Profile()
        eventstatuses = EventStatus()
        weeks = Week()
        
        for team_json in nfl_json.values():
            team_json = team_json.get("schedule")
            team_json = team_json.get("page").get("content")
            team_json = team_json.get("scheduleData")
            team = teams.find(team_json.get("team").get("uid"))
            for s in team_json.get("teamSchedule"):
                # season = seasons.find(s.get("season"))
                # seasontype = seasontypes.find(s.get("title"))
                # print(s.get("events").keys())
                # dict_keys(['pre', 'post'])
                for k, v in s.get("events").items():
                    eventstatus = eventstatuses.find(k)
                    if v:
                        for e in v:
                            # print(e.keys())
                            # dict_keys(['date', 'opponent', 'time', 'tickets', 'network', 'result', 'timeAndNetwork', 'record', 'seasonType', 'status', 'notes', 'competitionKey', 'competitionName', 'week'])
                            # _ = e.pop("competitionName")
                            # _ = e.pop("competitionKey")
                            # _ = e.pop("notes")
                            # _ = e.pop("tickets")
                            # _ = e.pop("network")
                            # _ = e.pop("date")
                            # _ = e.pop("timeAndNetwork")
                            # _ = e.pop("seasonType")
                            # print(e.keys())
                            # dict_keys(['opponent', 'time', 'result', 'record', 'status'])
                            # _ = e.pop("opponent")
                            # _ = e.pop("result")
                            # _ = e.pop("record")

                            _week = e.get("week").get("text")
                            if _week is None:
                                continue

                            week = weeks.find(_week)
                            event_time = e.get("time").get("time")

                            opponent = profiles.find(e.get("opponent").get("abbrev"), key="abbr")
                            homeaway = e.get("opponent").get("homeAwaySymbol")

                            event = (event_time, homeaway, team, opponent, eventstatus, week)
                            events.append(event)

        self.values = tuple(events)
        self.keys = ("time", "homeaway", "team", "opponent", "eventstatus", "week")
        self.model = "app.event"
