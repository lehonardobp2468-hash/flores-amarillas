import streamlit as st
import time

# Configuración de la página
st.set_page_config(page_title="Flores Amarillas", page_icon="💛")

# Estilos CSS personalizados
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

# Título y dedicatoria (usando código HTML seguro para el emoji &#127811;)
st.markdown("<h1>while(distancia > 0) { amor++; } &#127811;</h1>", unsafe_allow_html=True)
st.markdown("<p>Para la chica más linda, sin importar los kilómetros de distancia.</p>", unsafe_allow_html=True)

# Bloque de código simulado
st.markdown("""
<div class="code-box">
<code>
# Módulo de conexión a distancia<br>
ciudad_ella = "Lima puaj"<br>
ciudad_yo = "Huancayork"<br>
estado = "Pendiente de ti, moooor "<br>
print("¡Te extrañooo, corazoooom!")
</div>
</code>
""", unsafe_allow_html=True)

# Botón interactivo
if st.button("Haz clic para recibir tus flores amarillas 💛", use_container_width=True):
    st.balloons() 
    st.success("Espero que te gusteee, es un detallitooo, Te quieroamo muchísimo. 💛")
    time.sleep(1)
    st.markdown("<h3 style='text-align: center; color: #facc15;'>✨ Estoy seguro de que ya nos veremos, estoy muy orgulloso de ti corazóm ✨</h3>", unsafe_allow_html=True)
