import pandas as analytics
import numpy as maths
import os
import warnings
warnings.filterwarnings("ignore")

def extract_values(a):
    return [i.strip().replace(" ","_") for i in a.split("|")]

source_path = 'MovieLens100k_dataset'
data_path = os.path.join(source_path,'u.data')
genre_path = os.path.join(source_path,'u.genre')
item_path = os.path.join(source_path,'u.item')
occupation_path = os.path.join(source_path,'u.occupation')
user_path = os.path.join(source_path,'u.user')

data_headers = """user id | movie id | rating | timestamp"""
item_headers = """movie id | movie title | release date | video release date |
              IMDb URL | unknown | Action | Adventure | Animation |
              Children's | Comedy | Crime | Documentary | Drama | Fantasy |
              Film-Noir | Horror | Musical | Mystery | Romance | Sci-Fi |
              Thriller | War | Western |"""
user_headers = """user id | age | gender | occupation | zip code"""


data_headers = extract_values(data_headers)
item_headers = extract_values(item_headers)[:-1]
user_headers = extract_values(user_headers)


df_data = analytics.read_csv(data_path,header = None,sep="\t",names = data_headers)
df_data['rating'] = df_data['rating'] - 3

df_users = analytics.read_csv(user_path,header=None,sep = "|",names = user_headers)

df_items = analytics.read_csv(item_path, header = None, sep = "|" , names = item_headers)
df_items = df_items.drop(['release_date','video_release_date','IMDb_URL'],axis = 1)
df_items = df_items[df_items['unknown'] == 0]
df_items = df_items.drop('unknown',axis = 1)

