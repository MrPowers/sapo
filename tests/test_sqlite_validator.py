import pytest
import sqlite3
import os
from sapo.sqlite_validator import SqliteValidator


dirname = os.path.dirname(__file__)


def test_contains_table():
    filename = os.path.join(dirname, './data/nfl.db')
    conn = sqlite3.connect(filename)
    s = SqliteValidator(conn)
    assert s.contains_table('players') == True
    assert s.contains_table('teams') == True
    assert s.contains_table('dogs') == False
    conn.close()


def test_only_contains_tables():
    filename = os.path.join(dirname, './data/nfl.db')
    conn = sqlite3.connect(filename)
    s = SqliteValidator(conn)
    assert s.only_contains_tables(['players', 'teams']) == True
    assert s.only_contains_tables(['players', 'teams', 'dogs']) == False
    assert s.only_contains_tables(['players']) == False
    conn.close()


def test_contains_column():
    filename = os.path.join(dirname, './data/nfl.db')
    conn = sqlite3.connect(filename)
    s = SqliteValidator(conn)
    assert s.contains_column('players', 'last_name') == True
    assert s.contains_column('players', 'last_name', 'text') == True
    assert s.contains_column('players', 'last_name', 'int') == False
    conn.close()


