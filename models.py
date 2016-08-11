from __future__ import print_function

from abc import ABCMeta, abstractmethod

import records
from builtins import super


class Facility(object):
    """ Represents a Facility that houses Fellows and Staff e.g. Amity

        This facility is responsible for managing all other instances
        i.e. Rooms and People
    """

    def __init__(self, name):
        self.name = name
        self.db = records.Database('sqlite:///{}.db'.format(self.name))
        self.intialize_db()

    def intialize_db(self):
        """
        Create the database tables if they do not exist
        """
        self.db.query("""
            CREATE TABLE IF NOT EXISTS "rooms" (
                "id"   integer PRIMARY KEY AUTOINCREMENT,
                "name" text UNIQUE,
                "type" text
            );
            """)
        self.db.query("""
            CREATE TABLE IF NOT EXISTS "fellows" (
                "id"           integer PRIMARY KEY AUTOINCREMENT,
                "name"         text,
                "accomodation" integer
            );
            """)
        self.db.query("""
            CREATE TABLE IF NOT EXISTS "staff" (
                "id"   integer PRIMARY KEY AUTOINCREMENT,
                "name" text
            );
            """)
        self.db.query("""
            CREATE TABLE IF NOT EXISTS "fellows_rooms" (
                "id"        integer PRIMARY KEY AUTOINCREMENT,
                "fellow_id" integer NOT NULL REFERENCES "fellows" ("id"),
                "room_id"   integer NOT NULL REFERENCES "rooms" ("id")
            );
            """)
        self.db.query("""
            CREATE TABLE IF NOT EXISTS "staff_rooms" (
                "id"       integer PRIMARY KEY AUTOINCREMENT,
                "staff_id" integer NOT NULL REFERENCES "staff" ("id"),
                "room_id"  integer NOT NULL REFERENCES "rooms" ("id")
            );
            """)

    def create_rooms(self, room_type, rooms):
        """ Creates Rooms in a Facility

            Arguments:
                room_type: Room type of the rooms to be created
                rooms: One or more room instances
        """
        if room_type not in ('living_space', 'office'):
            raise ValueError('Invalid Room Type')

        for room_name in rooms:
            if room_type == 'living_space':
                room_instance = LivingSpace(room_name)
                self.rooms.append(room_instance)
            elif room_type == 'office':
                room_instance = Office(room_name)
                self.rooms.append(room_instance)

    def add_person(self, person):
        """ Add a person to a Facility

            Once a person is added, they can be allocated a Room
        """
        self.people.append(person)

    def reallocate_person(self, person, new_room):
        """ Reallocate the specified person to the specified room_name. """
        pass

    def load_people(self, file_path):
        """ Add people to rooms from the provided file """
        pass

    def print_allocations(self, ):
        """ Print a list of allocations onto the screen """
        pass

    def print_unallocated(self, ):
        """ Print a list of unallocated people to the screen """
        pass

    def print_room(self, room_name):
        """" Print the names of all the people in room_name on the screen """
        pass

    def save_state(self, db_name):
        """ Persist all the data stored in the app to a SQLite database """
        pass

    def load_state(self, db_name):
        """ Load data from a database into the application """
        pass


class Person(object):
    """ Represents a Person in a Facility

        Attributes:
            name: Name of the Person
    """

    def __init__(self, name):
        self.name = name
        self.role = None

    def get_role(self):
        """"Returns a string representing the role of the Person.
            i.e. Staff or Fellow
        """
        return self.role


class Fellow(Person):
    """ Represents a Fellow at a Facility """

    def __init__(self, name, wants_accomodation):
        super().__init__(name)
        self.wants_accomodation = wants_accomodation
        self.role = 'Fellow'


class Staff(Person):
    """ Represents a Staff Member at a Facility """

    def __init__(self, name):
        super().__init__(name)
        self.role = 'Staff'


class Room(object):
    """Represents a Room at a Facility"""

    def __init__(self, name):
        self.name = name
        self.occupants = []
        self.capacity = None

    def add_person(self, person):
        """Add a person to a room"""
        # Check if the person is an instance of the Person class
        # and if the room has a vacancy, then allocate
        if isinstance(person, Person) and has_vacancy(self):
            self.occupants.append(person)

    def print_occupants(self):
        """Print the names of all the people in this room."""
        for num, member in enumerate(self.occupants, start=1):
            print(num, member.name)

    def has_vacancy(self):
        """
        Return True if this Room has an available slot or False otherwise.
        """
        return len(self.occupants) < self.capacity


class LivingSpace(Room):
    """Represents a living space in a Facility."""

    def __init__(self, name):
        super().__init__(name)
        # Living spaces have a capacity of 4 fellows
        self.capacity = 4


class Office(Room):
    """Represents an office in a Facility"""

    def __init__(self, name):
        super().__init__(name)
        # Offices have a capacity of 6 people
        self.capacity = 6
