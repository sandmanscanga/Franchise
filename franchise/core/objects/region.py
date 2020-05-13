from framework.table import Table


class Region(Table):

    def __init__(self):
        self.values = (("North",), ("East",), ("South",), ("West",))
        self.keys = ("name",)
        self.model = "app.region"
