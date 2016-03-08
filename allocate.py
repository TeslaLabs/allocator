class RoomAllocator(object):
    pass


class Person(object):
    def __init__(self, name):
        self.name = name


class Fellow(Person):
    def __init__(self, name, living_space_choice):
        super().__init__(name)
        self.living_space_choice = living_space_choice


class Staff(Person):
    def __init__(self, name):
        super().__init__(name)


class Room(object):
    def __init__(self, name):
        self.name = name
        self.occupants = []
        self.capacity = None

    def add_person(self, person):
        # Check if the person is an instance of the Person class
        # and if the room is already full, then allocate
        if isinstance(person, Person) and len(self.occupants) < self.capacity:
            self.occupants.append(person)


class LivingSpace(Room):
    def __init__(self, name):
        super().__init__(name)
        # All living spaces have a capacity of 4 fellows
        self.capacity = 4


class Office(Room):
    def __init__(self, name):
        super().__init__(name)
        # All offices have a capacity of 6 people
        self.capacity = 6
