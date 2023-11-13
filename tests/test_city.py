#!/usr/bin/python3

"""Unittest module for the City Class."""

import unittest
import pep8
import os
from models import City
from models import storage
from models.base_model import BaseModel


class TestCity(unittest.TestCase):

    """Test Cases for the City class."""

    def setUp(self):
        """Sets up test methods."""
        self.city = City()

    def tearDown(self):
        """Tears down test methods."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_instance_creation(self):
        """Test instance creation."""
        self.assertIsInstance(self.city, City)
        self.assertIsInstance(self.city, BaseModel)

    def test_attributes(self):
        """Test attributes of the City class."""
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertTrue(hasattr(self.city, 'name'))

    def test_string_representation(self):
        """Test string representation of City class."""
        self.assertIn('state_id', str(self.city))
        self.assertIn('name', str(self.city))

    def test_save_method(self):
        """Test save method of City class."""
        current_updated_at = self.city.updated_at
        self.city.save()
        new_updated_at = self.city.updated_at
        self.assertNotEqual(current_updated_at, new_updated_at)

    def test_to_dict_method(self):
        """Test to_dict method of City class."""
        city_dict = self.city.to_dict()
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertIsInstance(city_dict['created_at'], str)
        self.assertIsInstance(city_dict['updated_at'], str)
        self.assertIsInstance(city_dict['id'], str)
        self.assertIsInstance(city_dict['state_id'], str)
        self.assertIsInstance(city_dict['name'], str)

    def test_create_object(self):
        """Test created instance."""
        new_city = City()
        self.assertIsInstance(new_city, City)
        self.assertIsNot(new_city, self.city)

    def test_storage_all_method(self):
        """Test storage all method."""
        all_cities = storage.all()
        self.assertIsNotNone(all_cities)
        self.assertIsInstance(all_cities, dict)

    def test_destroy_method(self):
        """Test destroy method."""
        new_city = City()
        new_city.save()
        key = 'City.' + new_city.id
        storage.destroy(new_city)
        all_cities = storage.all()
        self.assertNotIn(key, all_cities)

    def test_all_method(self):
        """Test all method."""
        new_city = City()
        new_city.save()
        all_cities = storage.all(City)
        self.assertIsInstance(all_cities, dict)
        self.assertIn(new_city.id, all_cities)

    def test_update_method(self):
        """Test update method."""
        new_city = City()
        new_city.save()
        key = 'City.' + new_city.id
        current_name = new_city.name
        storage.update(City, new_city.id, {'name': 'New York'})
        updated_city = storage.all()[key]
        self.assertNotEqual(current_name, updated_city.name)
        self.assertEqual(updated_city.name, 'New York')


if __name__ == "__main__":
    unittest.main()
