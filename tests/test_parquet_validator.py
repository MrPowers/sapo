import pytest
import os
import pyarrow as pa


from sapo.parquet_validator import ParquetValidator


def test_contains_column():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, './data/players.parquet')
    p = ParquetValidator(filename)
    assert p.contains_column('last_name') == True
    assert p.contains_column('last_name', pa.string()) == True
    assert p.contains_column('last_name', pa.string(), True) == True
    assert p.contains_column('last_name', pa.string(), True, None) == True
    assert p.contains_column('id', pa.int64()) == True
    assert p.contains_column('boo') == False


def test_validate_schema():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, './data/players.parquet')
    p = ParquetValidator(filename)

    expected_schema = pa.schema([
        pa.field("id", pa.int64(), True),
        pa.field("last_name", pa.string(), True),
        pa.field("position", pa.string(), True)])
    assert p.validate_schema(expected_schema) == True

    wrong_schema = pa.schema([
        pa.field("id", pa.string(), True),
        pa.field("last_name", pa.string(), True),
        pa.field("position", pa.string(), True)])
    assert p.validate_schema(wrong_schema) == False


