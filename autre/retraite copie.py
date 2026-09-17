#https://www.data.gouv.fr/fr/datasets/r/85bf035f-733e-4e6d-b591-c865192d0849
import pandas as pd
import numpy as np
import urllib.request
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pydeck as pdk



# URL à charger
url = "https://www.data.gouv.fr/fr/datasets/r/85bf035f-733e-4e6d-b591-c865192d0849"

# Nom de fichier local à charger si l'URL n'est pas disponible
filename = "retraite.xlsx"

try:
    # Vérifier si l'URL est disponible
    urllib.request.urlopen(url)
    # Si l'URL est disponible, charger le contenu du fichier Excel
    data = pd.read_excel(url)
    print('Lecture via l\'URL')
except:
    # Si l'URL n'est pas disponible, charger le contenu du fichier local
    data = pd.read_excel(filename)
    print('Lecture via le fichier')
    
# Définir la chaîne de caractères à rechercher
search_string = "AUVERGNE-\nRHÔNE-ALPES"
# Initialiser un tableau pour stocker les numéros de lignes
start = []

# Parcourir chaque colonne du DataFrame
for col in data.columns:
    # Appliquer une lambda fonction à la colonne pour localiser les numéros de lignes qui contiennent la chaîne de caractères
    line_numbers_in_col = data.index[data[col].apply(lambda x: search_string in str(x))].tolist()
    # Ajouter les numéros de lignes trouvées à la liste
    start += line_numbers_in_col

# Supprimer les doublons des numéros de lignes et trier la liste
start = list(set(start))
start.sort()

# Initialiser un tableau pour stocker les numéros de lignes
end = []

# Parcourir chaque colonne du DataFrame
for col in data.columns:
    # Appliquer une lambda fonction à la colonne pour localiser les numéros de lignes qui commencent par '(1)'
    line_numbers_in_col = data.index[data[col].apply(lambda x: isinstance(x, str) and x.startswith('(1)'))].tolist()
    # Ajouter les numéros de lignes trouvées à la liste
    end += line_numbers_in_col

# Supprimer les doublons des numéros de lignes et trier la liste
end = list(set(end))
end.sort()

# Décomposer le DataFrame en 5 DataFrames différents
dfs = []
for i in range(len(start)):
    dfs.append(data.iloc[start[i]-1:end[i]])

# Renommer les colonnes de chaque DataFrame
for i, df in enumerate(dfs):
    column_names = df.iloc[1]
    df = df[2:]
    df.columns = column_names
    df = df.reset_index(drop=True)
    df = df.rename_axis("", axis=1)
    dfs[i] = df
    dfs[i] = df.rename(columns={df.columns[-1]: "France entière"})

# Assigner chaque DataFrame à une variable
df1, df2, df3, df4, df5 = dfs
df_concat = pd.concat(dfs)
df_concat = df_concat.reset_index(drop=True)
df_concat = df_concat.rename(columns={df_concat.columns[0]: "Designation"})

df_concat['new_designation'] = df_concat['Designation']

