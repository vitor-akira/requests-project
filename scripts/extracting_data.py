import sys
import os
from scripts.repos_data import DataRepos

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

amazon_rep = DataRepos('amzn')
lang_most_used_amzn = amazon_rep.create_df_languages()

netflix_rep = DataRepos('netflix')
lang_most_used_netflix = netflix_rep.create_df_languages()

spotify_rep = DataRepos('spotify')
lang_most_used_spotify = spotify_rep.create_df_languages()

apple_rep = DataRepos('apple')
lang_most_used_apple = apple_rep.create_df_languages()

# saving datas

lang_most_used_amzn.to_csv('datas/languages_amzn.csv')
lang_most_used_netflix.to_csv('datas/languages_netflix.csv')
lang_most_used_spotify.to_csv('datas/languages_spotify.csv')
lang_most_used_apple.to_csv('datas/languages_apple.csv')