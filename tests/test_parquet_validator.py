import pytest
import os
import pyarrow as pa


from sapo.parquet_validator import ParquetValidator


def test_contains_column():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, './data/players.parquet')
    p = ParquetValidator(filename)
    assert p.contains_column(filename, 'last_name') == True
    assert p.contains_column(filename, 'last_name', pa.string()) == True
    assert p.contains_column(filename, 'last_name', pa.string(), True) == True
    assert p.contains_column(filename, 'last_name', pa.string(), True, None) == True
    assert p.contains_column(filename, 'id', pa.int64()) == True
    assert p.contains_column(filename, 'boo') == False

