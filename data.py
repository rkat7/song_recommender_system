# Using a couple of datasets from the Million Songs Dataset
# The triplet_file contains user_id, song_id and listen time. The metadat_file contains song_id, title, release_by and artist_name. 
# Million Songs Dataset is a mixture of song from various website with the rating that users gave after listening to the song.

# Have to integrate both triplet_file and metadata_file using Pandas

triplets_file = 'https://static.turi.com/datasets/millionsong/10000.txt'
songs_metadata_file = 'https://static.turi.com/datasets/millionsong/song_data.csv'

# Read the table of triplet_file using pandas and define the 3 columns as user_id, song_id and listen_count
song_df_1 = pandas.read_table(triplets_file,header=None)
song_df_1.columns = ['user_id', 'song_id', 'listen_count']

# Read the metadat_file and combine the metadata_file with triplets_file. Whenever datasets are combined, there will be duplicate columns. The duplicates between 2 datasets are dropped using song_id
song_df_2 =  pandas.read_csv(songs_metadata_file)
song_df = pandas.merge(song_df_1, song_df_2.drop_duplicates(['song_id']), on="song_id", how="left")

# Visualize the combined dataset 
print(song_df.head())

print(len(song_df))   #Total lenght of dataset

# DATA TRANSFORMATION (Doing data transformation allows to further simplify the dataset and makes it easy and simple to understand)
  # Create a subset of the original data. Using first 10k songs here
  # Merge the song and artist_name into one column, aggregated by number of time a particular song is listened too in general by all users.

# group the song_df by number of listen_count ascending
song_grouped = song_df.groupby(['song']).agg({'listen_count': 'count'}).reset_index()

#calculate the group_sum by summing the listen_count of each song
grouped_sum = song_grouped['listen_count'].sum()

#add a new column called percentage, and calculate this percentage by dividing the listen_count by the sum of listen_count of all songs and then multiply by 100
song_grouped['listen_count'].div(grouped_sum)*100

#list the song in the ascending order of popularity for a given song
song_grouped.sort_values(['listen_count', 'song'], ascending = [0,1])




