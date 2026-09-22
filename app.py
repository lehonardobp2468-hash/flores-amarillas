import streamlit as st
import time

# Configuración de la página
st.set_page_config(page_title="Flores Amarillas para ti 🌻", page_icon="🌻")

# Estilos CSS personalizados (modo oscuro y diseño programador)
st.markdown("""
    <style>
    .stApp {
        background-color: #0f172a;
        color: #f8fafc;
    }
    h1 {
        color: #facc15;
        text-align: center;
        font-family: 'Courier New', monospace;
    }
    p {
        text-align: center;
        font-size: 1.2rem;
        font-family: 'Courier New', monospace;
    }
    .code-box {
        background-color: #1e293b;
        padding: 15px;
        border-radius: 8px;
        border-left: 4px solid #facc15;
        font-family: 'Courier New', monospace;
        margin: 20px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Título y dedicatoria
st.markdown("<h1>while(distancia > 0) { amor++; } 🌻</h1>", unsafe_allow_html=True)
st.markdown("<p>Para la chica más linda, sin importar los kilómetros de distancia.</p>", unsafe_allow_html=True)

# Bloque de código simulado
st.markdown("""
<div class="code-box">
<code>
# Módulo de conexión a distancia<br>
ciudad_ella = "Su Ciudad"<br>
ciudad_yo = "Mi Ciudad"<br>
estado = "Pensando en ti 24/7"<br>
print("¡Feliz día de las flores amarillas, mi amor!")
</div>
</code>
""", unsafe_allow_html=True)

# Botón interactivo
if st.button("Haz clic para recibir tus flores amarillas 💛", use_container_width=True):
    st.balloons() # Lanza animación de globos/efectos en la web
    st.success("🌻 ¡Ramo de flores virtuales entregado con éxito a través de la red! Te amo muchísimo.")
    time.sleep(1)
    st.markdown("<h3 style='text-align: center; color: #facc15;'>✨ A pesar de la distancia, mi código siempre compila hacia ti. ✨</h3>", unsafe_allow_html=True)
