""" Set of DB queries """

from cars.car import CarBase
from cars.parts import (
    Model,
    Colour,
    Gearbox,
    EngineCapacity
)
from app import db


def save_car(car):
    """ Insert car into DB """
    db.session.add(car)
    db.session.commit()
    db.session.close()


def get_all_cars():
    """ Get all cars with all parts for them """
    cars = db.session.query(CarBase, Colour, Gearbox, Model, EngineCapacity)\
        .join(Colour)\
        .join(Gearbox)\
        .join(Model)\
        .join(EngineCapacity)\
        .all()
    db.session.close()

    return cars


def get_cars_prices():
    """ Get list of cars sorted by their prices """
    cars = get_all_cars()
    car_list = list(map(lambda c: (get_car_string(c), get_car_price(c)), cars))
    car_list.sort(key=lambda c: c[1])
    return car_list


def get_models():
    """ Get all car models """
    models = db.session.query(Model).order_by('id').all()
    db.session.close()
    return models


def get_colours():
    """ Get all available colours """
    colours = db.session.query(Colour).order_by('id').all()
    db.session.close()
    return colours


def get_gearboxes():
    """ Get all available gearboxes """
    gearboxes = db.session.query(Gearbox).order_by('id').all()
    db.session.close()
    return gearboxes


def get_engines():
    """ Get all available engine capacities """
    engines = db.session.query(EngineCapacity).order_by('id').all()
    db.session.close()
    return engines


def get_cars_by_price_range(price_range):
    """ Get all cars that in the price range """
    return list(filter(lambda car: price_range[0] <= car[1] <= price_range[1],
                       get_cars_prices()))


def get_car_string(car):
    """ Prettify car output"""
    return f"{car[1].name} {car[3].name} ({car[4].name}) with {car[2].name} transmission"


def get_car_price(car):
    """ Calculate car price"""
    price = 0
    for i in car[1:]:
        price += i.price
    return price
