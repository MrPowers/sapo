# sapo

Python data source validator.  Helps you check schemas and types at every step of your data pipeline.

## sqlite schema validation

Import the `SqliteValidator` and instantiate it with a sqlite connection object.

```python
from sapo.sqlite_validator import SqliteValidator

s = SqliteValidator(conn)
```

Check to make sure that the database contains the `players` table.

```python
s.contains_table('players') # True
```

Now check that the `players` table has a `last_name` text column.

```python
s.contains_column('players', 'last_name', 'text') # True
```

## Parquet schema validation

Import the `ParquetValidator` and instantiate it with a path to a Parquet file.

```python
from sapo.parquet_validator import ParquetValidator

s = ParquetValidator(path)
```

Make sure the Parquet file has a `last_name` string type column.

```python
import pyarrow as pa

p = ParquetValidator(filename)
p.contains_column('last_name', pa.string()) # True
```

Check the entire schema of a Parquet file.

```python
p = ParquetValidator(filename)
expected_schema = pa.schema([
    pa.field("id", pa.int64(), True),
    pa.field("last_name", pa.string(), True),
    pa.field("position", pa.string(), True)])
p.validate_schema(expected_schema) # True
```

## Terminology

* Table
* Column
* Column name
* Schema

