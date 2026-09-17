#https://www.data.gouv.fr/fr/datasets/r/85bf035f-733e-4e6d-b591-c865192d0849
import pandas as pd
import numpy as np
import urllib.request
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def df_dept():
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

    mask = df.loc['regions ou département'].eq('departement')
    df_dept = df.loc[:, mask]

    df_dept = df_dept.reset_index()

    return df_dept