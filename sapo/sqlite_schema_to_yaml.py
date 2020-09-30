import yaml

from sapo.sqlite_helpers import SqliteHelpers


def sqlite_db_schema_to_yaml(conn, output_path):
    schema = SqliteHelpers(conn).schema()
    with open(output_path, 'w') as outfile:
        yaml.dump(schema, outfile, default_flow_style=False)

