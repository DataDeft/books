CREATE TABLE books (
    book_id INTEGER PRIMARY KEY
    , title TEXT NOT NULL UNIQUE
    , year INTEGER NOT NULL
);