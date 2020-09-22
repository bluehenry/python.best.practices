class Container:
    next_serial = 1

    @classmethod
    def _get_next_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    @classmethod
    def create_empty(cls, owner):
        return cls(owner, contents=None)

    @classmethod
    def create_with_item(cls, owner, items):
        return cls(owner, contents=list(items))

    def __init__(self, owner, contents=None):
        self.owner = owner
        self.contents = contents

        # Container.next_serial is class attributes
        self.serial = Container._get_next_serial()


c1 = Container('Tom')
print(c1.owner)
print(c1.serial)

c2 = Container('Catalina')
print(c2.owner)
print(c2.serial)

c3 = Container.create_empty('A')
print(c3.owner)
print(c3.serial)
print(c3.contents)

c4 = Container.create_with_item('B', ['apple', 'pineapple', 'banana'])
print(c4.owner)
print(c4.serial)
print(c4.contents)
