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



## Terminology

* Column
* Column name
* Table
* Schema

