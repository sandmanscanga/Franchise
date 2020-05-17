from framework.table import Table


class EventStatus(Table):

    def __init__(self):
        self.values = (
            ("Scheduled", "pre"),
            ("Completed", "post")
        )
        self.keys = ("name", "abbr")
        self.model = "app.eventstatus"
        self.key = "abbr"