for i in range(len(df_concat)-2):
    if 'Espérance de vie à 65 ans en 2021' in df_concat.loc[i, 'Designation']:
        print(i)
        df_concat.loc[i+1, 'new_designation'] = df_concat.loc[i, 'Designation'] + ' ' + df_concat.loc[i+1, 'Designation']
        df_concat.loc[i+2, 'new_designation'] = df_concat.loc[i, 'Designation'] + ' ' + df_concat.loc[i+2, 'Designation']
    if 'Espérance de vie à la naissance en 2021' in df_concat.loc[i, 'Designation']:
        print(i)
        df_concat.loc[i+1, 'new_designation'] = df_concat.loc[i, 'Designation'] + ' ' + df_concat.loc[i+1, 'Designation']
        df_concat.loc[i+2, 'new_designation'] = df_concat.loc[i, 'Designation'] + ' ' + df_concat.loc[i+2, 'Designation']
    if 'Statut d\'emploi et type de contrat des 50 à 64 ans en emploi (en %)' in df_concat.loc[i, 'Designation']:
        print(i)
        df_concat.loc[i+1, 'new_designation'] = df_concat.loc[i, 'Designation'] + ' ' + df_concat.loc[i+1, 'Designation']
        df_concat.loc[i+2, 'new_designation'] = df_concat.loc[i, 'Designation'] + ' ' + df_concat.loc[i+2, 'Designation']
        df_concat.loc[i+3, 'new_designation'] = df_concat.loc[i, 'Designation'] + ' ' + df_concat.loc[i+3, 'Designation']
        df_concat.loc[i+4, 'new_designation'] = df_concat.loc[i, 'Designation'] + ' ' + df_concat.loc[i+4, 'Designation']
        df_concat.loc[i+5, 'new_designation'] = df_concat.loc[i, 'Designation'] + ' ' + df_concat.loc[i+5, 'Designation']
        df_concat.loc[i+6, 'new_designation'] = df_concat.loc[i, 'Designation'] + ' ' + df_concat.loc[i+6, 'Designation']
    if 'Secteur d\'activité des 50 à 64 ans en emploi (en %)' in df_concat.loc[i, 'Designation']:
        print(i)
        df_concat.loc[i+1, 'new_designation'] = df_concat.loc[i, 'Designation'] + ' ' + df_concat.loc[i+1, 'Designation']
        df_concat.loc[i+2, 'new_designation'] = df_concat.loc[i, 'Designation'] + ' ' + df_concat.loc[i+2, 'Designation']
        df_concat.loc[i+3, 'new_designation'] = df_concat.loc[i, 'Designation'] + ' ' + df_concat.loc[i+3, 'Designation']
        df_concat.loc[i+4, 'new_designation'] = df_concat.loc[i, 'Designation'] + ' ' + df_concat.loc[i+4, 'Designation']
        df_concat.loc[i+5, 'new_designation'] = df_concat.loc[i, 'Designation'] + ' ' + df_concat.loc[i+5, 'Designation']
    if 'Catégorie socioprofessionnelle des 50 à 64 ans en emploi (en %)' in df_concat.loc[i, 'Designation']:
        print(i)
        df_concat.loc[i+1, 'new_designation'] = df_concat.loc[i, 'Designation'] + ' ' + df_concat.loc[i+1, 'Designation']
        df_concat.loc[i+2, 'new_designation'] = df_concat.loc[i, 'Designation'] + ' ' + df_concat.loc[i+2, 'Designation']
        df_concat.loc[i+3, 'new_designation'] = df_concat.loc[i, 'Designation'] + ' ' + df_concat.loc[i+3, 'Designation']
        df_concat.loc[i+4, 'new_designation'] = df_concat.loc[i, 'Designation'] + ' ' + df_concat.loc[i+4, 'Designation']
        df_concat.loc[i+5, 'new_designation'] = df_concat.loc[i, 'Designation'] + ' ' + df_concat.loc[i+5, 'Designation']
        df_concat.loc[i+6, 'new_designation'] = df_concat.loc[i, 'Designation'] + ' ' + df_concat.loc[i+6, 'Designation']
    
    if 'Cumul emploi-retraite (en %)' in df_concat.loc[i, 'Designation']:
        print(i)
        df_concat.loc[i+1, 'new_designation'] = df_concat.loc[i, 'Designation'] + ' ' + df_concat.loc[i+1, 'Designation']
        df_concat.loc[i+2, 'new_designation'] = df_concat.loc[i, 'Designation'] + ' ' + df_concat.loc[i+2, 'Designation']
        df_concat.loc[i+3, 'new_designation'] = df_concat.loc[i, 'Designation'] + ' ' + df_concat.loc[i+3, 'Designation']
        df_concat.loc[i+4, 'new_designation'] = df_concat.loc[i, 'Designation'] + ' ' + df_concat.loc[i+4, 'Designation']
    
    if 'Répartition des retraités et préretraités exerçant un emploi selon leur tranche d’âge en %' in df_concat.loc[i, 'Designation']:
        print(i)
        df_concat.loc[i+1, 'new_designation'] = df_concat.loc[i, 'Designation'] + ' ' + df_concat.loc[i+1, 'Designation']
        df_concat.loc[i+2, 'new_designation'] = df_concat.loc[i, 'Designation'] + ' ' + df_concat.loc[i+2, 'Designation']
        df_concat.loc[i+3, 'new_designation'] = df_concat.loc[i, 'Designation'] + ' ' + df_concat.loc[i+3, 'Designation']
        df_concat.loc[i+4, 'new_designation'] = df_concat.loc[i, 'Designation'] + ' ' + df_concat.loc[i+4, 'Designation']
        df_concat.loc[i+5, 'new_designation'] = df_concat.loc[i, 'Designation'] + ' ' + df_concat.loc[i+5, 'Designation']
    if 'Répartition des retraités et préretraités exerçant un emploi selon leur catégorie socioprofessionnelle en %' in df_concat.loc[i, 'Designation']:
        print(i)
        df_concat.loc[i+1, 'new_designation'] = df_concat.loc[i, 'Designation'] + ' ' + df_concat.loc[i+1, 'Designation']
        df_concat.loc[i+2, 'new_designation'] = df_concat.loc[i, 'Designation'] + ' ' + df_concat.loc[i+2, 'Designation']
        df_concat.loc[i+3, 'new_designation'] = df_concat.loc[i, 'Designation'] + ' ' + df_concat.loc[i+3, 'Designation']
        df_concat.loc[i+4, 'new_designation'] = df_concat.loc[i, 'Designation'] + ' ' + df_concat.loc[i+4, 'Designation']        
        df_concat.loc[i+5, 'new_designation'] = df_concat.loc[i, 'Designation'] + ' ' + df_concat.loc[i+5, 'Designation']
        df_concat.loc[i+6, 'new_designation'] = df_concat.loc[i, 'Designation'] + ' ' + df_concat.loc[i+6, 'Designation']
        df_concat.loc[i+7, 'new_designation'] = df_concat.loc[i, 'Designation'] + ' ' + df_concat.loc[i+7, 'Designation']
        df_concat.loc[i+8, 'new_designation'] = df_concat.loc[i, 'Designation'] + ' ' + df_concat.loc[i+8, 'Designation']
        df_concat.loc[i+9, 'new_designation'] = df_concat.loc[i, 'Designation'] + ' ' + df_concat.loc[i+9, 'Designation']
        df_concat.loc[i+10, 'new_designation'] = df_concat.loc[i, 'Designation'] + ' ' + df_concat.loc[i+10, 'Designation']
        df_concat.loc[i+11, 'new_designation'] = df_concat.loc[i, 'Designation'] + ' ' + df_concat.loc[i+11, 'Designation']
        df_concat.loc[i+12, 'new_designation'] = df_concat.loc[i, 'Designation'] + ' ' + df_concat.loc[i+12, 'Designation']
        df_concat.loc[i+13, 'new_designation'] = df_concat.loc[i, 'Designation'] + ' ' + df_concat.loc[i+13, 'Designation']
        df_concat.loc[i+14, 'new_designation'] = df_concat.loc[i, 'Designation'] + ' ' + df_concat.loc[i+14, 'Designation']
        df_concat.loc[i+15, 'new_designation'] = df_concat.loc[i, 'Designation'] + ' ' + df_concat.loc[i+15, 'Designation']
        df_concat.loc[i+16, 'new_designation'] = df_concat.loc[i, 'Designation'] + ' ' + df_concat.loc[i+16, 'Designation']
        df_concat.loc[i+17, 'new_designation'] = df_concat.loc[i, 'Designation'] + ' ' + df_concat.loc[i+17, 'Designation']
        df_concat.loc[i+18, 'new_designation'] = df_concat.loc[i, 'Designation'] + ' ' + df_concat.loc[i+18, 'Designation']


