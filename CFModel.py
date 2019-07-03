# Collaborative based system predicts what a particular user might like based on what other similar users like.
# Leveraging the item similarity based collaborative filtering model

is_model = Recommenders.item_similarity_recommender_py()
is_model.create(train_data, 'user_id', 'song')

#Print the songs for the user in training data
user_id = users[5]
user_items = is_model.get_user_items(user_id)

#print("------------------------------------------------------------------------------------")
print("Training data songs for the user userid: %s:" % user_id)
print("------------------------------------------------------------------------------------")
for user_item in user_items:
    print(user_item)
print("----------------------------------------------------------------------")
print("Recommendation process going on:")
print("----------------------------------------------------------------------")

#Recommend songs for the user using personalized model
is_model.recommend(user_id)

# We can also use our item similarity based collaborative filtering model to find similar songs to any songs in our dataset:
is_model.get_similar_items(['U Smile - Justin Bieber'])




