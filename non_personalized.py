# This is a naive model

# count the number of unique users and songs in our subset of data
users = song_df['user_id'].unique()
len(users) 

songs = song_df['song'].unique()
len(songs) 

# splitting our dataset into training and testing data
train_data, test_data = train_test_split(song_df, test_size = 0.20, random_state=0)

# Using a popularity based Recommender class as a black box to train the model

pm = Recommenders.popularity_recommender_py() # Using an instance of that class
pm.create(train_data, 'user_id', 'song')

# use the popularity model to make some prediction
user_id = users[5]
pm.recommend(user_id)

