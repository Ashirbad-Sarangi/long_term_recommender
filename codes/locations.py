import os

data_folder = '../data'

dataset_filename = 'MovieLens100k_dataset'
rated_filename = "rated_movies.csv"

dataset_path = os.path.join(data_folder,dataset_filename)
data_path = os.path.join(dataset_path,'u.data')
genre_path = os.path.join(dataset_path,'u.genre')
item_path = os.path.join(dataset_path,'u.item')
occupation_path = os.path.join(dataset_path,'u.occupation')
user_path = os.path.join(dataset_path,'u.user')
rated_path = os.path.join(data_folder,rated_filename)
