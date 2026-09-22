import streamlit as st
import random
import time

# Configuración de la página
st.set_page_config(page_title="Flores Amarillas", page_icon="🌻")

# CSS para forzar el fondo oscuro global y hacer legibles los botones
st.markdown("""
    <style>
    /* Fondo principal oscuro */
    .stApp {
        background-color: #0b0f19 !important;
        color: #f8fafc !important;
    }
    
    /* Forzar que los textos superiores sean claros */
    p {
        color: #f8fafc !important;
    }
    h1 {
        color: #facc15 !important; 
        text-align: center;
    }
    
    /* Diseño de los botones con contraste (amarillo y letras oscuras) */
    div.stButton > button {
        background-color: #facc15 !important;
        color: #0b0f19 !important;
        font-weight: bold !important;
        border: none !important;
        border-radius: 8px !important;
    }
    div.stButton > button:hover {
        background-color: #eab308 !important;
    }
    </style>
""", unsafe_allow_html=True)

# Título
st.markdown("<h1>while(distancia > 0) { amor++; } 🌻</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-family: Courier New;'>Para la chica más lindaaa, para nada loquitaa, obvio, seriedad.</p>", unsafe_allow_html=True)
st.write("")

# Bloque de código construido con HTML para garantizar el fondo oscuro y letras claras
codigo_html = """
<div style="background-color: #1e293b; padding: 20px; border-radius: 10px; border-left: 5px solid #facc15; font-family: 'Courier New', monospace; font-size: 15px; line-height: 1.6; overflow-x: auto;">
    <span style="color: #94a3b8;"># Módulo de conexión a distancia</span><br>
    <span style="color: #f472b6;">ciudad_ella</span> <span style="color: #e2e8f0;">=</span> <span style="color: #a3e635;">"Lima puaj"</span><br>
    <span style="color: #f472b6;">ciudad_yo</span> <span style="color: #e2e8f0;">=</span> <span style="color: #a3e635;">"Huancayo"</span><br>
    <span style="color: #f472b6;">estado</span> <span style="color: #e2e8f0;">=</span> <span style="color: #a3e635;">"Pendiente de ti, amooor"</span><br>
    <span style="color: #38bdf8;">print</span><span style="color: #e2e8f0;">(</span><span style="color: #a3e635;">"¡Te extrañoooo, corazoooom!"</span><span style="color: #e2e8f0;">)</span>
</div>
"""
st.markdown(codigo_html, unsafe_allow_html=True)
st.write("")

# Función para generar la lluvia de girasoles usando CSS (no se bloquea nunca)
def generar_lluvia_flores():
    flores_css = "<style>"
    flores_html = ""
    for i in range(40): # Cantidad de flores
        left = random.randint(0, 100)
        delay = random.uniform(0, 1.5)
        duration = random.uniform(2.5, 4.5)
        size = random.randint(20, 35)
        
        flores_css += f"""
        @keyframes caida_{i} {{
            0% {{ top: -10%; transform: rotate(0deg) translateX(0px); opacity: 1; }}
            100% {{ top: 110%; transform: rotate({random.randint(180, 360)}deg) translateX({random.randint(-30, 30)}px); opacity: 0; }}
        }}
        .flor_{i} {{
            position: fixed;
            left: {left}%;
            z-index: 99999;
            font-size: {size}px;
            animation: caida_{i} {duration}s linear {delay}s forwards;
            pointer-events: none;
        }}
        """
        flores_html += f'<div class="flor_{i}">🌻</div>'
        
    flores_css += "</style>"
    return flores_css + flores_html

st.markdown("<h3 style='text-align: center; color: #facc15; font-family: Courier New;'>¿Lista para tu detalle?</h3>", unsafe_allow_html=True)

# Botón interactivo principal
if st.button("Haz clic para recibir tus flores amarillas 🌻", use_container_width=True):
    # Inyectar la lluvia de flores directamente en la pantalla
    st.markdown(generar_lluvia_flores(), unsafe_allow_html=True)
    time.sleep(0.5)
    
    st.success("¡Te extrañoo, estoy seguro de que ya nos veremoos, te quieroamo moor! 🌻💛")
    st.markdown("<h3 style='text-align: center; color: #facc15; font-family: Courier New;'>💛 Es un detallitoo espero te gusteee, te adorooo muack 💛</h3>", unsafe_allow_html=True)
