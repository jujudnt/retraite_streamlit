import pandas as pd
import numpy as np
import urllib.request
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pydeck as pdk
import sys
sys.path.append('../')
from retraite import get_df

df_concat, df_region = get_df()

st.set_page_config(page_title="Evolution de la population", page_icon="📊")

st.sidebar.header("Evolution de la population")

st.header("Evolution de la population entre 2019 et 2022")

#1
# Sélectionnez les données pour le graphique
st.markdown("<h4>Population au 1er janvier 2019 par régions</h4>", unsafe_allow_html=True)

pop_2019 = df_region[df_region['Designation'] == 'Population au 1er janvier 2019 (Recensement de la population)']
pop_2019 = pop_2019.drop(columns=['Designation']).T
pop_2019.columns = ['Population 2019']

st.bar_chart(pop_2019)

#2
st.markdown("<h4>Population au 1er janvier 2022 par régions</h4>", unsafe_allow_html=True)

pop_2022 = df_region[df_region['Designation'] == 'Population au 1er janvier 2022 (Estimation de population) (1)']
pop_2022 = pop_2022.drop(columns=['Designation']).T
pop_2022.columns = ['Population 2022']
st.bar_chart(pop_2022)

population_data = pop_2019.join(pop_2022)

st.markdown("<h4>Variation de la population entre 2019 et 2022</h4>", unsafe_allow_html=True)

# calculate the percentage change
population_data['Percentage Change'] = ((population_data['Population 2022'] - population_data['Population 2019']) / population_data['Population 2019']) * 100

st.bar_chart(population_data['Percentage Change'])

