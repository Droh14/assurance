"""Calculs purs du mécanisme d'assurance récolte indicielle PASSIR."""
from __future__ import annotations

from math import sqrt
from typing import Mapping

from config import ACTEURS, ALPHA_DEFAUT, CENTRES_DEFAUT, CLASSES, EXPOSANT_DEFAUT, PAIEMENTS_DEFAUT, PART_PRODUCTEUR, POIDS_DEFAUT, PRIME_COMMERCIALE_HA, SUBVENTION_ETAT


def valider_positif(valeur: float, nom: str, strict: bool = False) -> None:
    if (valeur <= 0) if strict else (valeur < 0):
        comparateur = "strictement positif" if strict else "positif ou nul"
        raise ValueError(f"{nom} doit être {comparateur}.")


def rendement(quantite: float, superficie: float) -> float:
    valider_positif(quantite, "La quantité")
    valider_positif(superficie, "La superficie", strict=True)
    return quantite / superficie


def ratio(quantite: float, superficie: float, reference: float) -> float:
    valider_positif(reference, "Le rendement de référence", strict=True)
    return rendement(quantite, superficie) / reference


def reference_moyenne_tronquee(campagnes: list[tuple[float, float]]) -> float:
    """Moyenne des rendements hors meilleur et pire, sur au moins 3 campagnes."""
    if len(campagnes) < 3:
        raise ValueError("Au moins trois campagnes sont nécessaires.")
    rendements = sorted(rendement(qte, sup) for qte, sup in campagnes)
    return sum(rendements[1:-1]) / len(rendements[1:-1])


def distances(ratios: Mapping[str, float], centres: Mapping[str, float] = CENTRES_DEFAUT, poids: Mapping[str, float] = POIDS_DEFAUT) -> dict[str, float]:
    _valider_ratios_poids(ratios, poids)
    return {classe: sqrt(sum(poids[acteur] * (ratios[acteur] - centre) ** 2 for acteur in ACTEURS)) for classe, centre in centres.items()}


def degres_appartenance(ratios: Mapping[str, float], centres: Mapping[str, float] = CENTRES_DEFAUT, poids: Mapping[str, float] = POIDS_DEFAUT, exposant: float = EXPOSANT_DEFAUT) -> dict[str, float]:
    """Degrés FCM avec les deux cas extrêmes retenus dans le document."""
    _valider_ratios_poids(ratios, poids)
    if exposant <= 1:
        raise ValueError("L'exposant de flou doit être supérieur à 1.")
    valeurs = list(ratios.values())
    if all(x <= centres["C1"] for x in valeurs):
        return {classe: float(classe == "C1") for classe in CLASSES}
    if all(x >= centres["C4"] for x in valeurs):
        return {classe: float(classe == "C4") for classe in CLASSES}
    dists = distances(ratios, centres, poids)
    zeros = [classe for classe, dist in dists.items() if dist == 0]
    if zeros:
        return {classe: float(classe == zeros[0]) for classe in CLASSES}
    puissance = 2 / (exposant - 1)
    return {classe: 1 / sum((dists[classe] / autre) ** puissance for autre in dists.values()) for classe in CLASSES}


def indemnisation(ratios: Mapping[str, float], superficie_assuree: float, centres: Mapping[str, float] = CENTRES_DEFAUT, poids: Mapping[str, float] = POIDS_DEFAUT, exposant: float = EXPOSANT_DEFAUT, alpha: float = ALPHA_DEFAUT, paiements: Mapping[str, float] = PAIEMENTS_DEFAUT) -> dict:
    valider_positif(superficie_assuree, "La superficie assurée", strict=True)
    if not 0 <= alpha <= 1:
        raise ValueError("Le seuil alpha doit être entre 0 et 1.")
    dists = distances(ratios, centres, poids)
    degres = degres_appartenance(ratios, centres, poids, exposant)
    seuil_atteint = any(degres[c] >= alpha for c in ("C1", "C2", "C3"))
    montant_ha = sum(degres[c] * paiements[c] for c in CLASSES) if seuil_atteint else 0.0
    return {"distances": dists, "degres": degres, "seuil_atteint": seuil_atteint, "indemnite_ha": montant_ha, "indemnite_totale": montant_ha * superficie_assuree}


def prime_contrat(superficie_assuree: float, annee: int, indemnite_totale: float) -> dict:
    valider_positif(superficie_assuree, "La superficie assurée", strict=True)
    if annee not in PART_PRODUCTEUR:
        raise ValueError("L'année du contrat doit être 2027, 2028 ou 2029.")
    prime_totale = PRIME_COMMERCIALE_HA * superficie_assuree
    part_producteur = PART_PRODUCTEUR[annee] * superficie_assuree
    return {"prime_totale": prime_totale, "part_producteur": part_producteur, "part_etat": prime_totale - part_producteur, "taux_subvention": SUBVENTION_ETAT[annee], "gain_net": indemnite_totale - part_producteur}


def classe_classique(ratios: Mapping[str, float], centres: Mapping[str, float] = CENTRES_DEFAUT, poids: Mapping[str, float] = POIDS_DEFAUT, paiements: Mapping[str, float] = PAIEMENTS_DEFAUT) -> tuple[str, float]:
    dists = distances(ratios, centres, poids)
    classe = min(dists, key=dists.get)
    return classe, paiements[classe]


def _valider_ratios_poids(ratios: Mapping[str, float], poids: Mapping[str, float]) -> None:
    if set(ratios) != set(ACTEURS):
        raise ValueError("Les trois ratios sont requis.")
    if set(poids) != set(ACTEURS) or abs(sum(poids.values()) - 1) > 1e-9:
        raise ValueError("Les poids des trois acteurs doivent totaliser 1.")
