import unittest

from .context import models


class FacilityTest(unittest.TestCase):
    """ Tests for the Facility Class """

    def setUp(self):
        self.test_facility = models.Facility('Test-Amity')

    def tearDown(self):
        self.test_facility.drop_db()

    def test_create_facility(self):
        self.assertEqual(self.test_facility.name, 'Test-Amity')
        self.assertEqual(
            self.test_facility.db.db_url,
            'sqlite:///{}.db'.format(self.test_facility.name)
        )

    def test_create_living_space(self):
        self.test_facility.create_rooms('living_space', ['one', 'two'])
        self.assertEqual(2, self.test_facility.rooms)

    def test_create_office(self):
        self.test_facility.create_rooms('office', ['one', 'two'])
        self.assertEqual(2, self.test_facility.rooms)

    def test_add_fellow(self):
        self.test_facility.add_fellows(['jesse', 'walter', 'tuco'], 'y')
        self.assertEqual(3, self.test_facility.people)

    def test_add_staff(self):
        self.test_facility.add_staff(['hank', 'marie', 'wj'])
        self.assertEqual(3, self.test_facility.people)
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
