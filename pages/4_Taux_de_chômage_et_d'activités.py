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
st.set_page_config(page_title="Taux de chômage et d'activités", page_icon="📊")

st.sidebar.header("Taux de chômage et d'activité")

st.header("Taux de chômage et d'activité des retraités et préretraités par région")
st.markdown("<br>", unsafe_allow_html=True)
#7
# Taux d'activité de la population en 2019
st.markdown("<h4>Taux d\'activité de la population en 2019 par région \n(rapport entre le nombre d\'actifs et la population de 15 à 64 ans en % )", unsafe_allow_html=True)

activity_rate = df_region[df_region['Designation'] == "Taux d'activité de la population en 2019 (rapport entre le nombre d'actifs et la population de 15 à 64 ans en % ) (3)"]
activity_rate = activity_rate.drop(columns='Designation')
activity_rate = activity_rate.apply(pd.to_numeric, errors='coerce')  # Conversion des données en numériques
fig, ax = plt.subplots(figsize=(12,1)) 
sns.heatmap(activity_rate, cmap='YlGnBu', annot=True, fmt=".1f", ax=ax)

st.pyplot(plt)

st.markdown("<br>", unsafe_allow_html=True)
#8
st.markdown("<h4>Taux de chômage des 50 à 64 ans VS part de retraités et préretraités parmi les personnes en emploi(en %)</h4>", unsafe_allow_html=True)

index = df_region[df_region['Designation'] == "Taux d'activité des 50 à 64 ans (en %)"].index[0]
df_chomeur = df_region.iloc[index+2]
df_chomeur = pd.DataFrame(df_chomeur)
df_chomeur.columns = df_chomeur.iloc[0]
df_chomeur = df_chomeur[1:]

retirees_working = df_region[df_region['Designation'] == "Part de retraités et préretraités parmi les personnes en emploi (en %)"]
retirees_working = retirees_working.drop(columns=['Designation']).T
retirees_working.columns = ['Retraités ayant un emploi']
df_all = df_chomeur.join(retirees_working)
df_all = df_all.sort_values('Retraités ayant un emploi', ascending=False)
st.table(df_all)