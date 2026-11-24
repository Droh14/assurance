"""Point d'entrée : accueil à l'ouverture, puis navigation libre."""
import streamlit as st

st.set_page_config(
    page_title="PASSIR · Assurance récolte cacao",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="collapsed",
)

accueil = st.Page("accueil.py", title="Accueil", icon="🏡", default=True)
page = st.navigation([
    accueil,
    st.Page("views/1_Calculateur.py", title="Simulation", icon="🌱"),
    st.Page("views/2_Fiche_du_projet.py", title="Le projet", icon="📖"),
    st.Page("views/3_Parametres.py", title="Paramètres", icon="⚙️"),
])

# Une nouvelle visite commence à l'accueil, même depuis un lien de sous-page.
if not st.session_state.get("_navigation_initialisee", False):
    st.session_state["_navigation_initialisee"] = True
    if page.url_path != accueil.url_path:
        st.switch_page(accueil)

page.run()
