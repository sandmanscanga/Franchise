
class Table(object):
    
    values = None
    keys = None
    model = None
    key = None

    def __len__(self):
        return len(self.values)

    def __iter__(self):
        for i, values in enumerate(self.values):
            fields = dict(zip(self.keys, values))
            yield {
                "model": self.model,
                "pk": i+1,
                "fields": fields
            }
    
    def __getitem__(self, index):
        for i, values in enumerate(self.values):
            if index == i:
                return values

    def find(self, value, key=None):
        if key is None:
            if self.key is None:
                col_key = 0
            else:
                col_key = self.keys.index(self.key)
        else:
            col_key = self.keys.index(key)
        for i, values in enumerate(self.values):
            if values[col_key] == value:
                return i + 1
