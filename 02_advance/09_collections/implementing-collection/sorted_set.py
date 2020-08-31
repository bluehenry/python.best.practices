# for index
from collections.abc import Sequence
from bisect import bisect_left
from itertools import chain

class SortedSet(Sequence):
    def __init__(self, items=None):
        self._items = sorted(set(items)) if items is not None else []

    def __contains__(self, item):
        # index = bisect_left(self._items, item)
        # return (index != len(self._items)) and (self._items[index] == item)
        try:
            self.index(item)
            return True
        except ValueError:
            return False

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        result = self._items[index]
        return SortedSet(result) if isinstance(index, slice) else result

    def __repr__(self):
        return "SortedSet({})".format(
            repr(self._items) if self._items else ''
        )

    def __eq__(self, rhs):
        # It's important to return NotImplemented rather than raise NotImplementedError
        if not isinstance(rhs, SortedSet):
            return NotImplemented
        return self._items == rhs._items

    def __ne__(self, rhs):
        # It's important to return NotImplemented rather than raise NotImplementedError
        if not isinstance(rhs, SortedSet):
            return NotImplemented
        return self._items != rhs._items

    def index(self, item):
        index = bisect_left(self._items, item)
        if (index != len(self._items)) and (self._items[index] == item):
            return index
        raise ValueError(f'{repr(item)} not found')

    def count(self, item):
        return int(item in self)

    def __add__(self, rhs):
        return SortedSet(chain(self._items, rhs._items))

    def __mul__(self, rhs):
        return self if rhs > 0 else SortedSet()

    def __rmul__(self, lhs):
        return self * lhs

    def issubset(self, iterable):
        return self <= SortedSet(iterable)

    def issuperset(self, iterable):
        return self >= SortedSet(iterable)

    def intersection(self, iterable):
        return self & SortedSet(iterable)

    def union(self, iterable):
        return self | SortedSet(iterable)

    def symetric_difference(self, iterable):
        return self ^ SortedSet(iterable)

    def difference(self, iterable):
        return self - SortedSet(iterable)