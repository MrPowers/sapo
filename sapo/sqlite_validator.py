class SqliteValidator:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()


    def table_schema(self, table_name):
        return self.cursor.execute(f"""PRAGMA table_info({table_name})""").fetchall()


    def tables(self):
        tables = self.cursor.execute("""SELECT name FROM sqlite_master WHERE type='table'""").fetchall()
        return list(map(lambda r: r[0], tables))


    def contains_table(self, table_name):
        return table_name in self.tables()


    def only_contains_tables(self, table_names):
        return sorted(self.tables()) == sorted(table_names)


    def contains_column(self, table_name, column_name, data_type = None, nullable = None, default_value = None):
        col = next((i for i in self.table_schema(table_name) if i[1] == column_name), None)
        if not col:
            return False
        if data_type and col[2] != data_type:
            return False
        if nullable and col[3] != nullable:
            return False
        if default_value and col[4] != default_value:
             return False
        return True

