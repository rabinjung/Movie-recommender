import streamlit as st
import pickle
import requests

st.header("Movies Recommender")

movies = pickle.load(open("new_df.pkl","rb"))
similarity = pickle.load(open("similarity.pkl","rb"))
movies_list = movies["title"].values
select_movie = st.selectbox("select the movies",movies_list)


def fetch_poster (movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=e53f7032ea626efb5268555e9a898e0b"
    data =requests.get(url.format(movie_id))
    data = data.json()
    poster_path =data["poster_path"]
    full_path = "https://image.tmdb.org/t/p/w500/"+poster_path
    return full_path

def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    movie_list1 =sorted(list(enumerate(similarity[movie_index])),reverse = True, key = lambda x :x[1])[1:11]
    recommender =[]
    poster = []

    for i in movie_list1:
        movie_id = movies.iloc[i[0]].id
        recommender.append(movies.iloc[i[0]].title)
        poster.append(fetch_poster(movie_id))
    return recommender,poster
    
    
if st.button("Show Recommendation"):
    movie_name,poster = recommend(select_movie)
    c1,c2,c3,c4,c5 = st.columns(5)
    c6,c7,c8,c9,c10 = st.columns(5)
    with c1:
        st.text(movie_name[0])
        st.image(poster[0])
    with c2:
        st.text(movie_name[1])
        st.image(poster[1])
    with c3:
        st.text(movie_name[2])
        st.image(poster[2])
    with c4:
        st.text(movie_name[3])
        st.image(poster[3])
    with c5:
        st.text(movie_name[4])
        st.image(poster[4])
    with c6:
        st.text(movie_name[5])
        st.image(poster[5])   
    with c7:
        st.text(movie_name[6])
        st.image(poster[6])
    with c8:
        st.text(movie_name[7])
        st.image(poster[7])
    with c9:
        st.text(movie_name[8])
        st.image(poster[8])
    with c10:
        st.text(movie_name[9])
        st.image(poster[9])