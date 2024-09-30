import sqlite3
import pytest


@pytest.fixture
def client_db():
    conn = sqlite3.connect('clients.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT NOT NULL,
    age TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Country(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    country TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users (id)
    )
    ''')
    contacts = [('Ivan', 'Ivanov', 'ivanivanov@example.com', '987-65-43', '30'),
                ('Piotr', 'Petrov', 'piotrpetrov@example.com', '210-98-76', '31'),
                ('Semen', 'Semenov', 'semensemenov@example.com', '543-21-09', '26'),
                ('Masha', 'Mashkina', 'mashamashkina@example.com', '876-54-32', '29'),
                ('Ruslan', 'Vide', 'ruslanvide@example.com', '109-87-65', '40'),
                ('Teresa', 'Kaleta', 'teresakaleta@example.com', '432-10-98', '48')]
    cursor.executemany("INSERT INTO Users (name, surname, email, phone, age) VALUES (?, ?, ?, ?, ?)", contacts)
    conn.commit()


    cursor.execute('''select id, name from Users''')
    rows = cursor.fetchall()
    map = {name: user_id for user_id, name in rows}

    country = [(map['Ivan'], 'Belarus'),
              (map['Piotr'], 'Poland'),
              (map['Semen'], 'Poland'),
              (map['Masha'], 'Russia'),
              (map['Ruslan'], 'Belarus'),
              (map['Teresa'], 'Poland')]

    cursor.executemany("INSERT INTO Country (user_id, country) VALUES (?, ?)", country)
    conn.commit()

    cursor.execute('''select c.name, c.phone, c.email from Users as c
    INNER JOIN Country as a
    ON c.id=a.user_id
    WHERE c.name='Masha'
    ''')

    yield cursor.fetchall()

    cursor.close()
    conn.close()

@pytest.fixture
def get_connection():
    conn = sqlite3.connect('clients.db')
    cursor = conn.cursor()

    yield cursor

    cursor.close()
    conn.close()