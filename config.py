"""Paramètres par défaut du modèle PASSIR.

Les valeurs signalées comme illustratives doivent être calibrées sur des données réelles.
"""

APP_NAME = "PASSIR Calculateur"
DEVISE = "FCFA"
CENTRES_DEFAUT = {"C1": 0.45, "C2": 0.65, "C3": 0.80, "C4": 1.00}
POIDS_DEFAUT = {"Producteur": 0.25, "Coopérative": 0.50, "Département": 0.25}
EXPOSANT_DEFAUT = 2.0
ALPHA_DEFAUT = 0.20
PAIEMENTS_DEFAUT = {"C1": 250_000.0, "C2": 100_000.0, "C3": 25_000.0, "C4": 0.0}
PRIME_COMMERCIALE_HA = 25_000.0
PART_PRODUCTEUR = {2027: 7_500.0, 2028: 10_000.0, 2029: 12_500.0}
SUBVENTION_ETAT = {2027: 0.70, 2028: 0.60, 2029: 0.50}
RENDEMENT_REFERENCE_DEFAUT = 550.0
ANNEES_CONTRAT = tuple(PART_PRODUCTEUR)
CLASSES = tuple(CENTRES_DEFAUT)
ACTEURS = tuple(POIDS_DEFAUT)
NB_CAMPAGNES_HISTORIQUE = 5
ARRONDI_AFFICHAGE = -2
RATIOS_COURBE = (0.35, 1.05, 0.01)
EXEMPLE = {
    "quantites": {"Producteur": 1100.0, "Coopérative": 173250.0, "Département": 24750000.0},
    "superficies": {"Producteur": 2.5, "Coopérative": 450.0, "Département": 60000.0},
    "reference": 550.0,
    "assuree": 2.5,
    "annee": 2027,
}
