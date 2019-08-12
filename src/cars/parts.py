"""
A class for car's parts and stuff
"""

from sqlalchemy import (
    Column,
    String,
    Integer
)
from app import db


class AbstractBasePart(db.Model):
    """ Car models class """

    __abstract__ = True

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)

    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.id}: {self.name} - {self.price} USD"

    def to_dict(self):
        data = {
            'id': self.id,
            'name': self.name,
            'price': self.price
        }
        return data


class Model(AbstractBasePart):

    __tablename__ = 'model'

    @classmethod
    def get_models(cls):
        """ Get all car models """
        models = db.session.query(cls).order_by('id').all()
        db.session.close()
        return models


class Gearbox(AbstractBasePart):

    __tablename__ = 'gearbox'

    @classmethod
    def get_gearboxes(cls):
        """ Get all available gearboxes """
        gearboxes = db.session.query(cls).order_by('id').all()
        db.session.close()
        return gearboxes


class EngineCapacity(AbstractBasePart):

    __tablename__ = 'engine_capacity'

    @classmethod
    def get_engines(cls):
        """ Get all available engine capacities """
        engines = db.session.query(cls).order_by('id').all()
        db.session.close()
        return engines


class Colour(AbstractBasePart):

    __tablename__ = 'colour'

    @classmethod
    def get_colours(cls):
        """ Get all available colours """
        colours = db.session.query(cls).order_by('id').all()
        db.session.close()
        return colours
