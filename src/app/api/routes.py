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


@bp.route('/cars', methods=['POST'])
def get_cars():
    from db.queries import get_cars_dict

    if request.data:
        data = request.get_json() or {}
        if 'start_range' not in data or 'end_range' not in data:
            return jsonify(get_cars_dict())
        else:
            price_range = list(data.values())
            return jsonify(get_cars_dict(price_range))
    return jsonify(get_cars_dict())


@bp.route('/model/<int:id>', methods=['POST'])
def get_model(id):
    return jsonify(Model.query.get_or_404(id).to_dict())


@bp.route('/colour/<int:id>', methods=['POST'])
def get_colour(id):
    return jsonify(Colour.query.get_or_404(id).to_dict())


@bp.route('/engine/<int:id>', methods=['POST'])
def get_engine(id):
    return jsonify(EngineCapacity.query.get_or_404(id).to_dict())


@bp.route('/gearbox/<int:id>', methods=['POST'])
def get_gearbox(id):
    return jsonify(Gearbox.query.get_or_404(id).to_dict())

