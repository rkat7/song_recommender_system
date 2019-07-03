# Collaborative based system predicts what a particular user might like based on what other similar users like.
# Leveraging the item similarity based collaborative filtering model

is_model = Recommenders.item_similarity_recommender_py()
is_model.create(train_data, 'user_id', 'song')

