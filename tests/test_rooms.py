import unittest

from peewee import *

from .context import models


class RoomTest(unittest.TestCase):
    """ Tests for the Room Class """

    def setUp(self):
        self.test_facility = models.Facility('Test-Amity')

    def tearDown(self):
        self.test_facility.drop_db()

    def test_should_not_create_invalid_room(self):
        with self.assertRaises(ValueError):
            self.test_facility.create_rooms('bleh bleh', ['one', 'two'])

    def test_print_room_calls_instance_mehtod_print_occupants(self):
        pass

    def test_print_occupants(self):
        pass

    def test_has_vacancy(self):
        pass


class LivingSpaceTest(unittest.TestCase):
    """ Tests for the LivingSpace Class """

    def setUp(self):
        self.test_facility = models.Facility('Test-Amity')

    def tearDown(self):
        self.test_facility.drop_db()

    def test_create_living_space(self):
        self.test_facility.create_rooms('living_space', ['one', 'two'])
        assert self.test_facility.room_count == 2

    def test_add_fellow_to_living_space(self):
        pass

    def test_living_space_is_created_with_correct_capacity(self):
        pass

    def test_should_not_add_person_to_filled_living_space(self):
        pass

    def test_should_not_add_staff_to_living_space(self):
        pass


class OfficeTest(unittest.TestCase):
    """ Tests for the Office Class """

    def setUp(self):
        self.test_facility = models.Facility('Test-Amity')

    def tearDown(self):
        self.test_facility.drop_db()

    def test_create_office(self):
        self.test_facility.create_rooms('office', ['one', 'two'])
        assert self.test_facility.room_count == 2

    def test_add_person_to_office(self):
        pass

    def test_office_is_created_with_correct_capacity(self):
        pass

    def test_should_not_add_person_to_filled_office(self):
        pass

    def test_should_add_fellow_if_they_already_have_a_living_space(self):
        pass
