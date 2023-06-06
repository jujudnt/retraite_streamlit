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
st.set_page_config(page_title="Répartition des retraités en emploi", page_icon="📊")

st.sidebar.header("Répartition des retraités en emploi")

st.header("Répartition des retraités et préretraités exerçant un emploi")

#5
st.markdown("<h4>Répartition des retraités et préretraités exerçant un emploi selon leur tranche d’âge</h4>", unsafe_allow_html=True)

age_dist = df_concat[df_concat['Designation'].isin(['Moins de 60 ans', '60 à 64 ans', '65 à 69 ans', '70 à 74 ans', '75 ans et plus'])]
age_dist = age_dist.set_index('Designation').T
age_dist = age_dist.loc['France entière']
fig, ax = plt.subplots()
ax.pie(age_dist, labels=age_dist.index, autopct='%1.1f%%')
ax.axis('equal')  # Pour un graphique à secteurs circulaire.
#plt.title('Répartition des retraités et préretraités exerçant un emploi selon leur tranche d’âge')
st.pyplot(fig)

#10
st.markdown("<h4>Répartition des retraités et préretraités exerçant un emploi par région (en %)</h4>", unsafe_allow_html=True)

index = df_region[df_region['Designation'] == "Répartition des retraités et préretraités exerçant un emploi selon leur catégorie socioprofessionnelle en %"].index[0]
df_retraite = df_region.iloc[index:-1]
df_retraite_clean = df_retraite.dropna(how='all')
# Créez un nouveau DataFrame pour stocker les données nécessaires
heatmap_data = pd.DataFrame()

# Stockez la catégorie actuelle (sera mise à jour à chaque nouvelle catégorie rencontrée)
current_category = ""

# Parcourez chaque ligne du DataFrame nettoyé
for i, row in df_retraite_clean.iterrows():
    # Si la ligne est une catégorie (ne contient pas "Proportion"), mettez à jour la catégorie actuelle
    if "Proportion" not in row['Designation']:
        current_category = row['Designation']
    # Sinon, si la ligne contient les proportions pour les retraités en cumul emploi-retraite, ajoutez ces données au nouveau DataFrame
    elif "Proportion parmi les retraités en cumul emploi-retraite" in row['Designation']:
        heatmap_data[current_category] = row[1:]
        
# Transposez le DataFrame pour que les catégories deviennent des colonnes et les régions deviennent des lignes
heatmap_data = heatmap_data.T


# Convertir toutes les données en float
heatmap_data = heatmap_data.apply(pd.to_numeric, errors='coerce')

# Créer une figure
fig, ax = plt.subplots(figsize=(10, 8))

# Créez la heatmap
sns.heatmap(heatmap_data, cmap='YlGnBu', annot=True)


# Afficher la figure avec streamlit
st.pyplot(fig)