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

IMAGE_PATH = os.path.join(dir_of_interest, "images", "AirQualityCover.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "air_quality_index.csv")

st.title("Dashboard - Air Quality")

img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)
st.dataframe(df)

DATE = st.selectbox("Select the Date: ", df['DATE'].unique())
COUNTRY = st.selectbox("Select the Country Type: ", df[df['DATE'] == DATE]['COUNTRY'].unique())

col1, col2, col3 = st.columns(3)


fig_1 = px.scatter(df[df['DATE'] == DATE], x="COUNTRY")
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.histogram(df[df['COUNTRY'] == COUNTRY], x="CITY")
col2.plotly_chart(fig_2, use_container_width=True)

fig_3 = px.histogram(df[df['COUNTRY'] == COUNTRY], x="VALUE")
col3.plotly_chart(fig_3, use_container_width=True)
