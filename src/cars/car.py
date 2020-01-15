"""
Base car class
"""
import uuid
from sqlalchemy import (
    Column,
    ForeignKey,
    Integer
)
from sqlalchemy.dialects.postgresql import UUID
from app import db


class CarBase(db.Model):
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

    def __init__(self, model: int, colour: int, gearbox: int, engine_capacity: int):
        self.model = model
        self.colour = colour
        self.gearbox = gearbox
        self.engine_capacity = engine_capacity

    @classmethod
    def from_dict(cls, data):
        """
        Making an object instance from a dict.
        This method assumes that data in the dict is valid
        """
        return cls(model=data['model'],
                   colour=data['colour'],
                   gearbox=data['gearbox'],
                   engine_capacity=data['engine_capacity'])

    def save_car(self):
        """ Insert car into DB """
        db.session.add(self)
        db.session.commit()
        db.session.close()

    # DB stuff
    @staticmethod
    def get_all_cars():
        """ Get all cars with all parts for them """
        from cars.parts import (
            Model,
            Colour,
            Gearbox,
            EngineCapacity
        )
        cars = db.session.query(CarBase, Colour, Gearbox, Model, EngineCapacity) \
            .join(Colour) \
            .join(Gearbox) \
            .join(Model) \
            .join(EngineCapacity) \
            .all()
        db.session.close()

        return cars

    @staticmethod
    def get_cars_dict(start_range=0, end_range=None):
        """
        Returns a list of cars with parts as a dict
        :param start_range: Lower bound of a price range
        :param end_range: Upper bound of a price range
        :return: a list of cars with parts as a dict
        """
        cars = []
        for car in CarBase.get_all_cars():
            price = CarBase.get_car_price(car)
            if end_range:
                if not start_range <= price <= end_range:
                    continue
            elif price <= start_range:
                continue
            cars.append({
                'id': car[0].id,
                'price': price,
                'model': car[2].to_dict(),
                'colour': car[1].to_dict(),
                'gearbox': car[3].to_dict(),
                'engine_capacity': car[4].to_dict()
            })
        cars.sort(key=lambda c: c['price'])
        return cars

    @staticmethod
    def get_car_price(car_result):
        """ Calculate car price"""
        return sum(car.price for car in car_result[1:])

    def is_already_exists(self):
        return bool(CarBase.query.filter_by(model=self.model,
                                            colour=self.colour,
                                            gearbox=self.gearbox,
                                            engine_capacity=self.engine_capacity).first())
