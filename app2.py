
from flask import Flask, render_template
from markupsafe import escape


app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h2>Hello, World!</h2> <br /> <a href="/user/example">With param</a> <br /> <a href="/user">Without</a>'


@app.route('/user/')
@app.route('/user/<name>')
def hello(name=None):
    return render_template('user.html', name=name)
