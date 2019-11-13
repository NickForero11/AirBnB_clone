#!/usr/bin/python3
"""Module with unit tests for the BaseModel class
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Tests for every method and attribute of the BaseModel class.
    """
    def setUp(self):
        self.fake_instance = BaseModel()
        self.comparator_instance = BaseModel()

    def tearDown(self):
        del self.fake_instance
        del self.comparator_instance

    def test_uuid(self):
        self.assertTrue(hasattr(self.fake_instance, "id"))
        self.assertEqual(type(self.fake_instance.id), str)
        self.assertNotEqual(self.fake_instance.id, self.comparator_instance.id)

    def test_instance(self):
        self.assertTrue(isinstance(self.fake_instance, BaseModel))

    def test_type(self):
        self.assertEqual(type(self.fake_instance), BaseModel)

    def test_created_at(self):
        self.assertTrue(hasattr(self.fake_instance, "created_at"))
        self.assertTrue(isinstance(self.fake_instance.created_at, datetime))

    def test_updated_at(self):
        self.assertTrue(hasattr(self.fake_instance, "updated_at"))
        self.assertTrue(isinstance(self.fake_instance.updated_at, datetime))

    def test_str(self):
        correct_output = '[{:s}] ({:s}) {}'.format(
            self.fake_instance.__class__.__name__, self.fake_instance.id,
            self.fake_instance.__dict__)
        self.assertEqual(str(self.fake_instance), correct_output)

    def test_save(self):
        old_date = self.fake_instance.updated_at
        self.fake_instance.save()
        self.assertTrue(old_date != self.fake_instance.updated_at)

    def test_to_dict(self):
        comparator = {
            key: value.isoformat() if isinstance(value, datetime) else value
            for key, value in self.fake_instance.__dict__.items()
        }
        output = self.fake_instance.to_dict()
        self.assertTrue(comparator.items() < output.items())
        self.assertTrue('__class__' in output)

if __name__ == '__main__':
    unittest.main()
