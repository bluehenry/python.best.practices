class ExampleIterator:
    def __init__(self, data):
        self.index = 0
        self.data = data

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration()

        result = self.data[self.index]
        self.index += 1
        return result


class ExampleIterable:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return ExampleIterator(self.data)

i = ExampleIterator([1, 2, 3, 4, 5])
next(i)
next(i)
next(i)

for j in ExampleIterator([1, 2, 3, 4, 5]):
    print(j)


for j in ExampleIterable([1, 2, 3, 4, 5]):
    print(j)

list = [ i*3 for i in ExampleIterable([1, 2, 3, 4, 5])]
print(list)