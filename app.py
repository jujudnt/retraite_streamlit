import streamlit as st

st.set_page_config(
    page_title="Analyse retraite France",
    page_icon=":bar_chart:",
    layout="wide",
)

with st.sidebar:
    st.header("Projet")
    st.write("Dashboard Streamlit sur les retraites, les seniors en emploi et les indicateurs regionaux.")
    st.divider()
    st.header("Auteur")
    st.write(
        "[GitHub](https://github.com/jujudnt) · "
        "[LinkedIn](https://www.linkedin.com/in/julia-denat/)"
    )
    


def main():
    st.title("Analyse retraite France")
    st.caption("Dashboard demographique et reglementaire autour de la retraite en France.")

    col1, col2, col3 = st.columns(3)
    col1.metric("Periode historique", "2019-2022")
    col2.metric("Bareme actualise", "2026")
    col3.metric("Format", "Streamlit")

    st.subheader("Sommaire")
    st.markdown(
        """
        - Evolution de la population par region
        - Analyse des retraites et preretraites
        - Repartition des retraites en emploi
        - Taux d'activite et de chomage des seniors
        - Esperance de vie par region
        - Bareme retraite actualise pour les generations 1963 a 1970
        """
    )

    st.info(
        "Les donnees demographiques historiques restent separees du bareme legal "
        "actualise, afin de distinguer l'analyse statistique des regles retraite."
    )

if __name__ == "__main__":
    main()
