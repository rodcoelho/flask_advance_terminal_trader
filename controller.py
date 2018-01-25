#!/usr/bin/env python3

import os
from flask import Flask, request, render_template, redirect, url_for
from forms import SignupForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
with open('/Users/rodrigocoelho/.ssh/fake_secret_key.txt') as f:
    app.secret_key = f.readline()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////database/database.sqlite'

@app.route('/', methods = ['GET'])
def index():
    return "Welcome to Flask"

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    title = 'Sign Up'
    h1 = "Register"
    form = SignupForm()

    if request.method == 'GET':
        return render_template('signup.html', form=form, title=title, h1=h1)
    elif request.method == 'POST':
        if form.validate_on_submit():
            if 'user already exist in db':
                return "Email address already exists"
            else:
                return "User has been added to DB"
        else:
            return "Form didn't validate"


if __name__ == '__main__':
    app.run(port=5000, host='localhost')
