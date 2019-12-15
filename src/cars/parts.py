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

    @classmethod
    def get_parts(cls):
        """ Get all car models """
        models = db.session.query(cls).order_by('id').all()
        db.session.close()
        return models


class Model(AbstractBasePart):

    __tablename__ = 'model'


class Gearbox(AbstractBasePart):

    __tablename__ = 'gearbox'


class EngineCapacity(AbstractBasePart):

    __tablename__ = 'engine_capacity'


class Colour(AbstractBasePart):

    __tablename__ = 'colour'

