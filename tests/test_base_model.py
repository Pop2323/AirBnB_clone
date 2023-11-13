#!/usr/bin/python3
"""Test for BaseModel"""
import unittest
import os
from models.base_model import BaseModel
import pep8


class TestBaseModel(unittest.TestCase):
    """Test BaseModel"""

    def setUp(self):
        self.test_base_model = BaseModel()

    def test_pep8_compliance(self):
        """Test for pep8 compliance."""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 style issues found")

    def test_save_method(self):
        """Test save method of BaseModel"""
        self.test_base_model.save()
        self.assertNotEqual(self.test_base_model.created_at,
                            self.test_base_model.updated_at)

    def test_docstring(self):
        """Test presence of docstring"""
        self.assertIsNotNone(BaseModel.__doc__)

    def test_kwargs_constructor(self):
        """Test BaseModel constructor with kwargs"""
        base_model = BaseModel(name="base")
        self.assertEqual(type(base_model).__name__, "BaseModel")
        self.assertFalse(hasattr(base_model, "id"))
        self.assertFalse(hasattr(base_model, "created_at"))
        self.assertTrue(hasattr(base_model, "name"))
        self.assertFalse(hasattr(base_model, "updated_at"))
        self.assertTrue(hasattr(base_model, "__class__"))


if __name__ == "__main__":
    unittest.main()
