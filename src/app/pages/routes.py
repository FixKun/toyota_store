from app.pages import bp
from flask import (
    render_template
)
from flask_login import (
    login_required
)


@bp.route('/')
@bp.route('/index')
@login_required
def index():
    return render_template('index.html')


# @app.route('/cars', methods=['POST'])
# def cars():
#     print('jsdbfjsdbhfkjshbdfkjsdf')
