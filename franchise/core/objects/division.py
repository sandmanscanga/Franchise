from framework.table import Table


class Division(Table):

    def __init__(self):
        self.values = (
            ("AFC North",), ("AFC East",),
            ("AFC South",), ("AFC West",),
            ("NFC North",), ("NFC East",),
            ("NFC South",), ("NFC West",)
        )
        self.keys = ("name",)
        self.model = "app.division"
