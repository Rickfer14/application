import streamlit as st
import time

# Configuración de la página
st.set_page_config(
    page_title="🥳❤️",
    page_icon="happy cum🥳",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Estilos CSS para el fondo rosado y detalles decorativos
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Harlow+Solid+Italic&display=swap');
    .stApp {
        background-color: #FFC0CB; /* Fondo rosado */
        color: #8B0000; /* Color de texto oscuro para contraste */
        font-family: 'Harlow Solid Italic', cursive;
        background-image: url("https://www.transparenttextures.com/patterns/flowers.png"); /* Patrón de flores */
        background-size: cover;
    }
    .loading {
        font-size: 24px;
        text-align: center;
        margin-top: 20%;
    }
    .main-text {
        font-size: 32px;
        text-align: center;
        margin-top: 20px;
        animation: fadeIn 2s forwards;
    }
    @keyframes fadeIn {
        to {
            opacity: 1;
        }
    }
    .info {
        position: fixed;
        font-size: 20px;
    }
    .info-left {
        bottom: 20px;
        left: 20px;
    }
    .info-right {
        bottom: 20px;
        right: 20px;
    }
    .rose {
        position: absolute;
        width: 100px;
        height: 100px;
        animation: fadeIn 2s forwards;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Pantalla de carga
with st.spinner("Cargando..."):
    time.sleep(3)  # Simula una carga de 3 segundos

# Función para simular la escritura en vivo
def typewriter(text, delay=0.1):
    placeholder = st.empty()
    for i in range(len(text) + 1):
        placeholder.markdown(f"<div class='main-text'>{text[:i]}</div>", unsafe_allow_html=True)
        time.sleep(delay)

# Texto principal
main_text = "Feliz cumpleaños Isabellita, ya son 19, te quiero mucho, eres tú y ya❤️"

# Escribir el texto principal
typewriter(main_text)

# Insertar una imagen
st.markdown(
    """
    <div style='text-align: center; margin-top: 20px;'>
        <img src='https://stickerly.pstatic.net/sticker_pack/GKxNn91GyJYvRhMszE6eOQ/0TEYRQ/45/-939941299.png' alt='Imagen' style='width: 300px; border-radius: 10px;'>
    </div>
    """,
    unsafe_allow_html=True,
)

# Dibujar tres rosas como imágenes alrededor del texto principal
st.markdown(
    """
    <div style='position: relative; text-align: center; margin-top: 20px;'>
        <!-- Rosa 1 (arriba a la izquierda) -->
        <img class="rose" src="https://i.ibb.co/zHsctgmG/Screenshot-20260115-231537-Spotify.jpg" alt="Rosa 1" style="top: 10%; left: 10%; width: 100px; height: 100px;">
        <!-- Rosa 2 (arriba a la derecha) -->
        <img class="rose" src="https://www.21-draw.com/wp-content/uploads/2023/08/color-the-leaves-e1692607469362-1024x1020.jpg" alt="Rosa 2" style="top: 10%; right: 10%; width: 100px; height: 100px;">
        <!-- Rosa 3 (abajo a la izquierda) -->
        <img class="rose" src="https://www.21-draw.com/wp-content/uploads/2023/08/color-the-leaves-e1692607469362-1024x1020.jpg" alt="Rosa 3" style="bottom: 10%; left: 10%; width: 100px; height: 100px;">
    </div>
    """,
    unsafe_allow_html=True,
)
#<a href="https://imgbb.com/"><img src="https://i.ibb.co/zHsctgmG/Screenshot-20260115-231537-Spotify.jpg" alt="Screenshot-20260115-231537-Spotify" border="0" /></a>
# Información adicional
st.markdown(
    """
    <div class="info info-left">Nos vemos mas tarde en Kabal</div>
    <div class="info info-right">Pasala bien!</div>
    """,
    unsafe_allow_html=True,
)
