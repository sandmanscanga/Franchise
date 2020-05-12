from objects.table import Table


class Position(Table):

    def __init__(self):
        self.values = (
            ('QB', "Quarterback"),
            ('RB', "Running Back"),
            ('FB', "Fullback"),
            ('WR', "Wide Receiver"),
            ('TE', "Tight End"),
            ('P', "Punter"),
            ('PK', "Placekicker"),
            ('LS', "Long Snapper"),
            ('C', "Center"),
            ('G', "Guard"),
            ('OT', "Offensive Tackle"),
            ('NT', "Nose Tackle"),
            ('DT', "Defensive Tackle"),
            ('DE', "Defensive End"),
            ('LB', "Linebacker"),
            ('CB', "Cornerback"),
            ('S', "Safety")
        )
        self.keys = ("name", "fullname")
        self.model = "app.position"
