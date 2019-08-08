""" Set of DB queries """

from cars.car import CarBase
from cars.parts import (
    Model,
    Colour,
    Gearbox,
    EngineCapacity
)
from app import db


#  todo распихать по классам????
def get_all_cars():
    """ Get all cars with all parts for them """
    cars = db.session.query(CarBase, Colour, Gearbox, Model, EngineCapacity) \
        .join(Colour) \
        .join(Gearbox) \
        .join(Model) \
        .join(EngineCapacity) \
        .all()
    db.session.close()

    return cars


def get_cars_prices():
    """ Get list of cars sorted by their prices """
    cars = get_all_cars()
    car_list = list(map(lambda c: (get_car_string(c), get_car_price(c)), cars))
    car_list.sort(key=lambda c: c[1])
    return car_list


def get_cars_dict(start_range, end_range):
    cars = []
    for car in get_all_cars():
        price = get_car_price(car)
        if end_range:
            if not start_range <= price <= end_range:
                continue
        elif price <= start_range:
            continue
        cars.append({
            'id': car[0].id,
            'price': price,
            'model': car[2].to_dict(),
            'colour': car[1].to_dict(),
            'gearbox': car[3].to_dict(),
            'engine_capacity': car[4].to_dict()
        })
    cars.sort(key=lambda c: c['price'])
    return cars


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
