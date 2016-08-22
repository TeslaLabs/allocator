import unittest

from faker import Factory

from .context import models


fake = Factory.create()


class RoomTest(unittest.TestCase):
    """ Tests for the Room Class """

    def setUp(self):
        self.test_facility = models.Facility('Test-Amity')

    def tearDown(self):
        self.test_facility.drop_db()

    def test_create_office(self):
        self.test_facility.create_rooms('office', ['one', 'two'])
        assert self.test_facility.room_count == 2

    def test_create_living_space(self):
        self.test_facility.create_rooms('living_space', ['one', 'two'])
        assert self.test_facility.room_count == 2

    def test_should_not_create_duplicate_office(self):
        self.test_facility.create_rooms('office', ['one'])
        self.test_facility.create_rooms('office', ['one'])
        self.assertEqual(self.test_facility.room_count, 1)

    def test_should_not_create_duplicate_living_space(self):
        self.test_facility.create_rooms('living_space', ['one'])
        self.test_facility.create_rooms('living_space', ['one'])
        self.assertEqual(self.test_facility.room_count, 1)

    def test_should_not_create_invalid_room(self):
        with self.assertRaises(ValueError):
            self.test_facility.create_rooms('bleh bleh', ['one', 'two'])

    def test_add_occupants_to_room(self):
        room = models.Room.create(name='Go', room_type='Living Space')
        fellow = models.Person.create(
            name=fake.name(), accomodation='N', role='Fellow')
        staff = models.Person.create(
            name=fake.name(), accomodation='N', role='Fellow')
        room.add_occupants(fellow, staff)
        # The added people should be in the occupants list
        self.assertIn(fellow.name, room.occupants)
        self.assertIn(staff.name, room.occupants)

    def test_should_not_add_occupants_if_room_is_full(self):
        room = models.Room.create(
            name=fake.color_name(), room_type='Living Space')
        count = 0
        while count < room.capacity:
            person = models.Person.create(
                name=fake.name(),
                accomodation='N',
                role='Fellow'
            )
            count += 1
            room.add_occupants(person)
        extra_person = models.Person.create(
            name=fake.name(),
            accomodation='N',
            role='Fellow'
        )
        with self.assertRaises(Exception):
            room.add_occupants(extra_person)

    def test_print_occupants(self):
        names = [fake.name_male(), fake.name_female()]
        room = models.Room.create(name='Go', room_type='Office')
        fellow = models.Person.create(
            name=names[0], accomodation='N', role='Fellow')
        staff = models.Person.create(
            name=names[1], accomodation='N', role='Staff')
        room.add_occupants(fellow, staff)

        return_string = ''
        for num, name in enumerate(names, start=1):
            return_string += '{}. {}\n'.format(num, name)
        self.assertEqual(room.print_occupants(), return_string)

    def test_print_occupants_returns_None_for_empty_room(self):
        room = models.Room.create(name='Go', room_type='Living Space')
        self.assertIsNone(room.print_occupants())

    def test_has_vacancy(self):
        pass


class LivingSpaceTest(unittest.TestCase):
    """ Tests for the LivingSpace Class """

    def setUp(self):
        self.test_facility = models.Facility('Test-Amity')

    def tearDown(self):
        self.test_facility.drop_db()

    def test_create_living_space_creates_correct_room_type(self):
        self.test_facility.create_rooms('living_space', ['one', 'two'])
        created_rooms = [room.room_type for room in models.Room.select()]
        self.assertListEqual(['Living Space', 'Living Space'], created_rooms)

    def test_creates_living_space_with_correct_capacity(self):
        self.test_facility.create_rooms('living_space', ['one'])
        for room in models.Room.select():
            assert room.capacity == 4

    def test_should_not_add_staff_to_living_space(self):
        room = models.Room.create(name='Go', room_type='Living Space')
        staff = models.Person.create(
            name=fake.name(), accomodation='N', role='Staff')
        with self.assertRaises(Exception):
            room.add_occupants(staff)


class OfficeTest(unittest.TestCase):
    """ Tests for the Office Class """

    def setUp(self):
        self.test_facility = models.Facility('Test-Amity')

    def tearDown(self):
        self.test_facility.drop_db()

    def test_creates_office_with_correct_capacity(self):
        self.test_facility.create_rooms('office', ['one', 'two'])
        for room in models.Room.select():
            assert room.capacity == 6

    def test_create_office_creates_correct_room_type(self):
        self.test_facility.create_rooms('office', ['one', 'two'])
        created_rooms = [room.room_type for room in models.Room.select()]
        self.assertListEqual(['Office', 'Office'], created_rooms)

    def test_office_is_created_with_correct_capacity(self):
        pass

    def test_should_not_add_person_to_filled_office(self):
        pass

    def test_should_add_fellow_if_they_already_have_a_living_space(self):
        pass
