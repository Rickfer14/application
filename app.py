import streamlit as st
import time

# 1. Configuración de la página
st.set_page_config(
    page_title="🥳❤️",
    page_icon="🎂", # Cambiado a emoji para mejor compatibilidad
    layout="centered",
    initial_sidebar_state="collapsed",
)

# 2. Configuración de Música de YouTube (Oculta)
# ID del video: l_NcVpR6DJo (Canción emotiva de cumpleaños)
video_id = "l_NcVpR6DJo"
youtube_url = f"https://www.youtube.com/embed/{video_id}?autoplay=1&loop=1&playlist={video_id}"

st.markdown(
    f"""
    <iframe width="0" height="0" src="{youtube_url}" 
        frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
    </iframe>
    """,
    unsafe_allow_html=True
)

# 3. Estilos CSS
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
    .main-text {
        font-size: 32px;
        text-align: center;
        margin-top: 20px;
        opacity: 0;
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

# 4. Pantalla de carga
with st.spinner("Cargando sorpresa..."):
    time.sleep(3)

# 5. Función de escritura en vivo
def typewriter(text, delay=0.1):
    placeholder = st.empty()
    for i in range(len(text) + 1):
        placeholder.markdown(f"<div class='main-text'>{text[:i]}</div>", unsafe_allow_html=True)
        time.sleep(delay)

# Texto principal
main_text = "Feliz cumpleaños Isabellita, ya son 19, te quiero mucho, eres tú y ya❤️"

# Ejecutar escritura
typewriter(main_text)

# 6. Imagen central
st.markdown(
    """
    <div style='text-align: center; margin-top: 20px;'>
        <img src='https://stickerly.pstatic.net/sticker_pack/GKxNn91GyJYvRhMszE6eOQ/0TEYRQ/45/-939941299.png' alt='Imagen' style='width: 300px; border-radius: 10px;'>
    </div>
    """,
    unsafe_allow_html=True,
)

# 7. Rosas decorativas
st.markdown(
    """
    <div style='position: relative; text-align: center; margin-top: 20px;'>
        <img class="rose" src="https://i.ibb.co/zHsctgmG/Screenshot-20260115-231537-Spotify.jpg" style="top: 10%; left: 10%;">
        <img class="rose" src="https://i.ibb.co/BKjgVsRX/Screenshot-20260115-233328-Whats-App.jpg" style="top: 10%; right: 10%;">
        <img class="rose" src="https://www.21-draw.com/wp-content/uploads/2023/08/color-the-leaves-e1692607469362-1024x1020.jpg" style="bottom: 10%; left: 10%;">
    </div>
    """,
    unsafe_allow_html=True,
)

# 8. Información adicional
st.markdown(
    """
    <div class="info info-left">Nos vemos mas tarde en Kabal</div>
    <div class="info info-right">Pasala bien!</div>
    """,
    unsafe_allow_html=True,
)
