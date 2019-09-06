from string import ascii_lowercase
from random import (
    choice,
    randint
)

from cars.car import CarBase
from cars.parts import (
    Model,
    Colour,
    Gearbox,
    EngineCapacity
)
from app import db


def make_colour(index, name, price, commit=True):
    colour = Colour(index, name, price)
    if commit:
        db.session.add(colour)
        db.session.commit()
    return colour


def make_model(index, name, price, commit=True):
    model = Model(index, name, price)
    if commit:
        db.session.add(model)
        db.session.commit()
    return model


def make_gearbox(index, name, price, commit=True):
    gearbox = Gearbox(index, name, price)
    if commit:
        db.session.add(gearbox)
        db.session.commit()
    return gearbox


def make_engine_capacity(index, name, price, commit=True):
    engine = EngineCapacity(index, name, price)
    if commit:
        db.session.add(engine)
        db.session.commit()
    return engine


def make_cars(count=1):
    """ Create a set of `count` random cars and save them into DB """
    for ind in range(count):
        make_colour(ind, make_string(), randint(1, 5000))
        make_engine_capacity(ind, make_string(), randint(1, 5000))
        make_gearbox(ind, make_string(), randint(1, 5000))
        make_model(ind, make_string(), randint(1, 5000))
        car = CarBase(ind, ind, ind, ind)
        db.session.add(car)
        db.session.commit()


def make_car(price=None):
    """ Create a car and save it into DB """
    if price:
        part_price = price/4
    else:
        part_price = randint(1, 5000)

    colours = Colour.get_colours()
    colour = make_colour(len(colours), make_string(), part_price, False)

    engine_capacities = EngineCapacity.get_engines()
    engine = make_engine_capacity(len(engine_capacities), make_string(), part_price, False)

    gearboxes = Gearbox.get_gearboxes()
    gearbox = make_gearbox(len(gearboxes), make_string(), part_price, False)

    models = Model.get_models()
    model = make_model(len(models), make_string(), part_price, False)

    car = CarBase(model.id, colour.id, gearbox.id, engine.id)
    db.session.add(colour)
    db.session.add(engine)
    db.session.add(model)
    db.session.add(gearbox)
    db.session.commit()
    db.session.add(car)
    db.session.commit()


def make_string(prefix=None, length=5, chars=None):
    """ Create a string a ascii chars of length `length` and return it """
    if not chars:
        chars = ascii_lowercase

    the_string = "".join(choice(chars) for _ in range(length))

    if prefix is not None:
        the_string = "{}-{}".format(prefix, the_string)

    return the_string
