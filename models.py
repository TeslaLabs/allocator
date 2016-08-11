from __future__ import print_function

import os
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
                "id"        integer PRIMARY KEY AUTOINCREMENT,
                "name"      text UNIQUE,
                "type"      text,
                "capacity"  integer
            );
            """)
        self.db.query("""
            CREATE TABLE IF NOT EXISTS "people" (
                "id"            integer PRIMARY KEY AUTOINCREMENT,
                "name"          text UNIQUE,
                "type"          text,
                "accomodation"  text
            );
            """)
        self.db.query("""
            CREATE TABLE IF NOT EXISTS "people_rooms" (
                "id"         integer PRIMARY KEY AUTOINCREMENT,
                "person_id"  integer NOT NULL REFERENCES "people" ("id"),
                "room_id"    integer NOT NULL REFERENCES "rooms" ("id")
            );
            """)

    def drop_db(self):
        """
        Deletes the database tables if it exists
        """
        db_name = self.db.db_url.split('///')[1]
        if os.path.exists(db_name):
            os.remove(db_name)

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
            elif room_type == 'office':
                room_instance = Office(room_name)
            room_instance.save(self.db)

    def add_fellows(self, fellows, accomodation):
        """ Add a fellow to a Facility

            Once a fellow is added, they can be allocated a Room
        """
        wants_accomodation = 'Y' if accomodation.lower() == 'y' else 'N'

        for name in fellows:
            fellow_instance = Fellow(name, wants_accomodation)
            fellow_instance.save(self.db)

    def add_staff(self, staff):
        """ Add staff members to a Facility

            Once a staff member is added, they can be allocated a Room
        """
        for name in staff:
            staff_instance = Staff(name)
            staff_instance.save(self.db)

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

    @property
    def rooms(self):
        """Get the number of rooms in a facility"""
        count = self.db.query('select count(*) as room_count from rooms')
        return count.all()[0]['room_count']

    @property
    def people(self):
        """Get the number of people in a facility"""
        count = self.db.query('select count(*) as people_count from people')
        return count.all()[0]['people_count']


class Person(object):
    """ Represents a Person in a Facility

        Attributes:
            name: Name of the Person
    """

    __metaclass__ = ABCMeta

    def __init__(self, name):
        self.name = name
        self.role = None

    def get_role(self):
        """"Returns a string representing the role of the Person.
            i.e. Staff or Fellow
        """
        return self.role

    @abstractmethod
    def save(self, db):
        """Save a Person instance to the database"""
        pass


class Fellow(Person):
    """ Represents a Fellow at a Facility """

    def __init__(self, name, wants_accomodation):
        super().__init__(name)
        self.wants_accomodation = wants_accomodation
        self.role = 'Fellow'

    def save(self, db):
        """Save a Fellow instance to the database"""
        db.query(
            "INSERT INTO people (name, type, accomodation)\
             VALUES(:name, :type, :accomodation)",
            name=self.name, type='F', accomodation=self.wants_accomodation
        )


class Staff(Person):
    """ Represents a Staff Member at a Facility """

    def __init__(self, name):
        super().__init__(name)
        self.role = 'Staff'

    def save(self, db):
        """Save a Staff instance to the database"""
        db.query(
            "INSERT INTO people (name, type, accomodation) \
            VALUES(:name, :type, :accomodation)",
            name=self.name, type='S', accomodation='N'
        )


class Room(object):
    """Represents a Room at a Facility"""

    __metaclass__ = ABCMeta

    def __init__(self, name):
        self.name = name
        self.capacity = None

    def add_person(self, person):
        """Add a person to a room"""
        # Check if the person is an instance of the Person class
        # and if the room has a vacancy, then allocate
        # TODO: Perform SQL Query
        # if isinstance(person, Person) and has_vacancy(self):
        #     self.occupants.append(person)
        pass

    @abstractmethod
    def save(self):
        """Save a Room instance to the database"""
        pass

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

    def save(self, db):
        """Save a LivingSpace instance to the database"""
        db.query(
            "INSERT INTO rooms (name, type, capacity) \
            VALUES(:name, :type, :capacity)",
            name=self.name, type='L', capacity=self.capacity
        )


class Office(Room):
    """Represents an office in a Facility"""

    def __init__(self, name):
        super().__init__(name)
        # Offices have a capacity of 6 people
        self.capacity = 6

    def save(self, db):
        """Save an Office instance to the database"""
        db.query(
            "INSERT INTO rooms (name, type, capacity) \
            VALUES(:name, :type, :capacity)",
            name=self.name, type='O', capacity=self.capacity
        )
