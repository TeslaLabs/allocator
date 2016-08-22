import unittest

from .context import models


class FacilityRoomsTest(unittest.TestCase):
    """ Tests for the Facility Rooms Functionality """

    def setUp(self):
        self.test_facility = models.Facility('Test-Amity')

    def tearDown(self):
        self.test_facility.drop_db()

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
