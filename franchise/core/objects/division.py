
class Division:

    def __init__(self):
        super().__init__()
        self.values = (
            ("AFC North",),
            ("AFC East",),
            ("AFC South",),
            ("AFC West",),
            ("NFC North",),
            ("NFC East",),
            ("NFC South",),
            ("NFC West",),
        )
        self.keys = ("name",)
        self.model = "app.division"
