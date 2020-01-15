from flask import (
    jsonify,
    request,
    g
)
from sqlalchemy.exc import ProgrammingError

from app.api.auth import token_auth
from app.api import bp
from app.api.errors import error_response, bad_request


@bp.route('/cars', methods=['GET'])
def get_cars():
    from cars.car import CarBase
    start_range = request.args.get('start_range', 0, type=int)
    end_range = request.args.get('end_range', None, type=int)
    if end_range and start_range > end_range:
        return bad_request("'start_range' cannot be greater than 'end_range'.")
    return jsonify(CarBase.get_cars_dict(start_range, end_range))


@bp.route('/model/', methods=['GET'])
@bp.route('/model/<int:id>', methods=['GET'])
def get_model(id=None):
    from cars.parts import Model
    return return_all_or_by_id(id, Model)


@bp.route('/colour/', methods=['GET'])
@bp.route('/colour/<int:id>', methods=['GET'])
def get_colour(id=None):
    from cars.parts import Colour
    return return_all_or_by_id(id, Colour)


@bp.route('/engine/', methods=['GET'])
@bp.route('/engine/<int:id>', methods=['GET'])
def get_engine(id=None):
    from cars.parts import EngineCapacity
    return return_all_or_by_id(id, EngineCapacity)


@bp.route('/gearbox/', methods=['GET'])
@bp.route('/gearbox/<int:id>', methods=['GET'])
def get_gearbox(id=None):
    from cars.parts import Gearbox
    return return_all_or_by_id(id, Gearbox)


@bp.route('/car', methods=['PUT'])
@token_auth.login_required
def add_car():
    from cars.car import CarBase
    if not g.current_user.is_admin():
        return bad_request('You don\'t have permission to perform this action')
    from cars.parts import (
        Model,
        Gearbox,
        EngineCapacity,
        Colour
    )
    data = request.get_json() or {}
    required_fields = ['model', 'colour', 'engine_capacity', 'gearbox']
    if not all(required_field in data for required_field in required_fields):
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
    try:
        car.save_car()
    except ProgrammingError:
        return error_response(400, "Unexpected error occurred")
    response = jsonify(data)
    response.status_code = 201
    return response


def return_all_or_by_id(id, entity):
    if id:
        return jsonify(entity.query.get_or_404(id).to_dict())
    else:
        return jsonify([part.to_dict() for part in entity.get_parts()])

