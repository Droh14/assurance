"""Accueil de l'application PASSIR Calculateur."""
import streamlit as st
from pathlib import Path

from config import APP_NAME
from ui import injecter_style


st.set_page_config(page_title=APP_NAME, layout="wide", initial_sidebar_state="expanded")
injecter_style()

st.markdown("""
<section class="hero">
  <div class="eyebrow">Cacao · Côte d'Ivoire · Projet PASSIR</div>
  <h1>PASSIR Calculateur</h1>
  <p>Comprendre les risques de récolte.<br>Simuler la protection de votre plantation.</p>
</section>
""", unsafe_allow_html=True)

illustration = Path(__file__).resolve().parent / "assets" / "plantation-cacao.png"
if illustration.exists():
    st.image(str(illustration), use_container_width=True)
    st.caption("Illustration générée d'une plantation de cacao en Côte d'Ivoire.")

st.page_link("pages/1_Calculateur.py", label="Simuler mon indemnité", icon="🌱", use_container_width=True)
st.markdown("Du producteur à la coopérative, découvrez comment les rendements de votre territoire interviennent dans l'estimation de votre indemnité.")

st.markdown("<div class='page-kicker'>Parcours guidé</div>", unsafe_allow_html=True)
st.subheader("Une estimation en quelques minutes")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""<article class="workflow-card"><div class="workflow-index">ÉTAPE 01</div><h3>Saisir</h3><p>Quantités et superficies des trois niveaux.</p></article>""", unsafe_allow_html=True)
with col2:
    st.markdown("""<article class="workflow-card"><div class="workflow-index">ÉTAPE 02</div><h3>Comprendre</h3><p>Les rendements révèlent le choc collectif.</p></article>""", unsafe_allow_html=True)
with col3:
    st.markdown("""<article class="workflow-card"><div class="workflow-index">ÉTAPE 03</div><h3>Décider</h3><p>Consultez l'estimation et exportez le détail.</p></article>""", unsafe_allow_html=True)

st.markdown("<div class='note'>Paramètres illustratifs à calibrer sur données réelles.</div>", unsafe_allow_html=True)
st.page_link("pages/1_Calculateur.py", label="Ouvrir le calculateur", use_container_width=True)

st.markdown("<p class='muted'>Projet PASSIR. Filière cacao, six régions du Sud et de l'Ouest de la Côte d'Ivoire.</p>", unsafe_allow_html=True)
