#!/usr/bin/env python


from flask import Flask
from markupsafe import escape
from flask import render_template


app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h2>Hello, World!</h2> <br /> <a href="/user/example">LINK</a>'


@app.route('/user/')
@app.route('/user/<name>')
def hello(name=None):
    return render_template('user.html', name=name)