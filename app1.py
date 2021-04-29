#!/usr/bin/env python


from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h2>Hello, World!</h2> <br /> <a href="/user/example">LINK</a>'


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)

