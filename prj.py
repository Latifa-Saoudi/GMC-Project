import streamlit as st
import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression

# Load trained model


model = joblib.load("D:/Streamlit/GMC project streamlit/linear_model.pkl")




# UI
st.title("Tomorrow's Stock Price Predictor")
open_ = st.number_input("Open Price")
high = st.number_input("High Price")
low = st.number_input("Low Price")
close = st.number_input("Close Price")
adj_close = st.number_input("Adj Close")
volume = st.number_input("Volume")
daily_range = st.number_input("Daily Range")
intraday_change = st.number_input("Intraday Change")
avg_volume_10 = st.number_input("10-day Avg Volume")
volume_rel = st.number_input("Relative Volume")

if st.button("Predict"):
    features = [[open_, high, low, close, adj_close, volume,
                 daily_range, volume_rel]]
    prediction = model.predict(features)
    st.success(f"Predicted Close Tomorrow: {prediction[0]:.2f}")
    