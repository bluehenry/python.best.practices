class AlternateIterable:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        return self.data[index]

[i for i in AlternateIterable([1, 2, 3, 4, 5])]