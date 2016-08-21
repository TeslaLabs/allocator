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

    def test_create_facility_should_call_initialize_database(self):
        pass
