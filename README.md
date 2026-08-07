# ✏️ Croquis Converter

Une application web qui transforme n'importe quelle photo en dessin au crayon, en quelques secondes, directement depuis le navigateur.

**Démo en ligne :** *(à ajouter après déploiement, voir plus bas)*

## 🎯 Fonctionnalités

- Upload d'une image (JPG / PNG)
- Génération automatique d'un croquis au crayon avec OpenCV
- Curseur pour régler l'intensité de l'effet
- Comparaison côte à côte "avant / après"
- Téléchargement du résultat en PNG

## 🛠️ Stack technique

- **Python 3**
- **Streamlit** — interface web
- **OpenCV** — traitement d'image
- **Pillow / NumPy** — manipulation des images

## 📁 Structure du projet

```
sketch-converter/
├── app.py              # Application Streamlit
├── requirements.txt    # Dépendances Python
├── .gitignore
└── README.md
```

## 🚀 Reproduire le projet en local

### 1. Cloner le dépôt (une fois qu'il est sur GitHub)

```bash
git clone https://github.com/TON-PSEUDO/sketch-converter.git
cd sketch-converter
```

### 2. Créer un environnement virtuel (recommandé)

```bash
python -m venv venv
source venv/bin/activate      # Sur Windows : venv\Scripts\activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Lancer l'application

```bash
streamlit run app.py
```

L'application s'ouvre automatiquement dans ton navigateur à l'adresse `http://localhost:8501`.

## 📤 Mettre le projet sur GitHub

Depuis le dossier `sketch-converter` :

```bash
git init
git add .
git commit -m "Premier commit : convertisseur de croquis"
git branch -M main
git remote add origin https://github.com/TON-PSEUDO/sketch-converter.git
git push -u origin main
```

(Crée d'abord un dépôt vide sur GitHub avec le nom `sketch-converter`, sans README ni licence, pour éviter les conflits.)

## 🌐 Déployer gratuitement pour obtenir un lien public

C'est l'étape qui te donnera le lien à mettre sur ton portfolio, comme pour le générateur de QR code.

1. Va sur [share.streamlit.io](https://share.streamlit.io) et connecte-toi avec ton compte GitHub.
2. Clique sur **"New app"**.
3. Sélectionne ton dépôt `sketch-converter`, la branche `main`, et le fichier principal `app.py`.
4. Clique sur **"Deploy"**.
5. Après 1 à 2 minutes, Streamlit te donne une URL du type :
   `https://ton-pseudo-sketch-converter.streamlit.app`

C'est ce lien que tu peux directement mettre sur ton portfolio et dans la description de ton dépôt GitHub.

## 💡 Idées d'améliorations (pour aller plus loin)

- Ajouter un mode "cartoon" ou "aquarelle" en plus du crayon
- Ajouter un historique des images traitées dans la session
- Convertir plusieurs images en une fois (traitement par lot)
- Ajouter des tests unitaires sur la fonction `image_to_sketch`

## 📄 Licence

Projet libre d'utilisation à des fins d'apprentissage et de portfolio (licence MIT).
