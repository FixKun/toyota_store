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

    def __init__(self, model, colour, gearbox, engine_capacity):
        self.model = model
        self.colour = colour
        self.gearbox = gearbox
        self.engine_capacity = engine_capacity

    @classmethod
    def from_dict(cls, data):
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
    def get_cars_dict(start_range, end_range):
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
    def get_cars_prices():
        """ Get list of cars sorted by their prices """
        cars = CarBase.get_all_cars()
        car_list = list(map(lambda c: (CarBase.get_car_string(c), CarBase.get_car_price(c)), cars))
        car_list.sort(key=lambda c: c[1])
        return car_list

    @staticmethod
    def get_cars_by_price_range(price_range):
        """ Get all cars that in the price range """
        return list(filter(lambda car: price_range[0] <= car[1] <= price_range[1],
                           CarBase.get_cars_prices()))

    @staticmethod
    def get_car_string(car_result):
        """ Prettify car output"""
        return f"{car_result[1].name} {car_result[3].name} " \
            f"({car_result[4].name}) with {car_result[2].name} transmission"

    @staticmethod
    def get_car_price(car_result):
        """ Calculate car price"""
        price = 0
        for i in car_result[1:]:
            price += i.price
        return price

    def is_already_exists(self):
        return bool(CarBase.query.filter_by(model=self.model,
                                            colour=self.colour,
                                            gearbox=self.gearbox,
                                            engine_capacity=self.engine_capacity).first())
