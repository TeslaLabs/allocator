class RoomAllocator(object):
    pass


class Person(object):
    def __init__(self, name):
        self.name = name


class Fellow(Person):
    can_have_living_space = True

    def __init__(self, name, chooses_living_space):
        super().__init__(name)
        self.chooses_living_space = chooses_living_space


class Staff(Person):
    can_have_living_space = False

    def __init__(self, name):
        super().__init__(name)


class Room(object):
    def __init__(self, name):
        self.name = name


class LivingSpace(Room):
    # All living spaces have a capacity of 4 people
    capacity = 4

    def __init__(self, name):
        super().__init__(name)


class Office(Room):
    # All offices have a capacity of 6 people
    capacity = 6

    def __init__(self, name):
        super().__init__(name)
