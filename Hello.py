import streamlit as st

st.set_page_config(
    page_title="Welcome",
    page_icon="👋",
)

st.header("# Welcome ! 👋")

st.sidebar.success("Welcome 👋")
# Side bar
with st.sidebar:
    st.header('Informations sur l\'auteur')
    st.write(
    """*Julia Denat* 
    [<img src='https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png' width='30'>](https://github.com/jujudnt)
     @jujudnt""",
    unsafe_allow_html=True
)
    st.write('📈Bnp Paribas Cardif | Data Management student🏫') 
    st.write("""<div style="width:100%;text-align:center;"><a href="https://www.linkedin.com/in/julia-denat/" style="float:center"><img src="https://img.shields.io/badge/Julia%20Denat-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&link=https://www.linkedin.com/in/julia-denat/%22" width="100%" height="50%"></img></a></div>""", unsafe_allow_html=True)
    


def main():
    st.title("Analyse démographique et des retraités en France :older_man::older_woman:")
    
    st.markdown(
        """
        ## Sommaire :bookmark_tabs:
        
        Bienvenue à notre analyse interactive! Nous avons préparé pour vous une série de visualisations détaillées. 

        Voici une liste de ce que vous pouvez explorer:
        
        - :bar_chart: Evolution de la population entre 2019 et 2022
        - :busts_in_silhouette: Analyse du nombre de retraités et préretraités
        - :briefcase: Répartition des retraités et préretraités exerçant un emploi
        - :chart_with_upwards_trend: Taux de chômage et d'activité des retraités et préretraités par région
        - :baby::boy::man::older_man: Espérance de vie de la population par région
        
        Amusez-vous à explorer les données!
        """
    )

if __name__ == "__main__":
    main()
