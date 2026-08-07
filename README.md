# ✏️ Croquis Converter

Une application web qui transforme n'importe quelle photo en dessin au crayon, en quelques secondes, directement depuis le navigateur.

**Démo en ligne :** https://zdf-sketch-converter.streamlit.app

## Fonctionnalités

- Upload d'une image (JPG / PNG)
- Génération automatique d'un croquis au crayon avec OpenCV
- Curseur pour régler l'intensité de l'effet
- Comparaison côte à côte "avant / après"
- Téléchargement du résultat en PNG

## Stack technique

- **Python 3**
- **Streamlit** — interface web
- **OpenCV** — traitement d'image
- **Pillow / NumPy** — manipulation des images

## Structure du projet

```
sketch-converter/
├── app.py              # Application Streamlit
├── requirements.txt    # Dépendances Python
├── .gitignore
└── README.md
```

## Idées d'améliorations (pour aller plus loin)

- Ajouter un mode "cartoon" ou "aquarelle" en plus du crayon
- Ajouter un historique des images traitées dans la session
- Convertir plusieurs images en une fois (traitement par lot)
- Ajouter des tests unitaires sur la fonction `image_to_sketch`
