import unittest
import pytest

from peewee import *

from .context import models


class RoomTest(unittest.TestCase):
    """ Tests for the Room Class """

    def setUp(self):
        self.test_facility = models.Facility('Test-Amity')

    def tearDown(self):
        self.test_facility.drop_db()

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

    def test_add_person_to_office(self):
        pass

    def test_office_is_created_with_correct_capacity(self):
        pass

    def test_should_not_add_person_to_filled_office(self):
        pass

    def test_should_add_fellow_if_they_already_have_a_living_space(self):
        pass
