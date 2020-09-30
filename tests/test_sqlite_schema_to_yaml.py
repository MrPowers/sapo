import pytest
import os
import sqlite3

from sapo.sqlite_schema_to_yaml import *

dirname = os.path.dirname(__file__)

def test_sqlite_db_schema_to_yaml():
    filename = os.path.join(dirname, './data/nfl.db')
    conn = sqlite3.connect(filename)
    output_path = os.path.join(dirname, '../tmp/nfl_db_schema.yml')
    sqlite_db_schema_to_yaml(conn, output_path)

