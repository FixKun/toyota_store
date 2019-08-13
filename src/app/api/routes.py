from app.api.auth import token_auth
from app.pages import bp
from flask import (
    jsonify,
    request
)

from app.api.errors import bad_request
from cars.car import CarBase


@bp.route('/cars', methods=['GET'])
def get_cars():
    from cars.car import CarBase

    start_range = request.args.get('start_range', 0, type=int)
    end_range = request.args.get('end_range', None, type=int)
    if end_range and start_range > end_range:
        return bad_request("'start_range' cannot be greater than 'end_range'.")
    return jsonify(CarBase.get_cars_dict(start_range, end_range))


@bp.route('/model/<int:id>', methods=['GET'])
def get_model(id):
    from cars.parts import Model
    return jsonify(Model.query.get_or_404(id).to_dict())


@bp.route('/colour/<int:id>', methods=['GET'])
def get_colour(id):
    from cars.parts import Colour
    return jsonify(Colour.query.get_or_404(id).to_dict())


@bp.route('/engine/<int:id>', methods=['GET'])
def get_engine(id):
    from cars.parts import EngineCapacity
    return jsonify(EngineCapacity.query.get_or_404(id).to_dict())


@bp.route('/gearbox/<int:id>', methods=['GET'])
def get_gearbox(id):
    from cars.parts import Gearbox
    return jsonify(Gearbox.query.get_or_404(id).to_dict())


@bp.route('/car/add', methods=['PUT'])
@token_auth.login_required
def add_car():
    from cars.parts import (
        Model,
        Gearbox,
        EngineCapacity,
        Colour
    )
    data = request.get_json() or {}
    if 'model' not in data or 'colour' not in data or 'engine_capacity' not in data or 'gearbox' not in data:
        return bad_request('Must include `model`, `colour`, `engine_capacity` and `gearbox` fields')
    if not Model.query.filter_by(id=data['model']).first():
        return bad_request('Model not found. Please, use existing model')
    if not Colour.query.filter_by(id=data['colour']).first():
        return bad_request('Colour not found. Please, use existing colour')
    if not EngineCapacity.query.filter_by(id=data['engine_capacity']).first():
        return bad_request('Engine capacity not found. Please, use existing Engine capacity')
    if not Gearbox.query.filter_by(id=data['gearbox']).first():
        return bad_request('Gearbox not found. Please, use existing gearbox')
    car = CarBase.from_dict(data)
    if car.is_already_exists():
        return bad_request('Car already exists.')
    car.save_car()
    response = jsonify(data)
    response.status_code = 201
    return response
