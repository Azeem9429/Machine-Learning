import streamlit as st
import pickle
import pandas as pd
import requests
#mport similarity

movies_dict= pickle.load(open('movies_dict.pkl','rb'))
movies= pd.DataFrame(movies_dict)



def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(movie):
    # to find the index of any movie
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_list=[]
    recommended_movie_posters = []
    for i in movies_list:
        recommended_list.append(movies.iloc[i[0]].title)
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
    return recommended_list,recommended_movie_posters
        
    
similarity = pickle.load(open('similarity.pkl','rb'))


st.title('Movies Recommendation')

selected_movie_name = st.selectbox("Select a Movie",movies['title'].values)


if st.button('Recommend Movie'):
    recommended_list,recommended_movie_posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(recommended_movie_posters[0])
        st.text(recommended_list[0])
        
    with col2:
        st.image(recommended_movie_posters[1])
        st.text(recommended_list[1])
        

    with col3:
        st.image(recommended_movie_posters[2])
        st.text(recommended_list[2])
        
    with col4:
        st.image(recommended_movie_posters[3])
        st.text(recommended_list[3])
        
    with col5:
        st.image(recommended_movie_posters[4])
        st.text(recommended_list[4])
        
   
        



