from pprint import pprint as pp


class SimpleList:

    def __init__(self, items):
        self._items = list(items)

    def add(self, item):
        self._items.append(item)

    def __getitem__(self, index):
        return self._items[index]

    def sort(self):
        self._items.sort()
        pp('SimpleList.add()')

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return f'Simplelist: {self._items}'


class SortedList(SimpleList):
    def __init__(self, items=()):
        super().__init__(items)
        self.sort()

    def add(self, item):
        super().add(item)
        self.sort()
        pp('SortedList.add()')

    def __repr__(self):
        return f'SortedList{list(self)}'


class IntList(SimpleList):
    def __init__(self, items=()):
        for x in items: self._validate(x)
        super().__init__(items)

    @staticmethod
    def _validate(x):
        if not isinstance(x, int):
            raise TypeError('IntList only supports integer values.')

    def add(self, item):
        self._validate(item)
        super().add(item)
        pp('IntList.add()')

    def __repr__(self):
        return f'IntList{list(self)}'


class SortedIntList(IntList, SortedList):
    def __repr__(self):
        return f'SortedIntList{list(self)}'


# pp(issubclass(SortedList, SimpleList))

l = SortedIntList([2, 3, 1])
l.add(4)
pp(l.__repr__())
# pp(SortedIntList.__bases__)
# pp(SortedIntList.__mro__)
# pp(SortedIntList.mro())
# pp(super(SortedList, SortedIntList))
# pp(super(SortedList, SortedIntList).add)
# pp(super(SortedIntList, SortedIntList)._validate(5))
# # print(super(SortedIntList, SortedIntList)._validate('abc'))
#
# pp(super(SortedList, l))
# super(SortedList, l).add(6)
# pp(l.__repr__())
