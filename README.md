# PASSIR Calculateur

Application Streamlit en français pour expliquer et simuler le mécanisme d'assurance récolte indicielle cacao du projet PASSIR.

## Installation

Utilisez Python 3.11 puis installez les dépendances :

```powershell
python -m pip install -r requirements.txt
```

## Lancement

```powershell
streamlit run app.py
```

L'application s'ouvre dans le navigateur. La page **Calculateur** contient un exemple chargé depuis le document. La page **Paramètres** permet de modifier les valeurs de la session et de rétablir celles du document.

## Vérification

```powershell
python -m pytest -q
```

## Mise en ligne sur Streamlit Community Cloud

Depuis https://share.streamlit.io/, choisissez **Create app**, le dépôt `Droh14/assurance`, la branche `main` et le fichier principal `app.py`, puis **Deploy**. Les dépendances sont installées à partir de `requirements.txt`.

L'accueil propose un diaporama de campagne avec défilement automatique, navigation manuelle et pause. Le bouton **Menu** reste accessible sur chaque page. Après un calcul, une fenêtre présente la synthèse ; le détail et l'export CSV restent disponibles dans la page. Toute modification des données invalide l'ancien résultat.

## Autre hébergement : Render

1. Créez un dépôt GitHub nommé `passir-calculateur`.
2. Ajoutez les fichiers du projet, notamment le dossier `pages`, le dossier `assets`, le dossier `.streamlit`, `requirements.txt` et `render.yaml`. Ne publiez aucun secret.
3. Dans Render, choisissez **New > Blueprint** et connectez ce dépôt GitHub.
4. Vérifiez le service `passir-calculateur` et son offre `free`, puis lancez le déploiement.
5. À la fin du déploiement, ouvrez et partagez l'adresse HTTPS affichée par Render. Cette adresse permet d'accéder à l'accueil et au calculateur sans installer Python.

Le fichier `render.yaml` définit l'installation, le démarrage et le contrôle de santé. Render doit avoir accès au dépôt. Aucun stockage persistant ou base de données n'est requis : les saisies et paramètres sont propres à la session du visiteur.

Le service gratuit peut se mettre en veille après une période d'inactivité ; le premier accès peut donc prendre plus de temps.

L'illustration de l'accueil est enregistrée dans `assets/plantation-cacao.png` et générée par IA. Elle n'identifie pas une exploitation réelle.

Les paramètres de classes et la prime sont illustratifs. L'outil ne constitue ni une offre commerciale ni un calcul actuariel validé.
