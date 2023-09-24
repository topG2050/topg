
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, DataRequired, Email, EqualTo, ValidationError
from market.models import User

class RegisterForm(FlaskForm):

    def validate_username(self, username_to_check):
        username = User.query.filter_by(username=username_to_check.data).first()
        if username:
            raise ValidationError('This username already exits')
        

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address= email_address_to_check.data).first()
        if email_address:
            raise ValidationError('This Email already exits')


    username = StringField(label='Username', validators=[Length(min=6, max=20), DataRequired()])
    email_address = StringField(label='Email', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create an account')

class LoginForm(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired()])
    password= StringField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Sign In')