import pyarrow.parquet as pq
import pyarrow as pa


class ParquetValidator:
    def __init__(self, path):
        self.path = path
        self.table = pq.read_table(path)


    def contains_column(self, column_name, data_type = None, nullable = None, metadata = None):
        col = next((i for i in self.table.schema if i.name == column_name), None)
        if not col:
            return False
        if data_type and col.type != data_type:
            return False
        if nullable and col.nullable != nullable:
            return False
        if metadata and col.metadata != metadata:
            return False
        return True


    def validate_schema(self, expected_schema):
        return self.table.schema.equals(expected_schema)

# def only_contains_columns():
