"""Vérification du parcours de simulation et des résultats actualisés."""
from pathlib import Path
from streamlit.testing.v1 import AppTest

ROOT = Path(__file__).resolve().parents[1]


def test_accueil_et_menu():
    app = AppTest.from_file(str(ROOT / "app.py")).run()
    assert not app.exception
    assert any(l.label == "Simulation" for l in app.get("page_link"))
    assert len(app.number_input) == 0


def test_premiere_visite_accueil_puis_navigation_libre():
    app = AppTest.from_file(str(ROOT / "app.py")).run()
    del app.session_state["_navigation_initialisee"]
    app.switch_page("views/1_Calculateur.py").run()
    assert not app.exception
    assert len(app.number_input) == 0
    app.switch_page("views/1_Calculateur.py").run()
    assert not app.exception
    assert len(app.number_input) > 0
    app.switch_page("accueil.py").run()
    assert not app.exception
    assert len(app.number_input) == 0


def test_calcul_resultats_et_modification():
    app = AppTest.from_file(str(ROOT / "app.py")).run()
    app.switch_page("views/1_Calculateur.py").run()
    assert not app.exception
    assert len(app.metric) == 0
    next(b for b in app.button if b.label == "Calculer l'indemnité").click().run()
    assert not app.exception
    assert "resultat" in app.session_state
    assert len(app.get("dialog")) == 1
    assert any(m.value == "145 500 FCFA" for m in app.metric)
    next(b for b in app.button if b.label == "Consulter le détail").click().run()
    assert not app.exception
    assert len(app.get("dialog")) == 0
    app.number_input(key="q_Producteur").set_value(1200).run()
    assert not app.exception
    assert "resultat" not in app.session_state
    assert len(app.metric) == 0


def test_surface_nulle_ne_montre_pas_de_resultat():
    app = AppTest.from_file(str(ROOT / "app.py")).run()
    app.switch_page("views/1_Calculateur.py").run()
    app.number_input(key="s_Producteur").set_value(0).run()
    next(b for b in app.button if b.label == "Calculer l'indemnité").click().run()
    assert not app.exception
    assert len(app.error) == 1
    assert "resultat" not in app.session_state
