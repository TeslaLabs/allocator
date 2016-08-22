from __future__ import print_function

import os

from builtins import super
from peewee import *
from playhouse.fields import ManyToManyField


DB_NAME = os.environ.get('DB_NAME', 'Amity.db')
db = SqliteDatabase(DB_NAME)


class BaseModel(Model):
    class Meta:
        database = db


class Facility(BaseModel):
    """ Represents a Facility that houses Fellows and Staff e.g. Amity

        This facility is responsible for managing all other instances
        i.e. Rooms and People
    """

    def __init__(self, name):
        self.name = name
        self.initialize_db()

    def initialize_db(self):
        # Connect to the database
        db.connect()
        # Create the necessary DB tables
        try:
            db.create_tables([Room, Person, Room.people.get_through_model()])
        except OperationalError:
            # table already exists
            pass

    def drop_db(self):
        """
        Deletes the database tables if it exists
        """
        if os.path.exists(DB_NAME):
            os.remove(DB_NAME)

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
                try:
                    Room.create(name=room_name, room_type='Living Space')
                except IntegrityError:
                    # The room already exists
                    pass
            elif room_type == 'office':
                try:
                    Room.create(name=room_name, room_type='Office')
                except IntegrityError:
                    # The room already exists
                    pass

    # TODO: Allocate room after adding a fellow
    def add_fellows(self, fellows, accomodation='N'):
        """ Add a fellow to a Facility

            Once a fellow is added, they can be allocated a Room
        """
        wants_accomodation = 'Y' if accomodation[0].lower() == 'y' else 'N'

        for name in fellows:
            try:
                Person.create(
                    name=name,
                    accomodation=wants_accomodation,
                    role='Fellow')
            except IntegrityError:
                # The person already exists
                pass

    # TODO: Allocate room after adding a staff member
    def add_staff(self, staff):
        """ Add staff members to a Facility

            Once a staff member is added, they can be allocated a Room
        """
        for name in staff:
            try:
                Person.create(name=name, accomodation='N', role='Staff')
            except IntegrityError:
                # The person already exists
                pass

    def reallocate_person(self, person, new_room):
        """ Reallocate the specified person to the specified room_name. """
        pass

    # def load_people(self, file_path):
    #     """ Add people to rooms from the provided file """
    #     fellows = []
    #     staff = []
    #
    #     with open(file_path, 'r') as people_file:
    #         # self.db.query('PRAGMA busy_timeout = 30000')
    #         for line in people_file:
    #             if 'FELLOW' in line:
    #                 fellow_data = [chunk.strip()
    #                                for chunk in line.split('FELLOW')]
    #                 # Temporarily save fellow data in a list
    #                 fellows.append((fellow_data[0], fellow_data[1]))
    #             elif 'STAFF' in line:
    #                 staff_data = [chunk.strip()
    #                               for chunk in line.split('STAFF')]
    #                 # Temporarily save all instances in a list
    #                 staff.append(staff_data[0])
    #             else:
    #                 raise ValueError('Invalid Input File!')
    #
    #     # Persist the people data to the DB
    #     for (name, accomodation) in fellows:
    #         fellow_instance = Fellow(name, accomodation)
    #         try:
    #             fellow_instance.save(self.db)
    #         # Duplicate item error
    #         except IntegrityError:
    #             # The fellow already exists in the DB
    #             pass
    #     for member in staff:
    #         staff_instance = Staff(member)
    #         try:
    #             staff_instance.save(self.db)
    #         except IntegrityError:
    #             pass
    #
    #     # Get available rooms
    #     print('FELLOWS:', fellows)
    #     print('STAFF:', staff)
    #     rooms = self.available_rooms()
    #     # TODO: Get newly-created people instances
    #     # TODO: Assign these people to rooms
    #     print('ROOMS:', rooms)

    def print_allocations(self):
        """ Print a list of allocations onto the screen """
        pass

    def print_unallocated(self):
        """ Print a list of unallocated people to the screen """
        pass

    def print_room(self, room_name):
        """" Print the names of all the people in room_name on the screen """
        pass

    @property
    def room_count(self):
        """Get the number of rooms in a facility"""
        return Room.select().count()

    @property
    def rooms(self):
        """Get the names of rooms in a facility"""
        return [room.name for room in Room.select()]

    @property
    def people_count(self):
        """Get the number of people in a facility"""
        return Person.select().count()

    @property
    def people(self):
        """Return the names of people in a facility"""
        return [person.name for person in Person.select()]

    def available_rooms(self):
        """Return a list of the available rooms in a facility"""
        return [room for room in Room.select() if room.has_vacancy()]


class Person(BaseModel):
    """ Represents a Person in a Facility

        Attributes:
            name: Name of the Person
    """

    accomodation = TextField()
    name = TextField(unique=True)
    role = TextField()

    class Meta:
        db_table = 'people'


class Room(BaseModel):
    """Represents a Room at a Facility"""

    name = CharField(unique=True)
    room_type = CharField()
    people = ManyToManyField(Person)

    @property
    def capacity(self):
        if self.room_type == 'Office':
            return 6
        elif self.room_type == 'Living Space':
            return 4

    @property
    def occupants(self):
        """Return the names of occupants in a room"""
        return [person.name for person in self.people]

    def print_occupants(self):
        """Print the names of all the people in this room."""
        if len(self.occupants) == 0:
            print('Room has no occupants')
        for num, member in enumerate(self.occupants, start=1):
            print('{}. {}'.format(num, member))

    def add_occupants(self, *occupants):
        """Add an occupant to a room"""
        if not self.has_vacancy():
            # If the room has no vacancy, raise an error
            raise Exception('Room is fully occupied')
        for occupant in occupants:
            if self.room_type == 'Living Space' and occupant.role == 'Staff':
                raise Exception('Cannot add a Staff Member to a Living Space')
            self.people.add(occupant)

    def has_vacancy(self):
        """
        Return True if this Room has an available slot or False otherwise.
        """
        return len(self.occupants) < self.capacity

    class Meta:
        db_table = 'rooms'
