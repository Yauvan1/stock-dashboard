import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("📈 Stock Market Dashboard")

# User input
ticker = st.text_input("Enter Stock Symbol", "AAPL")

# Get stock data
stock = yf.Ticker(ticker)

# History
data = stock.history(period="6mo")

# Show table
st.subheader("Stock Data")
st.write(data.tail())

# Show chart
st.subheader("Closing Price Chart")

fig, ax = plt.subplots()

ax.plot(data.index, data['Close'])

ax.set_xlabel("Date")
ax.set_ylabel("Closing Price")

st.pyplot(fig)