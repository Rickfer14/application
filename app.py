import streamlit as st
import time

# 1. Configuración de la página
st.set_page_config(
    page_title="🥳❤️",
    page_icon="🎂",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# 2. Estilos CSS Personalizados
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Harlow+Solid+Italic&display=swap');
    
    .stApp {
        background-color: #FFC0CB; /* Fondo rosado */
        color: #8B0000;
        font-family: 'Harlow Solid Italic', cursive;
        background-image: url("https://www.transparenttextures.com/patterns/flowers.png");
        background-size: cover;
    }

    .main-text {
        font-size: 35px;
        text-align: center;
        margin-top: 20px;
        line-height: 1.4;
    }

    .info {
        position: fixed;
        font-size: 18px;
        font-weight: bold;
    }

    .info-left { bottom: 20px; left: 20px; }
    .info-right { bottom: 20px; right: 20px; }

    .rose {
        position: absolute;
        width: 110px;
        height: 110px;
        border-radius: 50%;
        border: 3px solid #fff;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
    }

    /* Estilo para el contenedor de YouTube */
    .video-container {
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 3. Música de YouTube (The Abyss - The Weeknd & Lana Del Rey)
# Se muestra un reproductor pequeño para que ella pueda activar el sonido
st.markdown("<div class='video-container'>", unsafe_allow_html=True)
st.video("https://youtu.be/YJ84U_30GRM?si=g7CILpIwEL2fX6tO")
st.caption("dale plei para escuchar")
st.markdown("</div>", unsafe_allow_html=True)

# 4. Pantalla de carga
with st.spinner("Preparando tu sorpresa..."):
    time.sleep(2)

# 5. Función de escritura animada
def typewriter(text, delay=0.1):
    placeholder = st.empty()
    for i in range(len(text) + 1):
        placeholder.markdown(f"<div class='main-text'>{text[:i]}</div>", unsafe_allow_html=True)
        time.sleep(delay)

main_text = "Feliz cumpleaños Isabellita, ya son 19, te quiero mucho, eres tú y ya❤️"
typewriter(main_text)

# 6. Imagen central (Sticker)
st.markdown(
    """
    <div style='text-align: center; margin-top: 30px;'>
        <img src='https://stickerly.pstatic.net/sticker_pack/GKxNn91GyJYvRhMszE6eOQ/0TEYRQ/45/-939941299.png' 
        style='width: 280px; border-radius: 15px; box-shadow: 5px 5px 15px rgba(0,0,0,0.1);'>
    </div>
    """,
    unsafe_allow_html=True,
)

# 7. Rosas decorativas
st.markdown(
    """
    <div style='position: relative; text-align: center; margin-top: 20px;'>
        <img class="rose" src="https://i.ibb.co/zHsctgmG/Screenshot-20260115-231537-Spotify.jpg" style="top: 0%; left: 5%;">
        <img class="rose" src="https://i.ibb.co/BKjgVsRX/Screenshot-20260115-233328-Whats-App.jpg" style="top: 0%; right: 5%;">
        <img class="rose" src="https://www.21-draw.com/wp-content/uploads/2023/08/color-the-leaves-e1692607469362-1024x1020.jpg" style="top: 150px; left: 5%;">
    </div>
    """,
    unsafe_allow_html=True,
)
# 8. Mensajes en las esquinas
st.markdown(
    """
    <div class="info info-left">📍 Nos vemos en Kabal</div>
    <div class="info info-right">¡Disfruta tu día! ✨</div>
    """,
    unsafe_allow_html=True,
)
