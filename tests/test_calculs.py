import pytest

from calculs import degres_appartenance, indemnisation, ratio, reference_moyenne_tronquee, rendement


@pytest.mark.parametrize("r, attendu", [(0.40, 250000), (0.54, 175100), (0.56, 146300), (0.62, 101800), (0.72, 71700), (0.73, 61800), (0.85, 29600), (0.89, 26700), (0.91, 21000), (0.95, 0)])
def test_indemnites_ratios_egaux(r, attendu):
    result = indemnisation({"Producteur": r, "Coopérative": r, "Département": r}, 1)
    assert result["indemnite_ha"] == pytest.approx(attendu, abs=100)


@pytest.mark.parametrize("valeurs, attendu", [((.80, .70, .75), 58200), ((.50, .85, .90), 63600), ((.95, .55, .60), 96700), ((.50, .55, .60), 158800), ((1.00, .98, 1.02), 0)])
def test_indemnites_trios(valeurs, attendu):
    ratios = dict(zip(("Producteur", "Coopérative", "Département"), valeurs))
    assert indemnisation(ratios, 1)["indemnite_ha"] == pytest.approx(attendu, abs=100)


def test_degres_totalisent_un():
    assert sum(degres_appartenance({"Producteur": .8, "Coopérative": .7, "Département": .75}).values()) == pytest.approx(1)


def test_distance_nulle():
    degres = degres_appartenance({"Producteur": .65, "Coopérative": .65, "Département": .65})
    assert degres == {"C1": 0., "C2": 1., "C3": 0., "C4": 0.}


def test_quantite_nulle():
    assert rendement(0, 2) == 0
    assert ratio(0, 2, 550) == 0


def test_reference_moyenne_tronquee():
    assert reference_moyenne_tronquee([(100, 1), (200, 1), (300, 1), (400, 1), (500, 1)]) == 300


def test_superficie_invalide():
    with pytest.raises(ValueError):
        rendement(100, 0)
