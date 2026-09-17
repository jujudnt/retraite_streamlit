# Analyse Retraite France

Application Streamlit d'exploration des donnees demographiques liees aux
retraites, aux seniors en emploi et aux indicateurs regionaux en France.

Le projet part d'un ancien dashboard Streamlit et le remet a jour avec une
structure plus lisible, des regles retraite actualisees et des tests sur les
calculs metier.

## Fonctionnalites

- evolution de la population par region ;
- analyse des retraites et preretraites ;
- repartition des retraites en emploi ;
- taux d'activite et de chomage des 50-64 ans ;
- esperance de vie par region ;
- synthese des ages legaux et trimestres requis selon les regles applicables a
  partir du 1er septembre 2026.

## Installation

```bash
git clone https://github.com/jujudnt/retraite_streamlit.git
cd retraite_streamlit
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Tests

```bash
PYTHONPATH=src python3 -m unittest discover -s tests
```

## Donnees

Les pages historiques utilisent un fichier Excel issu de data.gouv.fr. La page
"Bareme retraite" utilise un jeu de regles maintenu dans le repository pour
documenter les ages legaux et trimestres requis par generation.

Sources principales :

- Assurance retraite, age legal et trimestres requis :
  https://www.lassuranceretraite.fr/portail-info/home/actif/age-depart/age-depart-retraite.html
- Assurance retraite, mesures retraite 2026 :
  https://www.lassuranceretraite.fr/portail-info/hors-menu/actualites-nationales/actif/2025/projet-de-loi-les-mesures-envisa.html

Ce projet est un outil pedagogique d'exploration. Il ne remplace pas une
estimation personnelle officielle.

