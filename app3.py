from flask import Flask, request, render_template

import sqlite3


app = Flask(__name__)


create_books_table_sql = '''
    CREATE TABLE books (
    book_id INTEGER PRIMARY KEY
    , title TEXT NOT NULL UNIQUE
    , year INTEGER NOT NULL
    );
'''

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/create-db')
def create_db():
    try:
        msg = "Connecting..."
        conn = sqlite3.connect('books.db')
        msg = "Connected..."
        cur = conn.cursor()
        msg = "Got cursor..."
        cur.execute(create_books_table_sql)
        conn.commit()
        msg = "Table created..."
    except Exception as ex:
        conn.rollback()
        msg = str(ex)
    finally:
        return render_template("create_db.html", msg = msg)


@app.route('/add-book',methods = ['GET', 'POST'])
def add_book():

    if request.method == 'GET':
        return render_template('add_book.html')


    if request.method == 'POST':

        try:

            title = request.form['title']
            year = request.form['year']

            conn = sqlite3.connect('books.db')
            cur = conn.cursor()
            cur.execute("INSERT INTO books (title,year) VALUES (?,?)", (title, year))
            conn.commit()

            msg = "Record successfully added"

        except Exception as ex:

            conn.rollback()
            msg = "error in insert operation"

        finally:
            return render_template("render_outcome.html",msg = msg)



@app.route('/listing-books')
def listing_books():


    rows = None
    msg = None
    try:

        conn = sqlite3.connect('books.db')
        cur = conn.cursor()
        conn.row_factory = sqlite3.Row
        cur.execute('SELECT * FROM books')
        rows = cur.fetchall()
        msg = "success"

    except Exception as ex:
        print(ex)
        msg = "failed"

    finally:

        return render_template('listing_books.html', rows = rows, msg = msg)


