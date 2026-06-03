import streamlit as st
import pickle 
import pandas as pd
import requests 
import os
from dotenv import load_dotenv

load_dotenv()

TMDB_API_KEY = os.getenv("TMDB_API_KEY")

base_dir = os.path.dirname(__file__)
movies_dict_path = os.path.join(base_dir, "movies_dict.pkl")
similarity_path = os.path.join(base_dir, "similarity.pckl")

if not os.path.exists(similarity_path):
    url = "https://drive.google.com/file/d/1XSQJM_F7NoCcLS6Y980-Ocpe4hQYEoMZ/view?usp=sharing"
    response = requests.get(url)
    with open(similarity_path, "wb") as f:
        f.write(response.content)

with open(movies_dict_path, "rb") as f:
    movies_dict = pickle.load(f)
movies = pd.DataFrame(movies_dict)

with open(similarity_path, "rb") as f:
    similarity = pickle.load(f)


def fetch_poster(movie_title):
    url = "https://drive.google.com/file/d/1XSQJM_F7NoCcLS6Y980-Ocpe4hQYEoMZ/view?usp=sharing"
    response = requests.get(url)
    data = response.json()
    
    if data['results']:
        poster_path = data['results'][0].get('poster_path')
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500/{poster_path}"
            
    return "https://via.placeholder.com/500x750.png?text=No+Poster"

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