df_concat = df_concat.replace('nd', np.nan)

colonnes_a_convertir = ['AUVERGNE-\nRHÔNE-ALPES',
 'Ain',
 'Allier',
 'Ardèche',
 'Cantal',
 'Drôme',
 'Isère',
 'Loire',
 'Haute-Loire',
 'Puy-de-Dôme',
 'Rhône',
 'Savoie',
 'Haute-Savoie',
 'BOURGOGNE-\nFRANCHE-COMTE',
 "Côte-d'Or",
 'Doubs',
 'Jura',
 'Nièvre',
 'Haute-Saône',
 'Saône-et-Loire',
 'Yonne',
 'Territoire de Belfort',
 'BRETAGNE',
 "Côtes d'Armor",
 'Finistère',
 'Ille-et-Vilaine',
 'Morbihan',
 'CENTRE - \nVAL DE LOIRE',
 'Cher',
 'Eure-et-Loir',
 'Indre',
 'Indre-et-Loire',
 'Loir-et-Cher',
 'Loiret',
 'CORSE',
 'Corse du sud',
 'Haute Corse',
 'GRAND EST',
 'Ardennes',
 'Aube',
 'Marne',
 'Haute-Marne',
 'Meurthe-et-Moselle',
 'Meuse',
 'Moselle',
 'Bas-Rhin',
 'Haut-Rhin',
 'Vosges',
 'HAUTS-DE-FRANCE ',
 'Aisne',
 'Nord',
 'Oise',
 'Pas-de-Calais',
 'Somme',
 'ILE-DE-FRANCE',
 'Paris',
 'Seine-et-Marne',
 'Yvelines',
 'Essonne',
 'Hauts-de-Seine',
 'Seine-Saint-Denis',
 'Val-de-Marne',
 "Val-d'Oise",
 'NORMANDIE',
 'Calvados',
 'Eure',
 'Manche',
 'Orne',
 'Seine-Maritime',
 'NOUVELLE-AQUITAINE',
 'Charente',
 'Charente-Maritime',
 'Corrèze',
 'Creuse',
 'Dordogne',
 'Gironde',
 'Landes',
 'Lot-et-Garonne',
 'Pyrénées-Atlantiques',
 'Deux-Sèvres',
 'Vienne',
 'Haute-Vienne',
 'OCCITANIE',
 'Ariège',
 'Aude',
 'Aveyron',
 'Gard',
 'Haute-Garonne',
 'Gers',
 'Hérault',
 'Lot',
 'Lozère',
 'Hautes-Pyrénées',
 'Pyrénées-Orientales',
 'Tarn',
 'Tarn-et-Garonne',
 'PAYS DE LA LOIRE',
 'Loire-Atlantique',
 'Maine-et-Loire',
 'Mayenne',
 'Sarthe',
 'Vendée',
 ' PACA  ',
 'Alpes-de-Haute-Provence',
 'Hautes-Alpes',
 'Alpes-Maritimes',
 'Bouches-du-Rhône',
 'Var',
 'Vaucluse',
 'France métropolitaine',
 'ANTILLES-GUYANE',
 'Guadeloupe',
 'Martinique',
 'Guyane',
 'OCEAN INDIEN',
 'La Réunion',
 'Mayotte',
 'France entière']

