# coding:utf-8

from flask_wtf import Form
#WTF Forms
from wtforms import TextField
from wtforms.validators import DataRequired
from wtforms import Form, BooleanField, TextField, PasswordField, validators

#Klasse for validering av LoginSkjema
class LoginForm(Form):
       username = TextField('Brukernavn', [validators.Required(), validators.Length(min=4, max=25)])
       password = TextField('Passord', [validators.Required(), validators.Length(min=4, max=25)])

#Klasse for validering (Fra Leksjonen)
class RegistrationForm(Form):
       username = TextField('Username', [validators.Length(min=4, max=25)])
       email = TextField('Email Address', [validators.Length(min=6, max=35)])
       password = PasswordField('New Password', [
              validators.Required(),
              validators.EqualTo('confirm', message='Passwords must match')
              ])
       confirm = PasswordField('Repeat Password')
       accept_tos = BooleanField('I accept the TOS', [validators.Required()])    
