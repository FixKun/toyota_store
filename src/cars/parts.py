"""
A class for car's parts and stuff
"""

from sqlalchemy import Column, String, Integer
from sqlalchemy.dialects.postgresql import UUID
from helpers.sql_base import Base


class AbstractBasePart(Base):
    """Car models class """

    __abstract__ = True

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)

    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


class Model(AbstractBasePart):

    __tablename__ = 'model'



class Gearbox(AbstractBasePart):

    __tablename__ = 'gearbox'


class EngineCapacity(AbstractBasePart):

    __tablename__ = 'engine_capacity'


class Colour(AbstractBasePart):

    __tablename__ = 'colour'

