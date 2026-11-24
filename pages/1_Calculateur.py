import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from calculs import classe_classique, degres_appartenance, indemnisation, prime_contrat, ratio, reference_moyenne_tronquee, rendement
from config import ACTEURS, ALPHA_DEFAUT, ANNEES_CONTRAT, ARRONDI_AFFICHAGE, CENTRES_DEFAUT, CLASSES, EXEMPLE, EXPOSANT_DEFAUT, PAIEMENTS_DEFAUT, POIDS_DEFAUT, RATIOS_COURBE, RENDEMENT_REFERENCE_DEFAUT
from ui import injecter_style


injecter_style()
st.markdown("<div class='page-kicker'>Simulation guidée</div>", unsafe_allow_html=True)
st.title("Calculateur d'indemnité")
st.caption("Renseignez les données de campagne. Les montants sont des estimations pédagogiques, non une offre d'assurance.")

def parametres():
    return st.session_state.get("parametres", {"centres": CENTRES_DEFAUT, "poids": POIDS_DEFAUT, "exposant": EXPOSANT_DEFAUT, "alpha": ALPHA_DEFAUT, "paiements": PAIEMENTS_DEFAUT})

def monnaie(montant):
    return f"{round(montant, ARRONDI_AFFICHAGE):,.0f} FCFA".replace(",", " ")

def valeurs_exemple():
    for acteur in ACTEURS:
        st.session_state[f"q_{acteur}"] = EXEMPLE["quantites"][acteur]
        st.session_state[f"s_{acteur}"] = EXEMPLE["superficies"][acteur]
        st.session_state[f"r_{acteur}"] = EXEMPLE["reference"]
    st.session_state["assuree"] = EXEMPLE["assuree"]
    st.session_state["annee"] = EXEMPLE["annee"]

if st.button("Charger l'exemple du document"):
    valeurs_exemple()
    st.rerun()

if "q_Producteur" not in st.session_state:
    valeurs_exemple()

advanced = st.toggle("Mode avancé : calculer la référence avec cinq campagnes", value=False)
donnees, references = {}, {}

for acteur in ACTEURS:
    with st.expander(acteur, expanded=True):
        c1, c2, c3 = st.columns(3)
        quantite = c1.number_input("Quantité livrée et enregistrée (kg)", min_value=0.0, step=100.0, key=f"q_{acteur}")
        superficie = c2.number_input("Superficie productive (ha)", min_value=0.0, step=0.1, key=f"s_{acteur}")
        if advanced:
            lignes = []
            st.caption("Cinq campagnes passées. La meilleure et la moins bonne seront retirées.")
            cols = st.columns(5)
            for i, col in enumerate(cols, start=1):
                with col:
                    q = st.number_input(f"Campagne {i} kg", min_value=0.0, value=RENDEMENT_REFERENCE_DEFAUT, key=f"histq_{acteur}_{i}")
                    s = st.number_input(f"Campagne {i} ha", min_value=0.01, value=1.0, key=f"hists_{acteur}_{i}")
                    lignes.append((q, s))
            try:
                reference = reference_moyenne_tronquee(lignes)
                c3.metric("Référence calculée", f"{reference:,.1f} kg/ha".replace(",", " "))
            except ValueError as erreur:
                c3.error(str(erreur))
                reference = 0.0
        else:
            reference = c3.number_input("Rendement de référence (kg/ha)", min_value=0.01, step=10.0, key=f"r_{acteur}")
        donnees[acteur] = (quantite, superficie)
        references[acteur] = reference

st.subheader("Contrat")
c1, c2 = st.columns(2)
superficie_assuree = c1.number_input("Superficie assurée du producteur (ha)", min_value=0.01, step=0.1, key="assuree")
annee = c2.selectbox("Année du contrat", ANNEES_CONTRAT, key="annee")

if st.button("Calculer l'indemnité", type="primary", use_container_width=True):
    try:
        ratios = {acteur: ratio(*donnees[acteur], references[acteur]) for acteur in ACTEURS}
        params = parametres()
        resultat = indemnisation(ratios, superficie_assuree, **params)
        prime = prime_contrat(superficie_assuree, annee, resultat["indemnite_totale"])
        st.session_state.resultat = {"ratios": ratios, "donnees": donnees, "references": references, "contrat": (superficie_assuree, annee), "calcul": resultat, "prime": prime, "params": params}
    except ValueError as erreur:
        st.error(str(erreur))

