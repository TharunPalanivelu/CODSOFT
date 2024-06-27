import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


data = {
    'user_id': [1, 1, 1, 2, 2, 3, 3, 3, 4, 4],
    'movie_id': [1, 2, 3, 1, 4, 2, 3, 5, 4, 5],
    'rating': [5, 3, 4, 4, 5, 2, 5, 3, 4, 2]
}


ratings_df = pd.DataFrame(data)


user_movie_matrix = ratings_df.pivot(index='user_id', columns='movie_id', values='rating').fillna(0)

print("User-Movie Rating Matrix:")
print(user_movie_matrix)

def get_similar_users(user_id, user_movie_matrix, top_n=2):
  
    user_similarity = cosine_similarity(user_movie_matrix)

    
    user_similarity_df = pd.DataFrame(user_similarity, index=user_movie_matrix.index, columns=user_movie_matrix.index)

   
    similar_users = user_similarity_df[user_id].sort_values(ascending=False)[1:top_n+1]

    return similar_users


similar_users = get_similar_users(1, user_movie_matrix, top_n=2)
print("\nSimilar Users to User 1:")
print(similar_users)

def recommend_movies(user_id, user_movie_matrix, similar_users, top_n=3):
    
    similar_users_ratings = user_movie_matrix.loc[similar_users.index]

    movie_recommendations = similar_users_ratings.mean(axis=0)

   
    user_rated_movies = user_movie_matrix.loc[user_id]
    movie_recommendations = movie_recommendations[user_rated_movies == 0]

 
    top_movie_recommendations = movie_recommendations.sort_values(ascending=False).head(top_n)

    return top_movie_recommendations


recommended_movies = recommend_movies(1, user_movie_matrix, similar_users, top_n=3)
print("\nRecommended Movies for User 1:")
print(recommended_movies)
