from framework.table import Table


class Season(Table):

    def __init__(self):
        self.values = ((2019,), (2020,))
        self.keys = ("name",)
        self.model = "app.season"
