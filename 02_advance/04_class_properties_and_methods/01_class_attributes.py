class Container:
    next_serial = 1;

    def __init__(self, owner):
        self.owner = owner

        # Container.next_serial is class attributes
        self.serial = Container.next_serial
        Container.next_serial += 1


container = Container('Tom')
print(container.owner)
print(container.serial)

container = Container('Catalina')
print(container.owner)
print(container.serial)