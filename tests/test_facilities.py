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

    def test_available_rooms(self):
        room = models.Room.create(name='Go', room_type='Living Space')
        self.assertListEqual([room for room in models.Room.select()], self.test_facility.available_rooms())

    def test_create_facility_should_call_initialize_database(self):
        pass

    def test_print_room_calls_instance_method_print_occupants(self):
        pass
