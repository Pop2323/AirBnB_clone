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
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test File Storage"""

    def test_pep8_compliance(self):
        """Test for pep8 compliance."""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 style issues found")

    def test_instance_creation(self):
        """Test FileStorage instance creation"""
        storage = FileStorage()
        self.assertIsInstance(storage, FileStorage, "FileStorage failed")


if __name__ == "__main__":
    unittest.main()
