"""Accueil de PASSIR, au rythme de la campagne cacao."""
import streamlit as st
from carousel import afficher_campagne
from ui import injecter_style

injecter_style()
st.markdown("""<div class="brand-line"><div class="brand-mark">P</div><div>
<div class="brand-title">PASSIR</div><div class="brand-subtitle">Assurance récolte · Côte d'Ivoire</div>
</div></div>""", unsafe_allow_html=True)
afficher_campagne()
intro, action = st.columns([3, 1], vertical_alignment="center")
with intro:
    st.markdown("<div class='page-kicker'>Votre campagne, en perspective</div>", unsafe_allow_html=True)
    st.subheader("Anticiper. Comprendre. Avancer.")
    st.write("Reliez les rendements de votre plantation à ceux de votre coopérative et de votre département pour estimer votre indemnité récolte.")
with action:
    st.page_link("views/1_Calculateur.py", label="Simuler mon indemnité", icon="🌱", use_container_width=True)
for col, numero, titre, texte in zip(st.columns(3), ("01", "02", "03"),
        ("Votre récolte", "Votre territoire", "Votre estimation"),
        ("Renseignez les quantités et les surfaces de la campagne.",
         "Comparez les rendements aux références des trois niveaux.",
         "Consultez votre indemnité, votre cotisation et le détail du calcul.")):
    with col:
        st.markdown(f"<article class='workflow-card'><div class='workflow-index'>{numero}</div><h3>{titre}</h3><p>{texte}</p></article>", unsafe_allow_html=True)
st.caption("Nawa · San-Pédro · Gbôklé · Cavally · Guémon · Tonkpi")
st.caption("Montants estimatifs selon les paramètres du modèle. Visuels de campagne créés par IA.")
