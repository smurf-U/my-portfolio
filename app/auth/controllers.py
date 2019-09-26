from flask import Blueprint, request, render_template, \
    flash, g, session, redirect, url_for
from passlib.handlers.sha2_crypt import sha256_crypt
from app.auth.forms import LoginForm
from app.auth.models import User

auth = Blueprint('auth', __name__, url_prefix='/auth',
                 template_folder='templates',
                 static_folder='static')


# Set the route and accepted methods
@auth.route('/signin', methods=['GET', 'POST'])
def signin():
    form = LoginForm(request.form)
    if form.validate():
        user = User.query.filter_by(email=form.email.data).first()

        if user and sha256_crypt.verify(user.password, form.password.data):
            session['user_id'] = user.id

            flash('Welcome %s' % user.name)

            return redirect(url_for('auth.home'))

        flash('Wrong email or password', 'error-message')

    return render_template("auth/signin.html", form=form)
