#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ """
        new = self.value()
        if type(new.state_id) is not NoneType:
            self.assertEqual(type(new.state_id), str)
        else:
            self.assertEqual(type(new.state_id), None)

    def test_name(self):
        """ """
        new = self.value()
        if type(new.name) is not NoneType:
            self.assertEqual(type(new.name), str)
        else:
            self.assertEqual(type(new.name), None)
