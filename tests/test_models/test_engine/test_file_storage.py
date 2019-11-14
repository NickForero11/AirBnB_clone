#!/usr/bin/python3
"""
This module contains the tests for FileStorage class
"""
import unittest
import models
from os.path import isfile as exist_file
from os import remove
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Tests for every method and attribute of the FileStorage class.
    Specifically the serialization/deserialization methods.
    """
    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        del self.storage
        if exist_file('file.json'):
            remove('file.json')

    def test_private_class_attributes(self):
        self.assertFalse(hasattr(self.storage, '__file_path'))
        self.assertFalse(hasattr(self.storage, '__objects'))

    def test_default_file_path(self):
        self.assertTrue(self.storage._FileStorage__file_path == "file.json")

    def test_objects(self):
        self.assertTrue(isinstance(self.storage._FileStorage__objects, dict))

    def test_all(self):
        response = self.storage.all()
        self.assertTrue(isinstance(response, dict))

    def test_new(self):
        fake_data = BaseModel()
        key = '{}.{}'.format(fake_data.__class__.__name__, fake_data.id)
        response = self.storage.all()
        self.assertTrue(key in response)
        self.assertTrue(response[key] is fake_data)

    def test_save(self):
        fake_data = BaseModel()
        key = '{}.{}'.format(fake_data.__class__.__name__, fake_data.id)
        instance_onmemory = self.storage.all()
        fake_data.save()
        exist_file(self.storage._FileStorage__file_path)

    def test_reload(self):
        fake_data = BaseModel()
        key = '{}.{}'.format(fake_data.__class__.__name__, fake_data.id)
        instance_onmemory = self.storage.all()
        fake_data.save()
        self.storage.reload()
        instance_fromJSON = self.storage.all()
        self.assertTrue(key in instance_fromJSON)
        self.assertTrue(instance_fromJSON == instance_onmemory)


if __name__ == '__main__':
    unittest.main()
