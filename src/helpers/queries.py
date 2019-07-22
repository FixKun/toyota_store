from cars.car import CarBase
from cars.parts import (
    Model,
    Colour,
    Gearbox,
    EngineCapacity
)
from helpers.sql_base import Session


def save_car(car):
    session = Session()
    session.add(car)
    session.commit()
    session.close()


def get_all():
    # Open a new session
    session = Session()
    cars = session.query(CarBase, Colour, Gearbox, Model, EngineCapacity)\
        .join(Colour)\
        .join(Gearbox)\
        .join(Model)\
        .join(EngineCapacity)\
        .all()
    session.close()

    return cars


def get_cars_prices():
    cars = get_all()
    # for car in cars:
    #     print(f"{get_car_string(car)} is {get_car_price(car)} USD")
    # return ((get_car_string(car),get_car_price(car)) for car in cars)
    car_list = list(map(lambda c: (get_car_string(c),get_car_price(c)), cars))
    car_list.sort(key=lambda c: c[1])
    return car_list


def get_models():
    session = Session()
    models = session.query(Model).order_by('id').all()
    session.close()
    print("Models:")
    for model in models:
        print(f"{model.id}: {model.name} - {model.price} USD")


def get_colours():
    session = Session()
    colours = session.query(Colour).order_by('id').all()
    session.close()
    print("Colours:")
    for colour in colours:
        print(f"{colour.id}: {colour.name} - {colour.price} USD")


def get_gearboxes():
    session = Session()
    gearboxes = session.query(Gearbox).order_by('id').all()
    session.close()
    print("Gearboxes:")
    for gearbox in gearboxes:
        print(f"{gearbox.id}: {gearbox.name} - {gearbox.price} USD")


def get_engines():
    session = Session()
    engines = session.query(EngineCapacity).order_by('id').all()
    session.close()
    print("Engine capacities:")
    for engine in engines:
        print(f"{engine.id}: {engine.name} - {engine.price} USD")


def get_cars_by_price_range(range):
    # return (car for car in get_cars_prices() if range[0] <= car[1] <= range[1])
    return list(filter(lambda car: range[0] <= car[1] <= range[1], get_cars_prices()))


def get_car_string(car):
    return f"{car[1].name} {car[3].name} ({car[4].name}) with {car[2].name} transmission"


def get_car_price(car):
    price = 0
    for i in car[1:]:
        price += i.price
    return price


