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
st.set_page_config(page_title="Espérance de vie", page_icon="📊")

st.sidebar.header("Espérance de vie")

st.header("Espérance de vie de la population par région")

#8
st.markdown("<h4>Espérance de vie à la naissance en 2021</h4>", unsafe_allow_html=True)

index = df_region[df_region['Designation'] == "Espérance de vie à la naissance en 2021 (1) (3)"].index[0]
selected_rows = df_region.iloc[index+1:index+3]
variable_1 = selected_rows.iloc[0]
variable_2 = selected_rows.iloc[1]
df_hommes = pd.DataFrame(variable_1)
df_femmes = pd.DataFrame(variable_2)
df_hommes.columns = df_hommes.iloc[0]
df_femmes.columns = df_femmes.iloc[0]
df_hommes = df_hommes[1:]
df_femmes = df_femmes[1:]
df_h_f = df_hommes.join(df_femmes)
df_h_f = df_h_f.dropna()
st.line_chart(df_h_f)



#11
st.markdown("<h4>Espérance de vie à partir de 65 ans en 2021</h4>", unsafe_allow_html=True)

index = df_region[df_region['Designation'] == "Espérance de vie à 65 ans en 2021 (1) (3)"].index[0]
df_vie = df_region.iloc[index+1:index+3]
df_vie = df_vie.mean()
df_vie = df_vie.dropna(how='all')

# DataFrame avec les latitudes et les longitudes des plus grandes villes de chaque région
df_cities = pd.DataFrame({
    'Region': ['AUVERGNE-\nRHÔNE-ALPES', 'BOURGOGNE-\nFRANCHE-COMTE', 'BRETAGNE', 'CENTRE - \nVAL DE LOIRE', 'GRAND EST', 'HAUTS-DE-FRANCE ', 'ILE-DE-FRANCE', 'NORMANDIE', 'NOUVELLE-AQUITAINE', 'OCCITANIE', 'PAYS DE LA LOIRE', ' PACA  ', 'ANTILLES-GUYANE', 'OCEAN INDIEN'],
    'Latitude': [45.75, 47.32, 48.11, 47.9, 48.69, 50.63, 48.85, 49.49, 44.84, 43.6, 47.22, 43.70, 16.24, -20.88], # Lyon, Dijon, Rennes, Orléans, Strasbourg, Lille, Paris, Rouen, Bordeaux, Toulouse, Nantes, Marseille, Basse-Terre, Saint-Denis
    'Longitude': [4.85, 5.04, -1.68, 1.9, 7.75, 3.07, 2.35, 1.10, -0.58, 1.44, -1.55, 5.40, -61.54, 55.45] # Coordonnées approximatives
})

total = df_vie
# Créer une nouvelle colonne dans df_cities qui correspond aux index de la série total
df_cities.set_index('Region', inplace=True)
df_cities['total'] = total

# Remettre l'index à zéro
df_cities.reset_index(inplace=True)
df_cities = df_cities.fillna(0)

# Minimum et maximum de la colonne 'total' 
min_total = df_cities['total'].min()
max_total = df_cities['total'].max()

# Définir une fonction pour obtenir la couleur
def get_color(total):
    if total == 0:  # Si la valeur est nulle, retourner le blanc
        return [255, 255, 255]
    else:
        # Normaliser la valeur de "total" entre 0 et 1
        norm_total = (total - min_total) / (max_total - min_total)
        # Appliquer une échelle quadratique pour exagérer la différence de couleur
        norm_total = norm_total ** 20
        # Mapper cette valeur à une couleur entre rouge (255, 0, 0) et blanc (255, 255, 255)
        r = 255
        g = int(255 * (1 - norm_total))
        b = int(255 * (1 - norm_total))
        return [r, g, b]

# Appliquer la fonction de couleur à la colonne 'total' pour obtenir la couleur de chaque point
df_cities['color'] = df_cities['total'].apply(get_color)

# Création du layer pour la carte
layer = pdk.Layer(
    "ScatterplotLayer",
    df_cities,
    pickable=True,
    opacity=0.8,
    stroked=True,
    filled=True,
    radius_scale=6,
    radius_min_pixels=10,
    radius_max_pixels=100,
    line_width_min_pixels=1,
    get_position=["Longitude", "Latitude"],
    get_radius="total",  # la taille des points dépendra de la somme totale de la proportion des retraités en cumul emploi-retraite
    get_fill_color="color", # Utiliser la couleur définie précédemment
    get_line_color=[0, 0, 0],
)
label_layer = pdk.Layer(
    "TextLayer",
    df_cities,
    pickable=True,
    get_position=["Longitude", "Latitude"],
    get_text="total",  # Les valeurs chiffrées que vous souhaitez afficher
    get_color=[0, 0, 0],
    get_size=15,
    get_alignment_baseline="'bottom'",
)

# Text layer for region names
region_name_layer = pdk.Layer(
    "TextLayer",
    df_cities,
    pickable=False,
    get_position=["Longitude", "Latitude"],
    get_text="Region",
    get_color=[0, 0, 0],
    get_size=16, 
    get_alignment_baseline="'middle'",
)


# Initialiser la vue
view_state = pdk.ViewState(latitude=48.8566, longitude=2.3522, zoom=5, max_zoom=15, pitch=40.5, bearing=-27.36)


# Rendre le deck avec le layer supplémentaire pour les noms de région
r = pdk.Deck(layers=[layer, label_layer, region_name_layer], initial_view_state=view_state)
st.pydeck_chart(r)
st.markdown(
"""
<style>
.color-scale {
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.color-scale > div {
  display: flex;
  align-items: center;
}
.color-scale > div > div {
  width: 24px;
  height: 24px;
  border: 1px solid #ccc;
}
</style>
<div class="color-scale">
  <div>
    <div style="background: rgb(255,0,0);"></div>
    <span>: Valeur maximale (rouge)</span>
  </div>
  <div>
    <div style="background: rgb(255,255,255);"></div>
    <span>: Valeur minimale (blanc)</span>
  </div>
</div>
""",
unsafe_allow_html=True)
# Espace entre les graphiques
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<h4>Tableau de l'espérance de vie à partir de 65 ans par région</h4>", unsafe_allow_html=True)



## Tab esperance
# Trier le dataframe par la colonne "total" en ordre décroissant
df_cities = df_cities.rename(columns={'total': 'Années'})

df_sorted = df_cities.sort_values("Années", ascending=False)

# Afficher le tableau trié
st.table(df_sorted[["Region", "Années"]])