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
st.set_page_config(page_title="Analyse du nombre de retraités et préretraités", page_icon="📊")

st.sidebar.header("Analyse du nombre de retraités et préretraités")

st.header("Analyse du nombre de retraités et préretraités")

#6
st.markdown("<h4>Nombre de retraités et pré-retraités en 2019</h4>", unsafe_allow_html=True)

#nb de retraité par région
retraité_2019 = df_region[df_region['Designation'] == 'Nombre de retraités et préretraités']
retraité_2019 = retraité_2019.drop(columns=['Designation']).T
retraité_2019.columns = ['Nombre']
st.bar_chart(retraité_2019)

#4
st.markdown("<h4>Pourcentage de retraités ayant moins de 65 ans</h4>", unsafe_allow_html=True)

under_65 = df_region[df_region['Designation'] == 'Proportion de moins de 65 ans (en %)']
under_65 = under_65.drop(columns=['Designation']).T
under_65.columns = ['Pourcentage']
st.area_chart(under_65)