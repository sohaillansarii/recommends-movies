#  Recommends-Movies

A **content-based movie recommendation engine** that suggests similar movies using machine learning techniques. The application analyzes movie features such as **genres, cast, crew, and keywords**, computes similarity scores using **Cosine Similarity**, and recommends the most relevant movies based on user input.

Movie posters and metadata are dynamically fetched using the **TMDB API**, and the entire application is deployed as an interactive web app using **Streamlit**.

---

## 🚀 Live Demo

🌐 [Open App](https://recommends-movies-112233.streamlit.app/)
---

## 🛠️ Tech Stack

- **Python**
- **Pandas**
- **Scikit-learn**
- **Streamlit**
- **TMDB API**
- **Pickle**

---

##  Dataset


## 📊 Dataset

Dataset used:

[TMDB Movie Metadata Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

The dataset contains information such as:

- Movie title
- Genres
- Cast
- Crew
- Keywords
- Overview


---

## How It Works

Setup Instructions
1. Clone the repository
bash

git clone https://github.com/sohaillansarii/recommends-movies.git
cd recommends-movies
2. Download similarity matrix
Download similarity.pckl from Hugging Face and place it in the root directory.

3. Create virtual environment & install dependencies
bash

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
4. Configure TMDB API
Get your API key from TMDB
Create a .env file:
text

TMDB_API_KEY=your_api_key_here
5. Run the application
bash

streamlit run app.py
Live Demo
https://recommends-movies-112233.streamlit.app/

License
MIT
---

