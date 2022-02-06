import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pickle

#Load-Model
classifier = pickle.load(open('/content/dtrmodel.pkl','rb'))

#Page-Design
title = '<h2 style="font-family:arial; color:black; font-size: 47px;text-align:center;"><b>Pre-owned Car Price Prediction</b></h2>'
st.markdown(title,unsafe_allow_html=True)

title2 = '<p style="font-family:Sans-serif; color:#a1a6ad; font-size: 18px;text-align:center;"><b>Not Sure at what price you want to sell your car?<br>Use our tool to predict the selling price of your car</b></p>'
st.markdown(title2,unsafe_allow_html=True)

title1 = '<h4 style="font-family:arial; color:black; font-size: 30px;text-align:center;"><b>Parameters</b></h4>'
st.markdown(title1,unsafe_allow_html=True)


#Input-Fields
col1,col2 = st.columns(2)
with col1:
  cp = st.text_input("Current Price (eg: 4.56)")
with col2:  
  kms = st.text_input('Kilometer Driven')

col3,col4 = st.columns(2)
with col3:
  seller = st.selectbox('Select Seller Type',('Dealer','Individual'))
with col4:
  trans = st.selectbox('Select Transmission Type',('Manual','Automatic'))

col5,col6 = st.columns(2)
with col5:
  own = st.selectbox('Select Owner Type',('First (0)','Second (1)','Third (2)'))
with col6:
  age = st.text_input("Age Difference (Current Year - MFG Year of Car)")

#Encoding
if seller == 'Dealer':
  y = 0
else:
  y = 1

if trans == 'Manual':
  z = 1
else:
  z = 0

if own == 'First (0)':
  m = 0
elif own == 'Second (1)':
  m = 1
else:
  m = 3

#Prediction
col10, col11, col12, col13, col14,col15,col16 = st.columns(7)
if col13.button('Submit'):
  predict = classifier.predict([[cp,kms,y,z,m,age]])[0]
  res = 'The Price of Car :  {} (in Lakhs)'.format(round(predict,3))
  st.success(res)