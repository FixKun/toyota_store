from app.pages import bp
from flask import (
    render_template,
    jsonify,
    request)
from flask_login import (
    login_required
)
from app.api.errors import bad_request


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

