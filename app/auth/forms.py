from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField,
                     BooleanField)
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = StringField('Username/Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    login = SubmitField('Login')