if "resultat" in st.session_state:
    data = st.session_state.resultat
    ratios, result, prime, params = data["ratios"], data["calcul"], data["prime"], data["params"]
    moyenne = sum(ratios[a] * params["poids"][a] for a in ACTEURS)
    phrase = "Aucune indemnité : la récolte est proche de la normale." if not result["seuil_atteint"] else "Une indemnité est estimée selon les trois niveaux de rendement."
    st.divider()
    a, b, c = st.columns(3)
    a.metric("Indemnité totale", monnaie(result["indemnite_totale"]))
    b.metric("Indemnité par hectare", monnaie(result["indemnite_ha"]))
    c.metric("Gain net après prime", monnaie(prime["gain_net"]))
    st.success(phrase)

    with st.expander("1. Rendements et ratios", expanded=True):
        rows = []
        for acteur in ACTEURS:
            q, s = data["donnees"][acteur]
            rend = rendement(q, s)
            rows.append({"Acteur": acteur, "Quantité (kg)": q, "Superficie (ha)": s, "Rendement (kg/ha)": rend, "Référence (kg/ha)": data["references"][acteur], "Ratio": ratios[acteur]})
        st.dataframe(pd.DataFrame(rows).style.format({"Quantité (kg)": "{:,.0f}", "Superficie (ha)": "{:,.2f}", "Rendement (kg/ha)": "{:,.2f}", "Référence (kg/ha)": "{:,.2f}", "Ratio": "{:.3f}"}), use_container_width=True, hide_index=True)
        st.caption("Formule : ratio = (quantité ÷ superficie) ÷ rendement de référence.")

    with st.expander("2. Écarts et distances aux centres"):
        table = pd.DataFrame({"Classe": list(CLASSES), "Centre": [params["centres"][c] for c in CLASSES], "Distance pondérée": [result["distances"][c] for c in CLASSES]})
        st.dataframe(table.style.format({"Centre": "{:.2f}", "Distance pondérée": "{:.4f}"}), use_container_width=True, hide_index=True)
        st.caption("Distance = racine de la somme des poids multipliés par les écarts au carré.")

    with st.expander("3. Degrés d'appartenance"):
        degres = result["degres"]
        frame = pd.DataFrame({"Classe": list(CLASSES), "Degré": [degres[c] for c in CLASSES], "Paiement par ha": [params["paiements"][c] for c in CLASSES]})
        st.dataframe(frame.style.format({"Degré": "{:.3f}", "Paiement par ha": "{:,.0f}"}), use_container_width=True, hide_index=True)
        st.bar_chart(frame.set_index("Classe")["Degré"], color="#f77d00")

    with st.expander("4. Seuil, paiement et prime", expanded=True):
        st.write(f"Test du seuil alpha = {params['alpha']:.2f} : {'au moins une classe indemnisable atteint le seuil' if result['seuil_atteint'] else 'les classes C1, C2 et C3 restent toutes sous le seuil'}.")
        lignes = pd.DataFrame({"Classe": list(CLASSES), "Degré": [result["degres"][c] for c in CLASSES], "Paiement (FCFA/ha)": [params["paiements"][c] for c in CLASSES], "Contribution (FCFA/ha)": [result["degres"][c] * params["paiements"][c] if result["seuil_atteint"] else 0 for c in CLASSES]})
        st.dataframe(lignes.style.format({"Degré": "{:.3f}", "Paiement (FCFA/ha)": "{:,.0f}", "Contribution (FCFA/ha)": "{:,.0f}"}), use_container_width=True, hide_index=True)
        st.write(f"Indemnité totale : {monnaie(result['indemnite_ha'])} × {data['contrat'][0]:.2f} ha = {monnaie(result['indemnite_totale'])}.")
        st.write(f"Prime commerciale : {monnaie(prime['prime_totale'])}. Part du producteur : {monnaie(prime['part_producteur'])}. Part de l'État : {monnaie(prime['part_etat'])}.")

    st.subheader("Flou ou classique")
    ratios_courbe = np.arange(*RATIOS_COURBE)
    flou, classique = [], []
    for r in ratios_courbe:
        commun = {acteur: r for acteur in ACTEURS}
        flou.append(indemnisation(commun, 1, **params)["indemnite_ha"])
        classique.append(classe_classique(commun, params["centres"], params["poids"], params["paiements"])[1])
    figure = go.Figure()
    figure.add_scatter(x=ratios_courbe, y=flou, mode="lines", name="Classification floue", line={"color": "#f77d00", "width": 4})
    figure.add_scatter(x=ratios_courbe, y=classique, mode="lines", name="Classification classique", line={"color": "#009a44", "dash": "dot"})
    figure.add_vline(x=moyenne, line_dash="dash", line_color="#10251d", annotation_text="Moyenne pondérée observée")
    figure.update_layout(template="plotly_white", xaxis_title="Ratio commun hypothétique", yaxis_title="Indemnité par hectare (FCFA)", height=400, margin={"l": 10, "r": 10, "t": 20, "b": 10})
    st.plotly_chart(figure, use_container_width=True)
    st.caption("Hypothèse du graphique : les trois ratios sont égaux. Le trait indique la moyenne pondérée des ratios réellement saisis.")

    export = pd.DataFrame([{"acteur": a, "quantite_kg": data["donnees"][a][0], "superficie_ha": data["donnees"][a][1], "reference_kg_ha": data["references"][a], "ratio": ratios[a]} for a in ACTEURS])
    export["indemnite_ha_fcfa"] = result["indemnite_ha"]
    export["indemnite_totale_fcfa"] = result["indemnite_totale"]
    st.download_button("Télécharger le détail en CSV", export.to_csv(index=False).encode("utf-8-sig"), "detail_passir.csv", "text/csv")
