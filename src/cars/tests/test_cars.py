import unittest
from cars.tests import factory
from app import create_app, db
from cars.car import CarBase
from config import TestConfig
from cars.parts import (
    Model,
    Colour,
    Gearbox,
    EngineCapacity
)
from users.user import User


class TestSum(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_class=TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_to_dict(self):
        """
        Test it can be converted from dict to instance
        """
        factory.make_colour(2, 'White', 4)
        factory.make_engine_capacity(0, '2.5', 400)
        factory.make_gearbox(1, 'Auto', 700)
        factory.make_model(0, 'Corolla', 4)
        data = {"model": 0,
                "gearbox": 1,
                "colour": 2,
                "engine_capacity": 0}
        result = CarBase.from_dict(data)
        self.assertEqual(result.engine_capacity, 0)
        self.assertEqual(result.model, 0)
        self.assertEqual(result.colour, 2)
        self.assertEqual(result.gearbox, 1)
        self.assertIsInstance(result, CarBase)

    def test_get_all_cars(self):
        """ test that get_all_cars() method returns a full set of cars in DB"""
        count = 5
        factory.make_cars(count)
        cars = CarBase.get_all_cars()
        self.assertEqual(len(cars), count)
        factory.make_car()
        cars = CarBase.get_all_cars()
        self.assertEqual(len(cars), count+1)

    def test_get_all_cars_returns_empty_list_when_no_cars_in_db(self):
        cars = CarBase.get_all_cars()
        self.assertEqual(len(cars), 0)

    def test_get_cars_dist_return_correctly_sorted_dict(self):
        factory.make_car(3000)
        factory.make_car(2000)
        car_dict = CarBase.get_cars_dict()
        self.assertEqual(len(car_dict), 2)
        self.assertEqual(car_dict[0]['price'], 2000)
        self.assertEqual(car_dict[1]['price'], 3000)

    def test_get_cars_dist_filter_out_prices_lower_then_lower_boundary(self):
        factory.make_car(3000)
        factory.make_car(2000)
        car_dict = CarBase.get_cars_dict(2500)
        self.assertEqual(len(car_dict), 1)
        self.assertEqual(car_dict[0]['price'], 3000)

    def test_get_cars_dist_filter_out_prices_higher_then_higher_boundary(self):
        factory.make_car(3000)
        factory.make_car(2000)
        car_dict = CarBase.get_cars_dict(0, 2500)
        self.assertEqual(len(car_dict), 1)
        self.assertEqual(car_dict[0]['price'], 2000)

    def test_get_cars_dist_return_empty_list_if_no_cars_found(self):
        factory.make_car(2000)
        car_dict = CarBase.get_cars_dict(100,250)
        self.assertEqual(len(car_dict), 0)



if __name__ == '__main__':
    unittest.main()
