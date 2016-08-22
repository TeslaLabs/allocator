import os
import unittest

from .context import models


class PersonTest(unittest.TestCase):
    """ Tests for the Person Class Functionality"""

    def setUp(self):
        self.test_facility = models.Facility('Test-Amity')

    def tearDown(self):
        self.test_facility.drop_db()

    def test_add_fellow(self):
        self.test_facility.add_fellows(['jesse', 'walter', 'tuco'], 'y')
        assert self.test_facility.people_count == 3

    def test_add_fellow_saves_fellow_list(self):
        fellow_names = ['jesse', 'walter', 'tuco']
        self.test_facility.add_fellows(['jesse', 'walter', 'tuco'], 'y')
        self.assertEqual(type(self.test_facility.people), list)
        self.assertEqual(len(self.test_facility.people), 3)
        self.assertListEqual(fellow_names, self.test_facility.people)

    def test_add_fellow_allocates_room(self):
        self.test_facility.add_fellows(['jesse', 'walter', 'tuco'], 'y')
        allocated_rooms = [room.name for room in self.test_facility.rooms]
        self.assertEqual(len(allocated_rooms), 3)

    def test_adds_fellow_with_correct_accomodation_option(self):
        self.test_facility.add_fellows(['jesse', 'walter', 'tuco'], 'y')
        assert self.test_facility.people_count == 3

    def test_adds_fellow_accomodation_option_if_not_provided(self):
        self.test_facility.add_fellows(['jesse', 'walter', 'tuco'])
        assert self.test_facility.people_count == 3

    def test_adds_fellow_with_no_accomodation_if_provided_option_is_invalid(self):
        self.test_facility.add_fellows(['jesse', 'walter', 'tuco'])
        assert self.test_facility.people_count == 3

    def test_add_staff(self):
        self.test_facility.add_staff(['hank', 'marie', 'wj'])
        assert self.test_facility.people_count == 3

    def test_should_not_add_person_if_they_already_exist(self):
        pass
