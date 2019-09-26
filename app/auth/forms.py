# Import Form and RecaptchaField (optional)
# from flask.ext.wtf import Form  # , RecaptchaField

from wtforms import Form, TextField, PasswordField  # BooleanField

from wtforms.validators import Required, Email, EqualTo


class LoginForm(Form):
    email = TextField('Email Address', [
        Email(), Required(message='Forgot your email address?')])
    password = PasswordField('Password', [
        # EqualTo('confirm', message='Passwords do not match'),
        Required(message='Must provide a password. ;-)')])
    # confirm = PasswordField('Confirm Password')
