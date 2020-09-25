class SqliteHelpers:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()


    def table_schema(self, table_name):
        return self.cursor.execute(f"""PRAGMA table_info({table_name})""").fetchall()


    def tables(self):
        tables = self.cursor.execute("""SELECT name FROM sqlite_master WHERE type='table'""").fetchall()
        return list(map(lambda r: r[0], tables))
