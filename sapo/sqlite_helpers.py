class SqliteHelpers:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()


    def table_schema(self, table_name):
        return self.cursor.execute(f"""PRAGMA table_info({table_name})""").fetchall()


    def tables(self):
        tables = self.cursor.execute("""SELECT name FROM sqlite_master WHERE type='table'""").fetchall()
        return list(map(lambda r: r[0], tables))


    def schema(self):
        res = {}
        for table_name in self.tables():
            ts = self.table_schema(table_name)
            inner = {}
            for cid, column_name, data_type, notnull, dflt_value, pk in ts:
                inner[column_name] = {'data_type': data_type, 'notnull': notnull}
            res[table_name] = inner
        return res


    def schema_equals(self, expected_schema):
        return self.schema() == expected_schema

