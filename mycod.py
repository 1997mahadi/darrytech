import streamlit as st
import numpy as np 
import pandas as pd 
import plotly as py
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import plotly.figure_factory as ff

@st.cache
def load_data():
    data = pd.read_csv('case_time_series (2).csv')
    return data
       
        

st.title('COVID-19 Data Visualization:')
data_load_state = st.text('Loading data...')
st.markdown('Dataset :')
data=load_data()
st.write(data.head())       

df= data.drop(['Date'], axis=1)
st.line_chart(df)

st.bar_chart(df)

fig, ax = plt.subplots()
ax.hist(df, bins=10)
st.pyplot(fig)

st.bar_chart(data["Daily Confirmed"])

st.area_chart(df)

agree = st.button("Total Confirmed Case")
if agree:
    st.bar_chart(data["Total Confirmed"])
    


