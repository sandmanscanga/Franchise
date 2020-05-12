from table import Table


class Division(Table):

    def __init__(self):
        self.values = (("AFC",), ("NFC",))
        self.keys = ("name",)
        self.model = "app.division"
