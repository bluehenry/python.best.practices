class Container:
    next_serial = 1

    @staticmethod
    def _get_next_serial():
        result = Container.next_serial
        Container.next_serial += 1
        return result

    def __init__(self, owner):
        self.owner = owner

        # Container.next_serial is class attributes
        self.serial = Container._get_next_serial()


container = Container('Tom')
print(container.owner)
print(container.serial)

container = Container('Catalina')
print(container.owner)
print(container.serial)
