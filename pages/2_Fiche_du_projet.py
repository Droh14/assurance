import pandas as pd
import streamlit as st

from ui import injecter_style


injecter_style()
st.markdown("<div class='page-kicker'>Repères du programme</div>", unsafe_allow_html=True)
st.title("Fiche du projet PASSIR")
st.caption("Une lecture simple du programme de gestion des risques agricoles et de résilience des producteurs de cacao.")

sections = [
    ("Le problème", "L'État garantit le prix du cacao, passé de 2 800 à 1 200 FCFA/kg, mais pas la quantité récoltée. La récolte nationale est passée de 2,3 millions de tonnes en 2022/23 à 1,76 million en 2023/24, soit environ 24 % de moins, sous l'effet du climat. Un planteur qui perd 30 % de sa récolte perd 30 % de son revenu. Il n'existe pas d'assurance récolte cacao et les producteurs restent peu organisés. La zone couvre la Nawa, San-Pédro, le Gbôklé, le Cavally, le Guémon et le Tonkpi."),
    ("Pourquoi l'État intervient", "Le marché fait face à l'information asymétrique, au risque covariant, au besoin de données collectives et à une demande insuffisante. L'assurance indicielle subventionnée est retenue car le coût est partagé, la subvention diminue dans le temps, le paiement est rapide et la fraude est faible. Les petites pertes restent au producteur, les pertes modérées à sévères vont à l'assurance et les catastrophes nationales à l'État, notamment via l'African Risk Capacity."),
    ("La solution", "Une assurance indicielle utilise un indice observable par tous au lieu d'expertiser chaque parcelle. Sous un seuil, les assurés concernés sont payés automatiquement. Le risque de base demeure : l'indice peut différer de la perte réelle d'une parcelle."),
    ("L'indice de rendement", "Le rendement couvre les chocs collectifs : sécheresse, excès de pluie, harmattan et pourriture brune. Les cartes producteurs sont obligatoires depuis 2026-2027 et les parcelles sont géolocalisées. Ratio = rendement ÷ référence. La référence est la moyenne des cinq dernières campagnes, sans la meilleure ni la pire. Un ratio de 1 signifie une année normale ; 0,6 signifie une récolte inférieure de 40 %."),
    ("La classification floue", "Les seuils rigides créent des ruptures injustes. La méthode floue attribue à chaque situation un degré de 0 à 1 dans quatre classes. Elle combine les ratios producteur, coopérative et département avec des poids de 25 %, 50 % et 25 %. Le poids collectif limite la fraude. Le seuil alpha évite les petits paiements. Les centres et pondérations définissent le modèle ; le risque de base doit être suivi."),
    ("Le calcul du paiement", "Le calculateur suit six étapes : rendements, ratios, distances aux centres, degrés d'appartenance, test du seuil et paiement. Dans l'exemple, les ratios 0,80, 0,70 et 0,75 donnent des degrés proches de 0,038, 0,344, 0,573 et 0,046, puis environ 58 200 FCFA par hectare."),
    ("Le contrat", "Le capital assuré est de 250 000 FCFA/ha, soit environ 38 % d'une récolte normale de 660 000 FCFA/ha. La prime est de 25 000 FCFA/ha. La souscription a lieu d'avril à juillet en coopérative. La campagne va d'octobre à septembre. Le paiement est automatique par mobile money dans les 60 jours après la campagne. Sont exclus le risque de prix, le vol et le dépérissement progressif du verger."),
    ("Limites à connaître", "Les centres et pondérations nécessitent une calibration. La prime de 10 % n'est pas issue d'un calcul actuariel. L'historique de rendement est court. Le dispositif dépend aussi du prix garanti. Le poids individuel de 25 % laisse un risque de base. La conformité au Code CIMA reste à confirmer."),
]
for titre, texte in sections:
    with st.expander(titre):
        st.write(texte)

st.subheader("Budget-programme P-GRA")
budget = pd.DataFrame([
    ["A1", "Organisation des producteurs et éducation financière", 2407.4],
    ["A2", "Conception et distribution du produit", 1417.5],
    ["A3", "Subvention des primes", 4906.3],
    ["A4", "Mesure des rendements et données", 1151.0],
    ["A5", "Pilotage et suivi-évaluation", 1993.5],
], columns=["Action", "Contenu", "Millions FCFA"])
st.dataframe(budget.style.format({"Millions FCFA": "{:,.1f}"}), use_container_width=True, hide_index=True)
st.write("Total : 11 875,7 millions de FCFA. Objectif fin 2029 : 75 000 producteurs et 187 500 hectares assurés.")

st.subheader("Chaîne de résultats")
st.markdown("**Intrants** : financement, données de rendement, équipes et cadre réglementaire.  \n**Activités** : organiser, former, mesurer, distribuer et subventionner.  \n**Extrants** : coopératives actives, contrats distribués, références validées et paiements suivis.  \n**Effets** : producteurs protégés, revenus plus résilients et confiance renforcée.  \n**Impact** : filière cacao plus résiliente face aux chocs climatiques.")

st.subheader("Indicateurs et cibles")
indicateurs = pd.DataFrame({"Indicateur": ["Producteurs assurés", "Hectares assurés", "Coopératives", "Risque de base maximal", "Délai maximal d'indemnisation"], "2027": ["20 000", "50 000", "150", "", ""], "2028": ["45 000", "112 500", "320", "15 %", "60 jours"], "2029": ["75 000", "187 500", "500", "10 %", "45 jours"]})
st.dataframe(indicateurs, use_container_width=True, hide_index=True)

st.subheader("Financement")
st.write("Le coût est de 3 472,6, puis 3 728,0, puis 4 675,1 millions de FCFA entre 2027 et 2029. La BOAD finance 65 % soit 7 719,2 millions, le Trésor 25 % soit 2 968,9 millions et le Conseil du Café-Cacao 10 % soit 1 187,6 millions. Les producteurs paient en plus 3 843,8 millions de primes hors budget. L'État subventionne les primes, il ne paie pas les indemnités. Sa dépense annuelle maximale reste sous 0,03 % du budget de l'État.")
