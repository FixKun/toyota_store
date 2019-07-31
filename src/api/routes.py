from api import app
from flask import (
    render_template,
    redirect,
    url_for,
    flash
)
from flask_login import (
    current_user,
    login_user,
    login_required
)
from api.forms import LoginForm
from users.user import User


@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html')


# @app.route('/cars', methods=['POST'])
# def cars():
#     print('jsdbfjsdbhfkjshbdfkjsdf')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=True)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)