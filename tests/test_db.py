import pytest
import requests
from helpers.db import client_db, get_connection


def test_db_(client_db):
    data_db = client_db

    for row in data_db:
        _, _, email = row
        assert '@' in email


def test_db_example(get_connection):
    cursor = get_connection

    cursor.execute('''select c.name, c.phone, c.email from Users as c
        INNER JOIN Country as a
        ON c.id=a.user_id
        WHERE c.name='MAsha'
        ''')

    data_db = cursor.fetchall()

    for row in data_db:
        _, _, email = row
        assert '@' in email