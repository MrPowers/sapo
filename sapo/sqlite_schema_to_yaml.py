import yaml

# sqlite GUIs let you copy the create statement to a string
# The CREATE TABLE syntax is like this
# CREATE TABLE players (id int, last_name text, position text)
# The argument to this function should be the "id int, last_name text, position text" part

def sqlite_create_table_to_yaml(table_name, cols, output_path):
    # data = dict(
        # A = 'a',
        # B = dict(
            # C = 'c',
            # D = 'd',
            # E = 'e',
        # )
    # )

    data = {table_name: {}}

    for col in cols.split(", "):
        col_name, data_type = col.split(" ")
        data[table_name][col_name] = {"data_type": data_type}


    with open(output_path, 'w') as outfile:
        yaml.dump(data, outfile, default_flow_style=False)

