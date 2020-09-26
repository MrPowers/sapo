import pandas as pd
import sqlite3
import os

def create_nfl_database():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, './data/nfl.db')

    conn = sqlite3.connect(filename)
    c = conn.cursor()

    # create sqlite database tables
    c.execute('''CREATE TABLE players (id int, last_name text, position text)''')
    c.execute('''CREATE TABLE teams (id int, team_name text, team_city text)''')

    # create DataFrames
    player_data = [(1, 'gronk', 'tight_end'),
        (2, 'brady', 'qb'),
        (3, 'newton', 'qb')]
    players_df = pd.DataFrame.from_records(player_data, columns=['id', 'last_name', 'position'])

    teams_data = [(1, 'bucs', 'tampa_bay'),
        (2, 'jets', 'new_york'),
        (3, 'cheifs', 'kansas_city')]
    teams_df = pd.DataFrame.from_records(teams_data, columns=['id', 'team_name', 'team_city'])

    # load DataFrames into sqlite database
    players_df.to_sql('players', conn, if_exists='append', index = False)
    teams_df.to_sql('teams', conn, if_exists='append', index = False)

create_nfl_database()
