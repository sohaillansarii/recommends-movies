import streamlit as st
import pickle 
import pandas as pd
import requests 
import os

# --- 1. API KEY SETUP ---
# Do NOT use dotenv on Streamlit Cloud. Use st.secrets instead.
TMDB_API_KEY = st.secrets["TMDB_API_KEY"]

# --- 2. LOAD DATA SAFELY ---
# This safely finds your files no matter what folder Streamlit puts them in
base_dir = os.path.dirname(__file__)
movies_dict_path = os.path.join(base_dir, "movies_dict.pkl")
similarity_path = os.path.join(base_dir, "similarity.pckl")

with open(movies_dict_path, "rb") as f:
    movies_dict = pickle.load(f)
movies = pd.DataFrame(movies_dict)

with open(similarity_path, "rb") as f:
    similarity = pickle.load(f)

# --- 3. FETCH POSTER FUNCTION ---
# Fixed: This now correctly calls the TMDB API instead of a Google Drive link
def fetch_poster(movie_title):
    search_url = f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={movie_title}"
    response = requests.get(search_url)
    data = response.json()
    
    if data.get('results'):
        poster_path = data['results'][0].get('poster_path')
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500/{poster_path}"
            
    return "https://via.placeholder.com/500x750.png?text=No+Poster"

# --- 4. RECOMMENDATION FUNCTION ---
def recommend(movie_name):
    movie_index = movies[movies['title'] == movie_name].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    recommended_posters = []
    
    for i in movies_list:
        title = movies.iloc[i[0]].title 
        recommended_movies.append(title)
        recommended_posters.append(fetch_poster(title))
        
    return recommended_movies, recommended_posters

# --- 5. STREAMLIT UI ---
st.title("🎬 Movie Recommender System")

selected_movie_name = st.selectbox(
    'Select a movie to get recommendations:',
    movies['title'].values
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i])
