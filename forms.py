from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField , ValidationError
from wtforms.validators import DataRequired, Email , EqualTo


class CommentForm(FlaskForm):
    name = StringField('name' , validators=[DataRequired()])
    email = StringField('name' , validators=[DataRequired(), Email()])
    message = TextAreaField('message')
    

class RegisterForm(FlaskForm):
    name = StringField('name' , validators=[DataRequired()] )
    email = StringField('email' , validators=[DataRequired() , Email()])
    password = StringField('password' , validators=[DataRequired()])
    confirm_password = StringField( 'password' , validators=[DataRequired() , EqualTo('password')])


class LoginForm(FlaskForm):
    name = StringField('name' , validators=[DataRequired()])
    password = StringField('password' , validators=[DataRequired()])


