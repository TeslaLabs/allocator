import unittest

from .context import models


class FellowTest(unittest.TestCase):
    """ Tests for the Fellow Related Functionality"""

    def setUp(self):
        self.test_facility = models.Facility('Test-Amity')

    def tearDown(self):
        self.test_facility.drop_db()

    def test_add_fellow(self):
        # A room needs to exist first before adding fellows
        self.test_facility.create_rooms('office', ['owfewfwefwefne'])
        self.test_facility.add_fellows(['jesse', 'walter', 'tuco'], 'y')
        assert self.test_facility.people_count == 3

    def test_does_not_create_duplicate_fellow(self):
        self.test_facility.create_rooms('office', ['owfewfwefwefne'])
        self.test_facility.add_fellows(['jesse'], 'y')
        self.test_facility.add_fellows(['jesse'], 'y')
        # The Duplicate fellow should not be created
        self.assertEqual(len(self.test_facility.people), 1)

    def test_add_fellow_raises_error_if_rooms_dont_exist(self):
        with self.assertRaises(IndexError):
            self.test_facility.add_fellows(['jesse', 'walter', 'tuco'], 'y')

    def test_add_fellow_saves_fellow_list(self):
        fellow_names = ['jesse', 'walter', 'tuco']
        self.test_facility.create_rooms('office', ['owfewfwefwefne'])
        self.test_facility.add_fellows(['jesse', 'walter', 'tuco'], 'y')
        self.assertEqual(type(self.test_facility.people), list)
        self.assertEqual(len(self.test_facility.people), 3)
        self.assertListEqual(fellow_names, self.test_facility.people)

    def test_add_fellow_allocates_room(self):
        names = ['jesse', 'walter', 'tuco']
        self.test_facility.create_rooms('office', ['owfewfwefwefne'])
        self.test_facility.add_fellows(names, 'y')
        self.assertEqual(len(self.test_facility.available_rooms()), 1)
        room = self.test_facility.available_rooms()[0]
        self.assertListEqual(room.occupants, names)

    def test_adds_fellow_with_correct_accomodation_option(self):
        self.test_facility.create_rooms('office', ['one'])
        self.test_facility.add_fellows(['jesse', 'walter', 'tuco'], 'y')
        for fellow in models.Person.select():
            self.assertEqual(fellow.accomodation, 'Y')

    def test_adds_no_as_fellow_accomodation_option_if_not_provided(self):
        self.test_facility.create_rooms('office', ['one'])
        self.test_facility.add_fellows(['jesse', 'walter', 'tuco'])
        self.assertEqual(self.test_facility.people_count, 3)
        for fellow in models.Person.select():
            self.assertEqual(fellow.accomodation, 'N')

    def test_adds_fellow_with_no_as_accomodation_if_option_is_invalid(self):
        self.test_facility.create_rooms('office', ['one'])
        self.test_facility.add_fellows(['jesse', 'walter', 'tuco'], 'invalid')
        self.assertEqual(self.test_facility.people_count, 3)
        for fellow in models.Person.select():
            self.assertEqual(fellow.accomodation, 'N')

    # def test_add_staff(self):
    #     self.test_facility.add_staff(['hank', 'marie', 'wj'])
    #     assert self.test_facility.people_count == 3
    #
    # def test_should_not_add_person_if_they_already_exist(self):
    #     pass
