""" Init DB """

from cars.car import CarBase
from cars.parts import (
    Model,
    Colour,
    Gearbox,
    EngineCapacity
)
from helpers.sql_base import (
    BASE,
    ENGINE,
    SESSION
)

# Generate db schema
BASE.metadata.create_all(ENGINE)

# Open a new session
session = SESSION()

# Doing the do
colour_white = Colour(0, 'White', 2)
colour_black = Colour(1, 'Black', 2)
colour_pink = Colour(2, 'Pink', 15)

model_landCruiser = Model(0, 'Land Cruiser', 9000)
model_camry = Model(1, 'Camry', 6000)
model_corolla = Model(2, 'Corolla', 5000)

gearbox_manual = Gearbox(0, 'Manual', 150)
gearbox_auto = Gearbox(1, 'Auto', 300)
gearbox_var = Gearbox(2, 'Variator', 250)

capacity_two = EngineCapacity(0, '2.0', 700)
capacity_two_point_five = EngineCapacity(1, '2.5', 900)
capacity_two_point_eight = EngineCapacity(2, '2.8', 1000)

car_1 = CarBase(model_landCruiser.id, colour_black.id, gearbox_auto.id, capacity_two_point_five.id)
car_2 = CarBase(model_corolla.id, colour_pink.id, gearbox_auto.id, capacity_two_point_five.id)

# Persists data
session.add(colour_pink)
session.add(colour_black)
session.add(colour_white)

session.add(model_landCruiser)
session.add(model_camry)
session.add(model_corolla)

session.add(gearbox_auto)
session.add(gearbox_manual)
session.add(gearbox_var)

session.add(capacity_two)
session.add(capacity_two_point_five)

session.commit()

session.add(car_1)
session.add(car_2)


# Commit and close session
session.commit()
session.close()
