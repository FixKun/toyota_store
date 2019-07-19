"""
Base car class and car model classes.
"""
import uuid

from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from helpers.sql_base import Base


class CarBase(Base):
    """Base car class"""

    __tablename__ = 'cars'

    id = Column(UUID(as_uuid=True),
                unique=True,
                primary_key=True,
                default=lambda: str(uuid.uuid4()))
    model = Column(Integer, ForeignKey('model.id'))
    gearbox = Column(Integer, ForeignKey('gearbox.id'))
    engine_capacity = Column(Integer, ForeignKey('engine_capacity.id'))

    # price = 0
    # model_base_price = 0

    def __init__(self, model, colour, gearbox, engine_capacity):
        self.model = model
        self.colour = colour
        self.gearbox = gearbox
        self.engine_capacity = engine_capacity


class LandCruiser(CarBase):
    """Sub-class for Land Cruiser"""

    model_base_price = 5000


class Camry(CarBase):
    """Sub-class for Camry"""


class Corolla(CarBase):
    """Sub-class for Corolla"""