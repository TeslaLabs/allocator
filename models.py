from __future__ import print_function

import os

from builtins import super
from dotenv import load_dotenv
from sqlalchemy.exc import IntegrityError
from peewee import *


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

        # Connect to the database
        db.connect()
        # Create the necessary DB tables
        try:
            db.create_tables([Room, Person])
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
                    Room.create(name=room_name, room_type='L', capacity=4)
                except IntegrityError:
                    # The room already exists
                    pass
            elif room_type == 'office':
                try:
                    Room.create(name=room_name, room_type='O', capacity=6)
                except IntegrityError:
                    # The room already exists
                    pass

    def add_fellows(self, fellows, accomodation):
        """ Add a fellow to a Facility

            Once a fellow is added, they can be allocated a Room
        """
        wants_accomodation = 'Y' if accomodation.lower() == 'y' else 'N'

        for name in fellows:
            try:
                Person.create(
                    name=name,
                    accomodation=wants_accomodation,
                    role='Fellow')
            except IntegrityError:
                # The person already exists
                pass

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
    def rooms(self):
        """Get the number of rooms in a facility"""
        return Room.select().count()

    @property
    def people(self):
        """Get the number of people in a facility"""
        return Person.select().count()

    # def available_rooms(self):
    #     """Get the number of available rooms in a facility"""
    #     rooms = []
    #
    #     all_rooms = self.db.query('select * from rooms', fetchall=True)
    #     for room in all_rooms.all():
    #         room_count = self.db.query('select count(id) as room_count \
    #             from people_rooms where room_id={}'.format(
    #             room['id']), fetchall=True).all()[0]['room_count']
    #
    #         rooms.append({
    #             'name': room['name'],
    #             'type': room['type'],
    #             'capacity': room['capacity'],
    #             'available_space': room['capacity'] - room_count
    #         })
    #
    #     return rooms


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
    capacity = IntegerField()

    def print_occupants(self):
        """Print the names of all the people in this room."""
        # for num, member in enumerate(self.occupants, start=1):
        #     print(num, member.name)
        pass

    def has_vacancy(self):
        """
        Return True if this Room has an available slot or False otherwise.
        """
        # return len(self.occupants) < self.capacity
        pass

    class Meta:
        db_table = 'rooms'


class PeopleRooms(BaseModel):
    person = ForeignKeyField(db_column='person_id', rel_model=Person)
    room = ForeignKeyField(db_column='room_id', rel_model=Room)

    class Meta:
        db_table = 'people_rooms'