# Convertir les colonnes spécifiées en float
for colonne in colonnes_a_convertir:
    if colonne in df_concat.columns:
        df_concat[colonne] = df_concat[colonne].astype(float)
        
        
# Créer un dictionnaire de colonnes à partir des noms de la première ligne
regions = ['AUVERGNE-\nRHÔNE-ALPES','ILE-DE-FRANCE','BRETAGNE', 'GRAND EST', 'BOURGOGNE-\nFRANCHE-COMTE', 'CENTRE - \nVAL DE LOIRE','HAUTS-DE-FRANCE ', 'NORMANDIE', 'NOUVELLE-AQUITAINE', 'OCCITANIE', 'PAYS DE LA LOIRE', ' PACA  ', 'ANTILLES-GUYANE', 'OCEAN INDIEN'] # Liste des noms de régions


departments_list = []
regions_list = []
# Parcourir tous les noms de colonnes du DataFrame
for col in df_concat.columns:
    # Vérifier si le nom de la colonne est dans la liste des régions
    if col in regions:
        regions_list.append(col)
    else:
        if col not in ['Designation', 'new_designation', 'France entière']:
            departments_list.append(col)

# Filtre pour département ou région
df_dept = pd.DataFrame(departments_list)
df_region = pd.DataFrame(regions_list)

# Créer un dictionnaire avec les valeurs pour la nouvelle ligne
new_row = {'Designation': 'regions ou département'}

# Parcourir chaque colonne du DataFrame
for col in df_concat.columns:
    # Ajouter la valeur de la région correspondante si le nom de la colonne est dans la liste des régions
    if col in regions:
        new_row[col] = 'region'
    # Ajouter la valeur du département correspondant si le nom de la colonne est dans la liste des départements
    elif col in departments_list:
        new_row[col] = 'departement'

# Ajouter la nouvelle ligne au DataFrame
df_concat = df_concat.append(new_row, ignore_index=True)

df = df_concat.set_index('Designation')

mask = df.loc['regions ou département'].eq('region')
df_region = df.loc[:, mask]
mask = df.loc['regions ou département'].eq('departement')
df_dept = df.loc[:, mask]

