#!/usr/bin/python3
"""Tests for Amenity"""

import unittest
import os
import pep8
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """Tests for Amenity class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the test"""
        cls.amenity = Amenity()

    def test_pep8(self):
        """Test pep8 compliance"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 style issues")

    def test_attributes(self):
        """Test attributes of Amenity class"""
        self.assertTrue('id' in dir(self.amenity))
        self.assertTrue('created_at' in dir(self.amenity))
        self.assertTrue('updated_at' in dir(self.amenity))
        self.assertTrue('name' in dir(self.amenity))

    def test_save_method(self):
        """Test save method of Amenity class"""
        initial_created_at = self.amenity.created_at
        self.amenity.save()
        updated_created_at = self.amenity.created_at
        self.assertNotEqual(initial_created_at, updated_created_at)

if __name__ == '__main__':
    unittest.main()
