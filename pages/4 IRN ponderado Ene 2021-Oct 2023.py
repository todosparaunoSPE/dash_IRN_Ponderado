# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 12:03:48 2023

@author: jperezr
"""

import pandas as pd
import numpy as np
import streamlit as st

from numerize.numerize import numerize

# Data import & columns
df = pd.read_csv('Libro4.csv')


st.title(f"IRN ponderado por mes")
st.header("ene-2021 a oct-2023")
st.subheader("Ranking")

st.subheader("")
st.subheader("")
st.subheader("")
st.subheader("")

###############################################################################################

with st.sidebar:
    Afore_filter = st.multiselect(label= 'Seleccione una AFORE',
                                options=df['AFORE'].unique(),
                                default=df['AFORE'].unique())

    Fecha_filter = st.multiselect(label='Seleccione una Fecha',
                            options=df['Fecha'].unique(),
                            default=df['Fecha'].unique())

df1 = df.query('AFORE == @Afore_filter & Fecha == @Fecha_filter')

total_IRN  = float(df1['IRN ponderado'].sum())
total_Ranking = float(df1['Ranking'].sum())



total1,total2 = st.columns(2,gap='large')

with total1:
    st.image('images/irn.png',use_column_width='Auto')
    st.metric(label = 'IRN ponderado', value= numerize(total_IRN))
    
with total2:
    st.image('images/posicion-ranking.png',use_column_width='Auto')
    st.metric(label='Total Ranking', value=numerize(total_Ranking))


################################################################################################

st.subheader("")
st.subheader("")
st.subheader("")
st.subheader("")


df = df[df['AFORE'].isin(Afore_filter)]
df = df[df['Fecha'].isin(Fecha_filter)]



# Main


# Main - dataframes
st.markdown('### Cuadro de datos')


s = df.style.format({"Expense": lambda x : '{:.4f}'.format(x)})
st.dataframe(s)

#st.dataframe(df.sort_values('Suma IRN',
#             ascending=False).reset_index(drop=True))
