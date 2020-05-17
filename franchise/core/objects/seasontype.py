from framework.table import Table


class SeasonType(Table):

    def __init__(self):
        self.values = (
            ("Preseason", "pre"),
            ("Regular Season", "reg"),
            ("Playoffs", "post")
        )
        self.keys = ("name", "abbr")
        self.model = "app.seasontype"
