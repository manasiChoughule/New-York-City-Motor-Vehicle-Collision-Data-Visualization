import streamlit as st
import pandas as pd
import numpy as np


# import the date

DATA_URL = "/Users/manasichoughule/Desktop/NYC_streamlit/Motor_Vehicle_Collisions_-_Crashes.csv"


st.title("Motor Vehicle Collisions in New York City")
st.markdown("This application is a Streamlit dashboards that can be used to analyze motor vehicle collisions in NYC 🗽💥🚗")

# stops running the loading of data again and again, only loads when the value changes.
@st.cache_data(persist =True)
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows= nrows, parse_dates=[['CRASH_DATE','CRASH_TIME']])
    data.dropna(subset = ['LATITUDE', 'LONGITUDE'], inplace = True)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis = 'columns', inplace = True)
    data.rename(columns = {'carsh_date_crash_time':'date/time'}, inplace = True)
    return data

data = load_data(100000)

st.header("Where are the most people injured in NYC?")

injured_people = st.slider("Number of persons injured in vehicle collision",0, 19)
st.map(data.query("injured_persons >= @injured_people")[["latitude",'longitude']].dropna(how="any"))

if st.checkbox("Show Raw Data", False):
    st.subheader('Raw Data')
    st.write(data)

st.header("How many collisions occur during a given time of day?")
hour = st.slider("Hour to look at", 0,23)
data = data[data['date/time'].dt.hour == hour]


