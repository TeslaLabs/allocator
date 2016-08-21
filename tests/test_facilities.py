import unittest
import pytest

from .context import models


class FacilityTest(unittest.TestCase):
    """ Tests for the Facility Class """

    def setUp(self):
        self.test_facility = models.Facility('Test-Amity')

    def tearDown(self):
        self.test_facility.drop_db()

    def test_create_facility(self):
        assert self.test_facility.name == 'Test-Amity'

    def test_should_not_create_invalid_room(self):
        with pytest.raises(ValueError):
            self.test_facility.create_rooms('bleh bleh', ['one', 'two'])


class FacilityRoomsTest(unittest.TestCase):
    """ Tests for the Facility Rooms Functionality """

    def setUp(self):
        self.test_facility = models.Facility('Test-Amity')

    def tearDown(self):
        self.test_facility.drop_db()

    def test_create_living_space(self):
        self.test_facility.create_rooms('living_space', ['one', 'two'])
        assert self.test_facility.rooms == 2

    def test_create_office(self):
        self.test_facility.create_rooms('office', ['one', 'two'])
        assert self.test_facility.rooms == 2

    def test_print_room(self):
        pass

    def test_load_people(self):
        pass

    def test_load_people_allocates_people_to_rooms(self):
        pass

    def test_print_allocations(self):
        pass

    def test_print_unallocated(self):
        pass

    def test_reallocate_person(self):
        pass
