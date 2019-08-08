from app.pages import bp
from flask import (
    render_template,
    jsonify,
    request)
from flask_login import (
    login_required
)
from cars.parts import (
    Model,
    Colour,
    Gearbox,
    EngineCapacity
)


@bp.route('/cars', methods=['GET'])
def get_cars():
    from db.queries import get_cars_dict

    start_range = request.args.get('start_range', 0, type=int)
    end_range = request.args.get('end_range', None, type=int)
    # todo validation
    return jsonify(get_cars_dict(start_range, end_range))


@bp.route('/model/<int:id>', methods=['GET'])
def get_model(id):
    return jsonify(Model.query.get_or_404(id).to_dict())


@bp.route('/colour/<int:id>', methods=['GET'])
def get_colour(id):
    return jsonify(Colour.query.get_or_404(id).to_dict())


@bp.route('/engine/<int:id>', methods=['GET'])
def get_engine(id):
    return jsonify(EngineCapacity.query.get_or_404(id).to_dict())


@bp.route('/gearbox/<int:id>', methods=['GET'])
def get_gearbox(id):
    return jsonify(Gearbox.query.get_or_404(id).to_dict())

