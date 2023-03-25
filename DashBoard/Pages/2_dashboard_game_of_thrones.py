import streamlit as st
from matplotlib import image
import pandas as pd
import seaborn as sns
import plotly.express as px
import os

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "GOTCover.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "game_of_thrones.csv")

st.title("Dashboard - Game of Thrones")

img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)
st.dataframe(df)

Season = st.selectbox("Select the Season: ", df['Season'].unique())
Title = st.selectbox("Select the Title: ", df[df['Season'] == Season]['Title'].unique())

col1, col2, col3 = st.columns(3)


fig_1 = px.scatter(df[df['Season'] == Season], x="Imdb_rating")
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.histogram(df[df['Season'] == Season], x="Imdb_rating")
col2.plotly_chart(fig_2, use_container_width=True)

fig_3 = px.histogram(df[df['Title'] == Title], x="Episode_No")
col3.plotly_chart(fig_3, use_container_width=True)
