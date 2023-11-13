#!/usr/bin/python3
"""Unittest Place"""

import unittest
import pep8
from models import place
from models.base_model import BaseModel

class TestPlace(unittest.TestCase):
    """ Tests Place """

    @classmethod
    def setUpClass(cls):
        """ Set up for the test """
        cls.place = place.Place()

    @classmethod
    def tearDownClass(cls):
        """ Clean up after the test """
        del cls.place

    def test_pep8(self):
        """ Tests pep8 """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/place.py"])
        self.assertEqual(result.total_errors, 0, "Check pep8")

    def test_Place_dict(self):
        """ Place_dict """
        attributes = ["id", "created_at", "updated_at", "city_id", "user_id", "name", "__class__"]
        for attr in attributes:
            self.assertTrue(hasattr(self.place, attr))

    def test_save_Place(self):
        """ Save_Place """
        self.place.save()
        self.assertNotEqual(self.place.created_at, self.place.updated_at)

if __name__ == '__main__':
    unittest.main()
