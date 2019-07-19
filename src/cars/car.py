"""
Base car class and car model classes.
"""
import uuid

from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from helpers.sql_base import Base, Session
from cars.parts import Model, Colour, Gearbox, EngineCapacity


class CarBase(Base):
    """Base car class"""

    __tablename__ = 'cars'

    id = Column(UUID(as_uuid=True),
                unique=True,
                primary_key=True,
                default=lambda: str(uuid.uuid4()))
    model = Column(Integer, ForeignKey('model.id'))
    colour = Column(Integer, ForeignKey('colour.id'))
    gearbox = Column(Integer, ForeignKey('gearbox.id'))
    engine_capacity = Column(Integer, ForeignKey('engine_capacity.id'))

    def __init__(self, model, colour, gearbox, engine_capacity):
        self.model = model
        self.colour = colour
        self.gearbox = gearbox
        self.engine_capacity = engine_capacity

    def get_price(self):

        session = Session()

        price = session.query(CarBase) \
        .join()