df_dept = df_dept.reset_index()
df_region = df_region.reset_index()


#2
st.header('Population au 1er janvier 2022 par régions')
pop_2022 = df_region[df_region['Designation'] == 'Population au 1er janvier 2022 (Estimation de population) (1)']
pop_2022 = pop_2022.drop(columns=['Designation']).T
pop_2022.columns = ['Population']
st.bar_chart(pop_2022)

#1
# Sélectionnez les données pour le graphique
st.header('Population au 1er janvier 2019 par régions')

pop_2019 = df_region[df_region['Designation'] == 'Population au 1er janvier 2019 (Recensement de la population)']
pop_2019 = pop_2019.drop(columns=['Designation']).T
pop_2019.columns = ['Population 2019']

pop_2022 = df_region[df_region['Designation'] == 'Population au 1er janvier 2022 (Estimation de population) (1)']
pop_2022 = pop_2022.drop(columns=['Designation']).T
pop_2022.columns = ['Population 2022']

population_data = pop_2019.join(pop_2022)

# calculate the percentage change
population_data['Percentage Change'] = ((population_data['Population 2022'] - population_data['Population 2019']) / population_data['Population 2019']) * 100

st.bar_chart(population_data['Percentage Change'])

#4
# pourcentage de retraités ayant moins de 65 ans
st.header('Pourcentage de retraités ayant moins de 65 ans')
under_65 = df_region[df_region['Designation'] == 'Proportion de moins de 65 ans (en %)']
under_65 = under_65.drop(columns=['Designation']).T
under_65.columns = ['Pourcentage de retraités ayant moins de 65 ans']
st.area_chart(under_65)

#5
st.header('Répartition des retraités et préretraités exerçant un emploi selon leur tranche d’âge')
age_dist = df_concat[df_concat['Designation'].isin(['Moins de 60 ans', '60 à 64 ans', '65 à 69 ans', '70 à 74 ans', '75 ans et plus'])]
age_dist = age_dist.set_index('Designation').T
age_dist = age_dist.loc['France entière']
fig, ax = plt.subplots()
ax.pie(age_dist, labels=age_dist.index, autopct='%1.1f%%')
ax.axis('equal')  # Pour un graphique à secteurs circulaire.
#plt.title('Répartition des retraités et préretraités exerçant un emploi selon leur tranche d’âge')
st.pyplot(fig)


#6
#nb de retraité par région
st.header('Nombre de retraités et pré-retraités en 2019')
retraité_2019 = df_region[df_region['Designation'] == 'Nombre de retraités et préretraités']
retraité_2019 = retraité_2019.drop(columns=['Designation']).T
retraité_2019.columns = ['Nombre']
st.bar_chart(retraité_2019)


#7
# Taux d'activité de la population en 2019
st.header('Taux d\'activité de la population en 2019 par région \n(rapport entre le nombre d\'actifs et la population de 15 à 64 ans en % )')
activity_rate = df_region[df_region['Designation'] == "Taux d'activité de la population en 2019 (rapport entre le nombre d'actifs et la population de 15 à 64 ans en % ) (3)"]
activity_rate = activity_rate.drop(columns='Designation')
activity_rate = activity_rate.apply(pd.to_numeric, errors='coerce')  # Conversion des données en numériques
fig, ax = plt.subplots(figsize=(12,1)) 
sns.heatmap(activity_rate, cmap='YlGnBu', annot=True, fmt=".1f", cbar=False, ax=ax)
#plt.title("Taux d'activité de la population en 2019 par région")
plt.xlabel('Régions')
plt.ylabel('Taux d\'activité')
st.pyplot(plt)

#8
st.header('Espérance de vie à la naissance en 2021')
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


#9
st.header("Taux de chômage des 50 à 64 ans VS part de retraités et préretraités parmi les personnes en emploi(en %)")
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
st.dataframe(df_all)

#10
st.header("Répartition des retraités et préretraités exerçant un emploi")
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
plt.title('Proportion de retraités et préretraités exerçant un emploi par catégorie socioprofessionnelle et par région')
plt.ylabel('Catégorie socioprofessionnelle')
plt.xlabel('Région')

# Afficher la figure avec streamlit
st.pyplot(fig)



#11
st.header("Espérance de vie à 65 ans en 2021")

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


## tab esperance

st.table(df_cities[["Region","total"]])