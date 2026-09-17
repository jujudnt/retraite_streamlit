import sys
from pathlib import Path

import streamlit as st

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from retraite_rules import legal_age_for_birth_year, retirement_rules_records


st.set_page_config(page_title="Bareme retraite 2026", page_icon=":calendar:", layout="wide")

st.title("Bareme retraite 2026")
st.caption("Synthese des ages legaux et trimestres requis applicables aux retraites prenant effet a partir du 1er septembre 2026.")

with st.sidebar:
    st.header("Simulation rapide")
    birth_year = st.number_input("Annee de naissance", min_value=1963, max_value=1970, value=1968)
    birth_month = st.slider("Mois de naissance", 1, 12, 1)

rule = legal_age_for_birth_year(int(birth_year), int(birth_month))

col1, col2 = st.columns(2)
col1.metric("Age legal", rule.legal_age)
col2.metric("Trimestres requis", rule.required_quarters)

if rule.note:
    st.info(rule.note)

st.subheader("Table de reference")
st.dataframe(retirement_rules_records(), hide_index=True, use_container_width=True)

st.subheader("Notes")
st.markdown(
    """
    - Ces dispositions concernent les retraites prenant effet a compter du 1er septembre 2026.
    - Jusqu'au 1er septembre 2026, la legislation precedente continue de s'appliquer.
    - La page ne traite pas les situations particulieres : handicap, invalidite, categorie active, carriere longue complete ou regimes speciaux.
    """
)

st.caption(
    "Source : Assurance retraite, article mis a jour le 13/05/2026 sur les mesures retraite du PLFSS 2026."
)
