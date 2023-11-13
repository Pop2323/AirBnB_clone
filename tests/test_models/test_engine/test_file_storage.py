#!/usr/bin/python3
"""Test File Storage"""

import unittest
import pep8
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

class TestFileStorage(unittest.TestCase):
    """Test File Storage"""
    def test_pep8_testFileCase(self):
        style = pep8.StyleGuide(quiet=True)
        test = style.check_FileStorage(['models/engine/file_storage.py'])
        self.assertEqual(test.total_errors, 0, "Check pep8")

if __name__ == "__main__":
    unittest.main