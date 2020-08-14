#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ """
        new = self.value()
        if new.city_id is not None:
            self.assertEqual(type(new.city_id), str)
        else:
            self.assertEqual(new.city_id, None)

    def test_user_id(self):
        """ """
        new = self.value()
        if new.user_id is not None:
            self.assertEqual(type(new.user_id), str)
        else:
            self.assertEqual(new.user_id, None)

    def test_name(self):
        """ """
        new = self.value()
        if new.name is not None:
            self.assertEqual(type(new.name), str)
        else:
            self.assertEqual(new.name, None)

    def test_description(self):
        """ """
        new = self.value()
        if new.description is not None:
            self.assertEqual(type(new.description), str)
        else:
            self.assertEqual(new.description, None)

    def test_number_rooms(self):
        """ """
        new = self.value()
        if new.number_rooms is not None:
            self.assertEqual(type(new.number_rooms), int)
        else:
            self.assertEqual(new.number_rooms, None)

    def test_number_bathrooms(self):
        """ """
        new = self.value()
        if new.number_bathrooms is not None:
            self.assertEqual(type(new.number_bathrooms), int)
        else:
            self.assertEqual(new.number_bathrooms, None)

    def test_max_guest(self):
        """ """
        new = self.value()
        if new.max_guest is not None:
            self.assertEqual(type(new.max_guest), int)
        else:
            self.assertEqual(new.max_guest, None)

    def test_price_by_night(self):
        """ """
        new = self.value()
        if new.price_by_night is not None:
            self.assertEqual(type(new.price_by_night), int)
        else:
            self.assertEqual(new.price_by_night, None)

    def test_latitude(self):
        """ """
        new = self.value()
        if new.latitude is not None:
            self.assertEqual(type(new.latitude), float)
        else:
            self.assertEqual(new.latitude, None)

    def test_longitude(self):
        """ """
        new = self.value()
        if new.longitude is not None:
            self.assertEqual(type(new.latitude), float)
        else:
            self.assertEqual(new.longitude, None)

    def test_amenity_ids(self):
        """ """
        new = self.value()
        if new.amenity_ids is not None:
            self.assertEqual(type(new.amenity_ids), list)
        else:
            self.assertEqual(new.amenity_ids, None)
