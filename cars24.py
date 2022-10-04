import streamlit as st
import pandas as pd
import yfinance as yf
import datetime
import pickle


df_org = pd.read_csv("./cars24-car-price.csv")
#st.dataframe(df_org)

encodings = {"fuel_type": {"Diesel":1,"Petrol":2,"CNG":3,"LPG":4,"Electric":5},
             "seller_type": {"Dealer":1,"Individual":2,"Trustmark Dealer":3},
             "transmission_type": {"Manual":1,"Automatic":2}
} 

def model_pred(fuel_type, transmission_type, engine, seats):
    
    with open("car_pred", 'rb') as file:
        reg_model = pickle.load(file)

    input_features = [[2018.0, 1, 40000, fuel_type, transmission_type, 19.70, engine,86.30, seats]]
    return reg_model.predict(input_features)


#Layout

st.set_page_config(layout='wide')

st.title("Cars24 selling price prediction")

col1, col2 = st.columns(2)

fuel_type = col1.selectbox("Select fuel type", ['Diesel','Petrol','CNG','LPG','Electric'])

engine = col1.slider("Set the engine power", 500, 5000, 100)

transmission_type = col2.selectbox("Select transmission_type",['Manual','Automatic'])

seats = col2.selectbox("No. of seats",[4,5,6,7,8])

if(st.button("Predict Price")):
    fuel_type = encodings['fuel_type'][fuel_type]
    transmission_type = encodings['transmission_type'][transmission_type]

    price = model_pred(fuel_type, transmission_type, engine, seats)
    st.text("Predicted price for this car"+ str(price))