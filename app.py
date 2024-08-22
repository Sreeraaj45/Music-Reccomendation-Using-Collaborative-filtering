import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import csr_matrix

file_path = 'Spotify-2000.csv'  
data = pd.read_csv(file_path)

data.drop_duplicates(inplace=True)
data.dropna(inplace=True)
data.reset_index(drop=True, inplace=True)

data_encoded = pd.get_dummies(data, columns=['Artist', 'Top Genre'], drop_first=True)

user_item_matrix = data.pivot_table(index='Artist', columns='Title', values='Popularity', fill_value=0)
user_item_sparse = csr_matrix(user_item_matrix.values)

item_similarity = cosine_similarity(user_item_sparse.T)
item_similarity_df = pd.DataFrame(item_similarity, index=user_item_matrix.columns, columns=user_item_matrix.columns)

def recommend_songs(song_title, similarity_matrix, num_recommendations=5):
    similar_songs = similarity_matrix[song_title].sort_values(ascending=False)
    recommended_songs = similar_songs.iloc[1:num_recommendations+1].index.tolist()
    recommendations = data[data['Title'].isin(recommended_songs)][['Title', 'Artist']].reset_index()
    recommendations.insert(0, 'S.No', recommendations.index + 1)
    return recommendations

st.title('Music Recommendation System')

song_title = st.selectbox('Select a song for recommendation:', data['Title'].unique())

num_recommendations = st.slider('Number of recommendations:', 1, 10, 5)

if st.button('Recommend Songs'):
    recommendations = recommend_songs(song_title, item_similarity_df, num_recommendations)
    st.table(recommendations[['S.No', 'Title', 'Artist']]) #Sreeraaj Manepalli
