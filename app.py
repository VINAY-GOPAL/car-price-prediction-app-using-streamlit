import streamlit as st
import pandas as pd
import yfinance as yf
import datetime

st.image("./Images/apple-logo.jpg",width=70)

st.write("""

# Stock Price Analyser

Shown are the apple stock's **closing prices** and *volume of shares* traded.
""")


ticker_symbol = "AAPL"

# date filter
col1, col2 = st.columns(2)

with col1:
    start_date = st.date_input("Input starting date", datetime.date(2019, 1, 6))

with col2:
    end_date = st.date_input("Input ending date", datetime.date(2019, 7, 6))

ticker_data = yf.Ticker(ticker_symbol)
ticker_df = ticker_data.history(period="1d",start=f"{start_date}",end=f"{end_date}")

# showing dataframe
st.dataframe(ticker_df)

st.write("""

# Closing price chart
""")
st.line_chart(ticker_df.Close)

st.write("""

# Volume of shares traded
""")
st.line_chart(ticker_df.Volume)


with st.expander("See explanation"):
    st.write("""
    
    The chart above shows the apple stock's closing price from 2010-2022.
    
    """)
    st.image("./Images/apple-logo.jpg",width=50)