import pytest
import sqlite3
import os
from sapo.sqlite_helpers import SqliteHelpers


dirname = os.path.dirname(__file__)


def test_table_schema():
    filename = os.path.join(dirname, './data/nfl.db')
    conn = sqlite3.connect(filename)
    s = SqliteHelpers(conn)
    expected = [
        (0, 'id', 'int', 0, None, 0),
        (1, 'last_name', 'text', 0, None, 0),
        (2, 'position', 'text', 0, None, 0)]
    assert s.table_schema('players') == expected
    conn.close()


def test_tables():
    filename = os.path.join(dirname, './data/nfl.db')
    conn = sqlite3.connect(filename)
    s = SqliteHelpers(conn)
    assert s.tables() == ['players', 'teams']
    conn.close()


def test_schema():
    filename = os.path.join(dirname, './data/nfl.db')
    conn = sqlite3.connect(filename)
    s = SqliteHelpers(conn)
    expected = {
        'players': {
            'id': {'data_type': 'int', 'notnull': 0},
            'last_name': {'data_type': 'text', 'notnull': 0},
            'position': {'data_type': 'text', 'notnull': 0}},
        'teams': {
            'id': {'data_type': 'int', 'notnull': 0},
            'team_name': {'data_type': 'text', 'notnull': 0},
            'team_city': {'data_type': 'text', 'notnull': 0}}}
    assert s.schema() == expected
    conn.close()


def test_schema_equals():
    filename = os.path.join(dirname, './data/nfl.db')
    conn = sqlite3.connect(filename)
    s = SqliteHelpers(conn)
    expected = {
        'players': {
            'id': {'data_type': 'int', 'notnull': 0},
            'last_name': {'data_type': 'text', 'notnull': 0},
            'position': {'data_type': 'text', 'notnull': 0}},
        'teams': {
            'id': {'data_type': 'int', 'notnull': 0},
            'team_name': {'data_type': 'text', 'notnull': 0},
            'team_city': {'data_type': 'text', 'notnull': 0}}}
    assert s.schema_equals(expected) == True
    conn.close()

