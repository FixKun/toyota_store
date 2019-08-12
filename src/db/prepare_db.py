""" Init DB """
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app import create_app, db
from cars.car import CarBase
from cars.parts import (
    Model,
    Colour,
    Gearbox,
    EngineCapacity
)
from users.user import User

# app = Flask(__name__)
# app.config.from_object(Config)
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)
app = create_app()

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

# Add users
admin = User('admin', True)
admin.set_password('password')
user = User('user', False)
user.set_password('pass')

# Generate db schema
with app.app_context():
    db.create_all()

    # Add data to DB
    db.session.add(colour_pink)
    db.session.add(colour_black)
    db.session.add(colour_white)

    db.session.add(model_landCruiser)
    db.session.add(model_camry)
    db.session.add(model_corolla)

    db.session.add(gearbox_auto)
    db.session.add(gearbox_manual)
    db.session.add(gearbox_var)

    db.session.add(capacity_two)
    db.session.add(capacity_two_point_five)

    db.session.commit()

    db.session.add(car_1)
    db.session.add(car_2)
    db.session.commit()

    db.session.add(admin)
    db.session.add(user)

    # Commit and close session
    db.session.commit()
    db.session.close()
