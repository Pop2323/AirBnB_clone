#!/usr/bin/python3
""" unit test for class State """

import os
import pep8
import unittest
from models.state import State


class TestStateDocs(unittest.TestCase):
    """ Test docstring in the class """

    def test_doc_class(self):
        """ Test document class """
        doc = State.__doc__
        self.assertIsNotNone(doc)

    def test_doc_methods_class(self):
        """ Test document methods Class """
        l_method = ["save", "__init__", "__str__", "to_dict"]
        for key in State.__dict__.keys():
            if key in l_method:
                doc = getattr(State, key).__doc__
                self.assertIsNotNone(doc)


class TestState(unittest.TestCase):
    """ Test creation objects and use methods """
    @classmethod
    def setUpClass(cls):
        """ new_state set up """
        cls.new_state = State()
        cls.new_state.name = "Tunis"
        cls.new_state.save()

    def test_create_object(self):
        """ Test created instance """
        self.assertIsInstance(self.new_state, State)

    # Other test methods...

    @classmethod
    def tearDownClass(cls):
        """ Test new state Down """
        del cls.new_state
        try:
            os.remove("objects.json")
        except FileNotFoundError:
            pass


if __name__ == '__main__':
    unittest.main()
