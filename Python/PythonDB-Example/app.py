# -*- coding: utf-8 -*-
# imports
from flask import Flask, request, g, redirect, url_for, \
     abort, render_template, flash, jsonify

from forms import RegistrationForm
from flask.ext.sqlalchemy import SQLAlchemy
import os

#WTF Forms
from wtforms import Form, BooleanField, TextField, PasswordField, validators

# mappen der scriptet kjøres
basedir = os.path.abspath(os.path.dirname(__file__))

# konfigurasjon av globale variable
DATABASE = 'blogg.db'
DEBUG = True
SECRET_KEY = 'test'

# definerer sti for databasen
DATABASE_PATH = os.path.join(basedir, DATABASE)

# database uri'en
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH

# lager og initialiserer app’en
app = Flask(__name__)
app.config.from_object(__name__)
db = SQLAlchemy(app)

import models
@app.route('/')
def index():
       """Leter etter data fra bloggen i databasen og viser de."""
       entries = db.session.query(models.Blogg)
       return render_template('index.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
       """Legger inn nye data i databasen."""
       new_entry = models.Blogg(request.form['tittel'],
                                request.form['nyhet'],
                                request.form['forfatter'])
       db.session.add(new_entry)
       db.session.commit()
       flash('Nytt innlegg ble lagret')
       return redirect(url_for('index'))

# Registerings Skjema
@app.route('/adduser', methods=['POST'])
def add_user():
       """Legger inn nye brukere i databasen."""
       new_entry2 = models.Bruker(request.form['brukernavn'],
                                request.form['passord'],
                                request.form['navn'])
       db.session.add(new_entry2)
       db.session.commit()
       flash('Nytt bruker ble lagret')
       """Leter etter data fra bruker databasen og viser de."""
       entries = db.session.query(models.Bruker)
       return render_template('register.html', entries=entries)


# Innlogging før aksess til bloggen (Brukernavn og Passord: admin)
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Feil brukernavn eller passord.'
        else:
                   return redirect(url_for('index'))
    return render_template('login.html', error=error)


#Route Validering av Login Skjema (WTForm)
@app.route('/logginn', methods=['GET', 'POST'])
def loginskjema():
       form = LoginForm(request.form)
       if request.method == 'POST' and form.validate():
              return redirect(url_for('blogg'))
       return render_template('logginn.html', form=form)


#Route Validering av Register kjema (Fra Leksjonen)
@app.route('/register', methods=['GET', 'POST'])
def register():
       form = RegistrationForm(request.form)
       if request.method == 'POST' and form.validate():
              user = User(form.brukernavn.data, form.navn.data,
                          form.passord.data)
              db_session.add(user)
              flash('Thanks for registering')
              return redirect(url_for('login'))
       return render_template('register.html', form=form)

if __name__ == '__main__':
       app.run()
