# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 11:22:19 2023

@author: jperezr
"""

import pandas as pd
import numpy as np
import streamlit as st

from numerize.numerize import numerize


# Data import & columns
df = pd.read_csv('Libro1.csv')

st.title(f"IRN ene-2021 a oct-2023")

st.subheader("")
st.subheader("")
st.subheader("")
st.subheader("")


#############################################################################################

with st.sidebar:
    Afore_filter = st.multiselect(label= 'Seleccione una AFORE',
                                options=df['AFORE'].unique(),
                                default=df['AFORE'].unique())

    Siefore_filter = st.multiselect(label='Seleccione una SIEFORE',
                            options=df['SIEFORE'].unique(),
                            default=df['SIEFORE'].unique())

    Fecha_filter = st.multiselect(label='Seleccione una Fecha',
                            options=df['Fecha'].unique(),
                            default=df['Fecha'].unique())

df1 = df.query('AFORE == @Afore_filter & SIEFORE == @Siefore_filter & Fecha == @Fecha_filter')

total_IRN  = float(df1['IRN'].sum())

total_Ranking = float(df1['Ranking'].sum())



total1,total2 = st.columns(2,gap='large')

with total1:
    st.image('images/irn.png',use_column_width='Auto')
    st.metric(label = 'Total IRN', value= numerize(total_IRN))
    
with total2:
    st.image('images/posicion-ranking.png',use_column_width='Auto')
    st.metric(label='Total Ranking', value=numerize(total_Ranking))


#############################################################################################


#AFORE = list(df['AFORE'].drop_duplicates())

#SIEFORE = list(df['SIEFORE'].drop_duplicates())

#Fecha = list(df['Fecha'].drop_duplicates())

## App

## Sidebar - title & filters
#st.sidebar.markdown('### Filtro de datos')
#AFORE_choice = st.sidebar.multiselect(
#    'Elige una AFORE:', AFORE, default=AFORE)

#SIEFORE_choice = st.sidebar.multiselect(
#    "Elige una SIEFORE:", SIEFORE, default=SIEFORE)

#Fecha_choice = st.sidebar.multiselect(
#    "Elige una Fecha:", Fecha, default=Fecha)


##price_choice = st.sidebar.slider(
##    'Max Price:', min_value=4.0, max_value=15.0, step=.5, value=15.0)


df = df[df['AFORE'].isin(Afore_filter)]
df = df[df['SIEFORE'].isin(Siefore_filter)]
df = df[df['Fecha'].isin(Fecha_filter)]


st.subheader("")
st.subheader("")
st.subheader("")
st.subheader("")

#############################################################################################


# Main


# Main - dataframes
st.markdown('### Cuadro de datos')

st.dataframe(df.sort_values('IRN',
             ascending=False).reset_index(drop=True))

