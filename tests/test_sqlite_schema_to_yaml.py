import pytest
import os

from sapo.sqlite_schema_to_yaml import *

def test_sqlite_create_table_to_yaml():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../tmp/nfl_players_schema.yml')

    cols = "id int, last_name text, position text"
    sqlite_create_table_to_yaml('players', cols, filename)

