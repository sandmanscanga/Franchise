from table import Table


class Category(Table):

    def __init__(self):
        self.values = (
            ("Passing", "passingYards"),
            ("Rushing", "rushingYards"),
            ("Receiving", "receivingYards"),
            ("Defense", "totalTackles"),
            ("Scoring", "totalPoints"),
            ("Returning", "kickReturnYards"),
            ("Kicking", "fieldGoalsMade"),
            ("Punting", "puntYards"),
        )
        self.keys = ("name", "sortkey")
        self.model = "app.category"
