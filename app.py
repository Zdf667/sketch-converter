import streamlit as st
import cv2
import numpy as np
from PIL import Image, UnidentifiedImageError
import io

st.set_page_config(page_title="Croquis Converter", page_icon="✏️", layout="wide")

# Ne pas avoir une trop grande image
MAX_DIMENSION = 2000

st.title("✏️ Convertisseur d'image en croquis au crayon")
st.write(
    "Téléverse une photo et transforme-la instantanément en dessin au crayon, "
    "directement dans ton navigateur."
)

uploaded_file = st.file_uploader("Choisis une image", type=["jpg", "jpeg", "png"])

blur_intensity = st.slider(
    "Intensité de l'effet crayon",
    min_value=21,
    max_value=111,
    value=51,
    step=2,
    help="Plus la valeur est haute, plus le trait est doux et estompé.",
)


def image_to_sketch(image: Image.Image, blur_value: int) -> np.ndarray:
    """Convertit une image PIL en croquis au crayon en niveaux de gris.

    Lève une ValueError avec un message clair si l'image ne peut pas
    être traitée (image vide, mode non convertible, etc.).
    """
    try:
        img_array = np.array(image.convert("RGB"))
    except Exception as exc:
        raise ValueError(f"Impossible de convertir l'image en RGB : {exc}") from exc

    if img_array.size == 0 or 0 in img_array.shape[:2]:
        raise ValueError("L'image semble vide (dimensions nulles).")

    try:
        gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
        gray_smoothed = cv2.bilateralFilter(gray, d=9, sigmaColor=60, sigmaSpace=60)
        inverted = 255 - gray_smoothed
        blurred = cv2.GaussianBlur(inverted, (blur_value, blur_value), 0)
        inverted_blurred = 255 - blurred
        sketch = cv2.divide(gray, inverted_blurred, scale=256.0)
    except cv2.error as exc:
        raise ValueError(f"Erreur de traitement d'image (OpenCV) : {exc}") from exc

    return sketch


if uploaded_file is not None:
    # 1. Ouverture et validation du fichier envoyé par l'utilisateur
    try:
        image = Image.open(uploaded_file)
        image.load()  # force la lecture complète pour détecter un fichier corrompu tout de suite
    except UnidentifiedImageError:
        st.error(
            "Ce fichier ne semble pas être une image valide. "
            "Vérifie qu'il s'agit bien d'un .jpg, .jpeg ou .png non corrompu."
        )
        st.stop()
    except (IOError, OSError) as exc:
        st.error(f"Impossible de lire ce fichier : {exc}")
        st.stop()

    # 2. Redimensionnement si l'image est trop grande
    if max(image.size) > MAX_DIMENSION:
        st.warning(
            f"Image redimensionnée automatiquement (elle dépassait {MAX_DIMENSION}px)."
        )
        image.thumbnail((MAX_DIMENSION, MAX_DIMENSION))

    # 3. Conversion en croquis avec une gestion d'erreur
    try:
        sketch = image_to_sketch(image, blur_intensity)
    except ValueError as exc:
        st.error(f"Erreur lors de la conversion en croquis : {exc}")
        st.stop()

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Image originale")
        st.image(image, use_container_width=True)
    with col2:
        st.subheader("Croquis au crayon")
        st.image(sketch, use_container_width=True, clamp=True, channels="GRAY")

    # 4. Préparation du téléchargement avec gestion d'erreur
    try:
        sketch_img = Image.fromarray(sketch)
        buf = io.BytesIO()
        sketch_img.save(buf, format="PNG")
    except Exception as exc:
        st.error(f"Impossible de préparer le fichier à télécharger : {exc}")
        st.stop()

    st.download_button(
        label="Télécharger le croquis",
        data=buf.getvalue(),
        file_name="croquis.png",
        mime="image/png",
    )
else:
    st.info("Téléverse une image pour commencer.")

st.markdown("---")
st.caption("Projet réalisé avec Python, OpenCV et Streamlit.")
