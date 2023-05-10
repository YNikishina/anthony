#Getting our necessary libraries
import pandas as pd
import streamlit as st
import plotly_express as px #So that's why a requirements.txt file is needed...
#loading our dataset
cars_us = pd.read_csv('vehicles_us.csv')

#creating a new column titled 'manufacturer', which gets the first word of the 'model' column
cars_us['manufacturer'] = cars_us['model'].apply(lambda x: x.split()[0])

st.header('Vehicle types by manufacturer')                          #Creating a histogram about the vehicle brands...
veh_type = px.histogram(cars_us,x='manufacturer', color='type')     #Our histogram line of code
st.write(veh_type)                                                  #Showing the histogram with Streamlit

st.header('Vehicle Condition')                                      #And then one about each vehicle's condition.
veh_con = px.histogram(cars_us, x='condition',color='type')
st.write(veh_con)

st.header('Scatterplot Distribution of Price and Miles of Vehicle Type')
example = px.scatter(cars_us, x='price', y='odometer')
st.write(example)

#----------------------

st.header('Price comparision between two different manufacturers')      
manufac_list = sorted(cars_us['manufacturer'].unique())                 #Our list of car manufacturers
manufacturer_1 = st.selectbox(                                          #Gets users inputs from dropdown menu
                            label= 'Choose the first manufacturer',     #Title of the select box
                            options=manufac_list,                       #Options listed in select box
                            index=manufac_list.index('ford'))           #Default pre-selected option

manufacturer_2 = st.selectbox(                                          #Repeat practice for second dropdown
                            label= 'Choose the second manufacturer',     
                            options=manufac_list,                       
                            index=manufac_list.index('chevrolet'))
mask_filter = (cars_us['manufacturer'] == manufacturer_1) | (cars_us['manufacturer'] == manufacturer_2)
cars_us_filtered = cars_us[mask_filter]
normalize = st.checkbox('Normalize histogram', value=True)
if normalize:
    histnorm = 'percent'
else:
    histnorm = None
st.write(px.histogram(cars_us_filtered,
                    x='price',
                    nbins=30,
                    color='manufacturer',
                    histnorm=histnorm,
                    barmode='overlay'))
