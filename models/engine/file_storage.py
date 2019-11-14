"""Module that handles the storing and loading of data in JSON files,
more specifically instances of BaseModel Objects.
"""
from json import load as read_data, dump as save_data
from os.path import isfile as file_exist
from models.base_model import BaseModel


class FileStorage:
    """Class that defines an interface to serialize and deserialize instances
    of BaseModel data classes.

    Attributes:
        __file_path (str): The path of the file that will be used to store the
        data.

        _objects (dict): The dictionary that stores the data instances.

    """
    __file_path = "file.json"
    __objects = dict()

    def all(self):
        """Retrieves all the data objects stored in runtime memory.

        Returns:
            Dict: All the instances stored in memory from the __objects
                  attribute"""
        return self.__objects

    def new(self, obj):
        """Adds an instance in the __objects dictionary with the formated key:
        <obj class name>.id

        Arguments:
            obj (BaseModel): The instance (object) that will be stored in
                             runtime memory.
        """
        key = f'{obj.__class__.__name__}.{obj.id}'
        self.__objects[key] = obj

    def save(self):
        """Save the data serializing the instances in the __objects dictionary
        to the JSON file located in __file_path.
        """
        with open(self.__file_path, "w", encoding="UTF-8") as file:
            parsed_dict = {
                key: value.to_dict()
                for key, value in self.__objects.items()
            }
            save_data(parsed_dict, file)

    def reload(self):
        """Load the data stored in the JSON file at __file_path if it exists,
        otherwise, do nothing.
        """
        if file_exist(self.__file_path):
            with open(self.__file_path, "r", encoding="UTF-8") as file:
                data = read_data(file)
                for key, value in data.items():
                    class_name = key.split('.')[0]
                    instance = BaseModel (**value)
                    FileStorage.__objects[key] = instance
