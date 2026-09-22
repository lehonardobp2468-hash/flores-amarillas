import streamlit as st
import time

# Configuración de la página
st.set_page_config(page_title="Flores Amarillas para ti 🌻", page_icon="🌻")

# Estilos CSS corregidos para forzar el fondo oscuro uniforme y arreglar los textos
st.markdown("""
    <style>
    /* Forzar fondo general oscuro en toda la app */
    .stApp {
        background-color: #0b0f19 !important;
        color: #f8fafc !important;
    }
    
    /* Estilo del título principal */
    h1 {
        color: #facc15 !important;
        text-align: center;
        font-family: 'Courier New', monospace;
    }
    
    /* Estilo de los textos y subtítulos */
    p, .stMarkdown {
        color: #f8fafc !important;
        text-align: center;
        font-family: 'Courier New', monospace;
    }

    /* Caja de código con colores fijos para que no se mezclen */
    .code-box {
        background-color: #1e293b !important;
        color: #38bdf8 !important;
        padding: 20px;
        border-radius: 8px;
        border-left: 4px solid #facc15;
        font-family: 'Courier New', monospace;
        margin: 20px 0;
        text-align: left !important;
    }
    
    .code-box span.comentario { color: #94a3b8; }
    .code-box span.variable { color: #f472b6; }
    .code-box span.string { color: #a3e635; }
    .code-box span.funcion { color: #6ee7b7; }
    </style>
""", unsafe_allow_html=True)

# Título y dedicatoria
st.markdown("<h1>while(distancia > 0) { amor++; } 🌻</h1>", unsafe_allow_html=True)
st.markdown("<p>Para la menos loquitaaa, te extrañooo muchísimo.</p>", unsafe_allow_html=True)

# Bloque de código con diseño limpio
st.markdown("""
<div class="code-box">
<code>
<span class="comentario"># Módulo de conexión a distancia</span><br>
<span class="variable">ciudad_ella</span> = <span class="string">"Lima puaj"</span><br>
<span class="variable">ciudad_yo</span> = <span class="string">"Huancayork"</span><br>
<span class="variable">estado</span> = <span class="string">"Pendiente de ti, amor"</span><br>
<span class="funcion">print</span>(<span class="string">"¡Te extrañoooo, corazoooom!"</span>)
</div>
</code>
""", unsafe_allow_html=True)

# Componente visual interactivo con animación de flores amarillas reales cayendo
# (Esto inyecta JavaScript para que lluevan girasoles al hacer clic en el botón)
flores_html = """
<div style="text-align: center;">
    <button onclick="lloverFlores()" style="
        background-color: #facc15; 
        color: #0b0f19; 
        border: none; 
        padding: 15px 30px; 
        font-size: 1.1rem; 
        font-weight: bold; 
        border-radius: 8px; 
        cursor: pointer;
        font-family: 'Courier New', monospace;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    ">
        Haz clic para recibir tus flores amarillas 🌻
    </button>
</div>

<script>
function lloverFlores() {
    for (let i = 0; i < 40; i++) {
        setTimeout(() => {
            const flower = document.createElement('div');
            flower.innerHTML = '🌻';
            flower.style.position = 'fixed';
            flower.style.left = Math.random() * window.innerWidth + 'px';
            flower.style.top = '-50px';
            flower.style.fontSize = (Math.random() * 20 + 20) + 'px';
            flower.style.zIndex = '999999';
            flower.style.transition = 'transform 3s linear, top 3s linear';
            document.body.appendChild(flower);

            setTimeout(() => {
                flower.style.top = window.innerHeight + 'px';
                flower.style.transform = 'rotate(' + (Math.random() * 360) + 'deg)';
            }, 100);

            setTimeout(() => {
                flower.remove();
            }, 3500);
        }, i * 80);
    }
}
</script>
"""

st.markdown(flores_html, unsafe_allow_html=True)

# Mensaje final oculto o de éxito
st.markdown("<br>", unsafe_allow_html=True)
if st.button("Ver dedicatoria especial 💌"):
    st.success("¡Espero que te gusteeees, es un detallitooo! Te quiero muchísimo. 🌻💛")
