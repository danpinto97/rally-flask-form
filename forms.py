from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, RadioField, DateTimeField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class TextForm(FlaskForm):
    answer1 = StringField(label= 'Text Answer',  validators=[DataRequired()])
    checkbox1 = SelectField(label= 'Check Answer', choices= [
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("3", "3")
    ])
    radio1 = RadioField(label= "This is a radio",
    choices= [
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("3", "3")
    ]
    )
    dob = DateTimeField(label= "Date of birth")
    submit = SubmitField('Submit')

class NumForm(FlaskForm):
    answer2 = StringField(label= 'numAnswer')
