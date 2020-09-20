import pandas as pd
import os

def create_players_file():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, './data/players.parquet')

    player_data = [(1, 'gronk', 'tight_end'),
        (2, 'brady', 'qb'),
        (3, 'newton', 'qb')]

    players_df = pd.DataFrame.from_records(player_data, columns=['id', 'last_name', 'position'])

    players_df.to_parquet(filename)

create_players_file()
