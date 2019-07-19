from cars.car import CarBase
from cars.parts import Model, Colour, Gearbox, EngineCapacity
from helpers.sql_base import Base, Session, engine


# Open a new session
session = Session()

colours = session.query(CarBase).join(Colour).all()

print('\n### All colours:')
for c in colours:
    print(f'{c.id}: Colour {c.name} with a price of {c.price}')
print('')