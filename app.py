from itsdangerous import json
import streamlit as st

'''
# TaxiFareModel front
'''

st.markdown("Taxi Fare Predictor")

import datetime

date_input = st.date_input("Pickup Date", datetime.date(2022, 6, 3))
time_input = st.time_input("Pickup Time", datetime.time(8, 45))

pickup_longitude = st.number_input('Pickup longitude')
pickup_latitude = st.number_input('Pickup latitude')
dropoff_longitude = st.number_input('Dropoff longitude')
dropoff_latitude = st.number_input('Dropoff latitude')
passenger_count = st.number_input('Passenger count')

predict_dict = {'pickup_datetime': '{} {}'.format(date_input, time_input),
                "pickup_longitude" : pickup_longitude,
                "pickup_latitude" : pickup_latitude,
                "dropoff_longitude" : dropoff_longitude,
                "dropoff_latitude" : dropoff_latitude,
                "passenger_count" : int(passenger_count)

        }


url = 'https://taxifare.lewagon.ai/predict'

import requests

response = requests.get(url, params=predict_dict).json()

if st.button('Get Prediction'):
    # print is visible in the server output, not in the page
    st.write(response["fare"])
    st.write('I was clicked 🎉')
else:
    st.write('I was not clicked 😞')
