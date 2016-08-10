import unittest

from .context import models


class FacilityTest(unittest.TestCase):
    """ Tests for the Facility Class """

    def setUp(self):
        self.test_facility = models.Facility('Test-Amity')
        pass

    def tearDown(self):
        pass

    def test_create_facility(self):
        self.assertEqual('Test-Amity', self.test_facility.name)
        self.assertEqual(0, len(self.test_facility.people))
        self.assertEqual(0, len(self.test_facility.rooms))
        pass

    def test_create_living_space(self):
        self.test_facility.create_rooms('living_space', ['one', 'two'])
        self.assertEqual(2, len(self.test_facility.rooms))

    def test_create_office(self):
        self.test_facility.create_rooms('office', ['one', 'two'])
        self.assertEqual(2, len(self.test_facility.rooms))

    def test_add_person(self):
        pass

    def test_reallocate_person(self):
        pass

    def test_load_people(self):
        pass

    def test_print_allocations(self):
        pass

    def test_print_unallocated(self):
        pass

    def test_print_room(self):
        pass

    def test_save_state(self):
        pass

    def test_load_state(self):
        pass


if __name__ == '__main__':
    unittest.main()
