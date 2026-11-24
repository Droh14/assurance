import streamlit as st

from config import ALPHA_DEFAUT, CENTRES_DEFAUT, CLASSES, EXPOSANT_DEFAUT, PAIEMENTS_DEFAUT, POIDS_DEFAUT
from ui import injecter_style


injecter_style()
st.markdown("<div class='page-kicker'>Réglages de la session</div>", unsafe_allow_html=True)
st.title("Paramètres du modèle")
st.caption("Ajustez les paramètres utilisés pour vos simulations. Les modifications s'appliquent à votre session.")

def defaults():
    return {"centres": CENTRES_DEFAUT.copy(), "poids": POIDS_DEFAUT.copy(), "exposant": EXPOSANT_DEFAUT, "alpha": ALPHA_DEFAUT, "paiements": PAIEMENTS_DEFAUT.copy()}

if "parametres" not in st.session_state:
    st.session_state.parametres = defaults()

if st.button("Rétablir les paramètres par défaut"):
    st.session_state.parametres = defaults()
    st.rerun()

param = st.session_state.parametres
with st.form("form_parametres"):
    st.subheader("Centres des classes")
    cols = st.columns(len(CLASSES))
    centres = {}
    for col, classe in zip(cols, CLASSES):
        centres[classe] = col.number_input(classe, min_value=0.0, value=float(param["centres"][classe]), step=0.01, format="%.2f")

    st.subheader("Poids des trois niveaux")
    cols = st.columns(3)
    poids = {acteur: col.number_input(acteur, min_value=0.0, max_value=1.0, value=float(param["poids"][acteur]), step=0.05, format="%.2f") for col, acteur in zip(cols, POIDS_DEFAUT)}
    col1, col2 = st.columns(2)
    exposant = col1.number_input("Exposant de flou m", min_value=1.01, value=float(param["exposant"]), step=0.10)
    alpha = col2.number_input("Seuil d'appartenance alpha", min_value=0.0, max_value=1.0, value=float(param["alpha"]), step=0.01, format="%.2f")

    st.subheader("Paiement par hectare assuré")
    cols = st.columns(len(CLASSES))
    paiements = {classe: col.number_input(f"{classe} en FCFA", min_value=0.0, value=float(param["paiements"][classe]), step=1000.0) for col, classe in zip(cols, CLASSES)}
    sauvegarder = st.form_submit_button("Enregistrer les paramètres")

if sauvegarder:
    if abs(sum(poids.values()) - 1) > 0.000001:
        st.error("Les poids doivent totaliser 1.")
    elif list(centres.values()) != sorted(centres.values()):
        st.error("Les centres doivent être classés de C1 à C4.")
    else:
        st.session_state.parametres = {"centres": centres, "poids": poids, "exposant": exposant, "alpha": alpha, "paiements": paiements}
        st.success("Paramètres enregistrés pour cette session.")
