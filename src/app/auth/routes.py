from app.auth import bp
from flask import (
    render_template,
    redirect,
    url_for,
    flash
)
from flask_login import (
    current_user,
    login_user,
    logout_user
)
from app.auth.forms import LoginForm
from users.user import User


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('pages.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Password is incorrect. Please, try again.")
            return redirect(url_for('auth.login'))
        login_user(user, remember=True)
        return redirect(url_for('pages.index'))
    return render_template('login.html', title='Sign In', form=form)


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
