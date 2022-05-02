import pickle
from urllib.request import urlopen
import PIL.Image
import io
import pandas as pd
import requests
import streamlit as st
from PIL import Image
from bs4 import BeautifulSoup

image1 = Image.open('image_search_16481053202241.jpg')

st.image(image1)
st.title('Mainak Movie Recommendation')

english_m = pickle.load(open('df_english.pkl', 'rb'))
english_movies = pd.DataFrame(english_m)
hindi_m = pickle.load(open('df_hindi.pkl', 'rb'))
hindi_movies = pd.DataFrame(hindi_m)
bengali_m = pickle.load(open('df_bengali.pkl', 'rb'))
bengali_movies = pd.DataFrame(bengali_m)

similarity1 = pickle.load(open('similarity1.pkl', 'rb'))
similarity2 = pickle.load(open('similarity2.pkl', 'rb'))
similarity3 = pickle.load(open('similarity3.pkl', 'rb'))

option = st.selectbox(
    'Select Language',
    ('Bengali', 'Hindi', 'English'))

if option == 'English':
    final_df = english_movies
    similarity = similarity1


elif option == 'Hindi':
    final_df = hindi_movies
    similarity = similarity2


elif option == 'Bengali':
    final_df = bengali_movies
    similarity = similarity3


def movie_poster_fetcher(poster_url):
    url_data = requests.get(poster_url).text
    s_data = BeautifulSoup(url_data, 'html.parser')
    imdb_dp = s_data.find("meta", property="og:image")
    movie_poster_link = imdb_dp.attrs['content']
    u = urlopen(movie_poster_link)
    raw_data = u.read()
    image = PIL.Image.open(io.BytesIO(raw_data))
    image = image.resize((130, 247), )
    return image
    # st.image(image, use_column_width=False)


def recommend(movie1):
    movie_index = final_df[final_df['title'] == movie1].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[0:6]

    recommend_movies = []
    movie_poster = []
    for i in movie_list:
        recommend_movies.append(final_df['title'].iloc[i[0]])
        movie_poster.append(movie_poster_fetcher(final_df['poster_url'].iloc[i[0]]))
    # post_1 = final_df['poster_url'][final_df[final_df['title'] == movie].index.values].values
    post_1 = final_df['poster_url'][
        int(final_df[final_df['title'] == movie].index.values)]
    return recommend_movies, movie_poster, post_1


movie = st.selectbox(
    'Select Movie Name',
    final_df['title'].values)

if st.button('Recommend'):
    names, posters, pos = recommend(movie)
    st.image(movie_poster_fetcher(pos))
    st.header(movie)
    st.title('Recommendations')

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[1])
        st.image(posters[1])
    with col2:
        st.text(names[2])
        st.image(posters[2])
    with col3:
        st.text(names[3])
        st.image(posters[3])
    with col4:
        st.text(names[4])
        st.image(posters[4])
    with col5:
        st.text(names[5])
        st.image(posters[5])
