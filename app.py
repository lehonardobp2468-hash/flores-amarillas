import streamlit as st
import time

# Configuración de la página
st.set_page_config(page_title="Flores Amarillas para ti 🌻", page_icon="🌻")

# Estilos CSS limpios para garantizar el fondo oscuro y evitar fondos blancos molestos
st.markdown("""
    <style>
    .stApp {
        background-color: #0b0f19;
        color: #f8fafc;
    }
    .titulo {
        color: #facc15;
        text-align: center;
        font-family: 'Courier New', monospace;
        font-weight: bold;
    }
    .subtitulo {
        color: #f8fafc;
        text-align: center;
        font-size: 1.1rem;
        font-family: 'Courier New', monospace;
    }
    </style>
""", unsafe_allow_html=True)

# Título y subtítulo
st.markdown("<h1 class='titulo'>while(distancia > 0) { amor++; } 🌻</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitulo'>Para la chica más linda, sin importar los kilómetros de distancia.</p>", unsafe_allow_html=True)

st.write("")

# Bloque de código usando el componente nativo de Streamlit (se ve perfecto y ordenado)
codigo_romantico = """# Módulo de conexión a distancia
ciudad_ella = "Lima"
ciudad_yo = "Huancayo"
estado = "Pendiente de ti, amor"
print("¡Te extrañoooo, corazoooom!")"""

st.code(codigo_romantico, language="python")

st.write("")

# Sección interactiva con el botón nativo de Streamlit
st.markdown("<h3 style='text-align: center; color: #facc15; font-family: Courier New;'>¿Lista para tu detalle?</h3>", unsafe_allow_html=True)

# Botón interactivo que activa la animación nativa de globos/celebración y muestra mensajes hermosos
if st.button("Haz clic para recibir tus flores amarillas 🌻", use_container_width=True):
    st.balloons() # Lanza la animación oficial de celebración de Streamlit
    time.sleep(0.5)
    st.success("¡Ramo de flores virtuales entregado con éxito a través de la red! 🌻💛")
    st.markdown("<h3 style='text-align: center; color: #facc15; font-family: Courier New;'>✨ A pesar de la distancia, mi código siempre compila hacia ti. ✨</h3>", unsafe_allow_html=True)
    st.balloons()

# Botón adicional para la dedicatoria
st.write("")
if st.button("Ver dedicatoria especial 💌", use_container_width=True):
    st.info("¡Espero que te gusteeees, es un detallitooo hecho con código para ti! Te quiero muchísimo. 🌻💛")
