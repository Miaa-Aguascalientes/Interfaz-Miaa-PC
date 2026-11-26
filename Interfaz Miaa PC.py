import base64
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Interfaz Miaa",
    page_icon="https://www.miaa.mx/favicon.ico",
    layout="wide",
    initial_sidebar_state="expanded"
)

LOGO_URL = "https://raw.githubusercontent.com/Miaa-Aguascalientes/Logos/38504978c8f77a4dac38ad476f74dbdee6af2cad/LogoMIAA.svg"


def img_to_base64(ruta: str) -> str:
    archivo = Path(ruta)
    if archivo.exists():
        ext = archivo.suffix.lower().replace(".", "")
        if ext == "jpg":
            ext = "jpeg"
        data = base64.b64encode(archivo.read_bytes()).decode("utf-8")
        return f"data:image/{ext};base64,{data}"
    return ""


FONDO_B64 = img_to_base64("assets/fondo_miaa.jpg")

SISTEMAS = [
    {
        "titulo": "SCADA<br>Pozos y Equipos",
        "descripcion": "Monitoreo y control de pozos y equipos",
        "url": "https://sistema-scada.streamlit.app/",
        "imagen": img_to_base64("assets/icon_scada.png"),
        "glow": "#00d4ff",
        "glow_rgba": "rgba(0, 212, 255, 0.75)"
    },
    {
        "titulo": "Medidores<br>Inteligentes",
        "descripcion": "Lecturas y análisis de medidores",
        "url": "https://lecturas-hes.streamlit.app/",
        "imagen": img_to_base64("assets/icon_medidores.png"),
        "glow": "#00e5ff",
        "glow_rgba": "rgba(0, 229, 255, 0.75)"
    },
    {
        "titulo": "Mapa y GIS",
        "descripcion": "Información geográfica y sectorización",
        "url": "https://miaa-sincronizador-ver-app.streamlit.app/",
        "imagen": img_to_base64("assets/icon_gis.png"),
        "glow": "#10b981",
        "glow_rgba": "rgba(16, 185, 129, 0.75)"
    },
    {
        "titulo": "Mantenimiento",
        "descripcion": "Gestión de mantenimiento y fallas",
        "url": "https://incidencias-miaa.streamlit.app/",
        "imagen": img_to_base64("assets/icon_mantenimiento.png"),
        "glow": "#f59e0b",
        "glow_rgba": "rgba(245, 158, 11, 0.75)"
    },
    {
        "titulo": "Tableros y Reportes",
        "descripcion": "Indicadores y reportes ejecutivos",
        "url": "https://tableros-miaa.streamlit.app/",
        "imagen": img_to_base64("assets/icon_tableros.png"),
        "glow": "#8b5cf6",
        "glow_rgba": "rgba(139, 92, 246, 0.75)"
    },
    {
        "titulo": "HES - Consumo",
        "descripcion": "Lecturas y análisis de consumo",
        "url": "https://hes-consumo.streamlit.app/",
        "imagen": img_to_base64("assets/icon_hes.png"),
        "glow": "#06b6d4",
        "glow_rgba": "rgba(6, 182, 212, 0.75)"
    }
]

fondo_css = (
    f'url("{FONDO_B64}") center center / cover no-repeat fixed'
    if FONDO_B64
    else 'radial-gradient(ellipse at 75% 20%, rgba(0, 174, 255, 0.35) 0%, transparent 45%), linear-gradient(180deg, #020b18 0%, #05264d 45%, #020d1f 100%)'
)

st.markdown(
    f'<style>'
    "@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap');"
    '[data-testid="stHeader"] {{background: transparent !important;}}'
    '[data-testid="stDecoration"] {{display: none !important;}}'
    '#MainMenu, footer {{visibility: hidden;}}'
    '[data-testid="stSidebar"] {{'
    '  background: linear-gradient(180deg, #031124 0%, #051f3f 100%) !important;'
    '  border-right: 1px solid rgba(0, 212, 255, 0.25) !important;'
    '}}'
    '.stApp {{'
    f'  background: {fondo_css};'
    '  font-family: "Inter", sans-serif;'
    '  color: #ffffff;'
    '}}'
    '.block-container {{'
    '  padding-top: 0.6rem !important;'
    '  padding-bottom: 4rem !important;'
    '  padding-left: 2rem !important;'
    '  padding-right: 2rem !important;'
    '  max-width: 1520px;'
    '}}'
    '.miaa-header-bar {{'
    '  display: flex;'
    '  justify-content: space-between;'
    '  align-items: center;'
    '  padding: 6px 4px 18px 4px;'
    '  margin-bottom: 18px;'
    '}}'
    '.miaa-brand-wrap {{display: flex; align-items: center; gap: 22px;}}'
    '.miaa-brand-wrap img {{height: 64px; width: auto; filter: brightness(0) invert(1) drop-shadow(0 2px 10px rgba(0,0,0,0.65));}}'
    '.miaa-divider {{width: 2px; height: 52px; background: rgba(255,255,255,0.75);}}'
    '.miaa-heading h1 {{margin: 0; font-size: 1.65rem; font-weight: 700; color: #ffffff; text-shadow: 0 2px 8px rgba(0,0,0,0.75);}}'
    '.miaa-heading p {{margin: 4px 0 0 0; font-size: 1.15rem; font-weight: 400; color: #cbd5e1; text-shadow: 0 2px 8px rgba(0,0,0,0.75);}}'
    '.miaa-clock-box {{'
    '  background: rgba(4, 18, 38, 0.72);'
    '  border: 1px solid rgba(148, 163, 184, 0.35);'
    '  border-radius: 10px;'
    '  padding: 10px 18px;'
    '  backdrop-filter: blur(10px);'
    '  min-width: 195px;'
    '}}'
    '.miaa-clock-line {{display: flex; align-items: center; gap: 9px; font-size: 0.9rem; color: #e2e8f0; margin-bottom: 4px;}}'
    '.miaa-clock-line:last-child {{margin-bottom: 0; font-size: 1.1rem; font-weight: 700; color: #ffffff;}}'
    '.miaa-cards-grid {{'
    '  display: grid;'
    '  grid-template-columns: repeat(3, minmax(0, 1fr));'
    '  gap: 22px;'
    '}}'
    '@media (max-width: 1120px) {{.miaa-cards-grid {{grid-template-columns: repeat(2, minmax(0, 1fr));}}}}'
    '@media (max-width: 740px) {{.miaa-cards-grid {{grid-template-columns: 1fr;}}}}'
    '.miaa-module-card {{'
    '  position: relative;'
    '  display: grid;'
    '  grid-template-columns: 138px 1fr 36px;'
    '  align-items: center;'
    '  gap: 16px;'
    '  height: 176px;'
    '  padding: 16px 20px;'
    '  border-radius: 18px;'
    '  background: linear-gradient(135deg, rgba(16, 46, 84, 0.62) 0%, rgba(5, 19, 39, 0.82) 100%);'
    '  border: 1.5px solid rgba(255, 255, 255, 0.28);'
    '  backdrop-filter: blur(14px);'
    '  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.6), inset 0 1px 1px rgba(255, 255, 255, 0.25);'
    '  overflow: hidden;'
    '  transition: transform 0.22s ease, border-color 0.22s ease, box-shadow 0.22s ease;'
    '}}'
    '.miaa-module-card::after {{'
    '  content: "";'
    '  position: absolute;'
    '  bottom: 0;'
    '  left: 5%;'
    '  right: 5%;'
    '  height: 5px;'
    '  background: var(--g);'
    '  border-radius: 5px 5px 0 0;'
    '  box-shadow: 0 -3px 16px var(--gr), 0 0 26px var(--gr);'
    '}}'
    '.miaa-module-card:hover {{'
    '  transform: translateY(-5px);'
    '  border-color: var(--g);'
    '  box-shadow: 0 16px 36px rgba(0, 0, 0, 0.75), 0 0 22px var(--gr);'
    '}}'
    '.miaa-module-overlay {{position: absolute; inset: 0; z-index: 5; text-decoration: none !important;}}'
    '.miaa-module-thumb {{'
    '  width: 138px;'
    '  height: 134px;'
    '  border-radius: 12px;'
    '  overflow: hidden;'
    '  display: flex;'
    '  align-items: center;'
    '  justify-content: center;'
    '  background: rgba(3, 14, 30, 0.55);'
    '  border: 1px solid rgba(255, 255, 255, 0.14);'
    '}}'
    '.miaa-module-thumb img {{width: 100%; height: 100%; object-fit: cover;}}'
    '.miaa-module-info {{min-width: 0;}}'
    '.miaa-module-title {{font-size: 1.28rem; font-weight: 700; color: #ffffff; line-height: 1.18; margin-bottom: 8px; text-shadow: 0 2px 6px rgba(0,0,0,0.65);}}'
    '.miaa-module-desc {{font-size: 0.9rem; font-weight: 400; color: #e2e8f0; line-height: 1.3;}}'
    '.miaa-module-next {{'
    '  width: 34px;'
    '  height: 34px;'
    '  border-radius: 50%;'
    '  border: 2px solid var(--g);'
    '  display: flex;'
    '  align-items: center;'
    '  justify-content: center;'
    '  color: #ffffff;'
    '  font-size: 1rem;'
    '  font-weight: 700;'
    '  align-self: end;'
    '  background: rgba(2, 11, 23, 0.55);'
    '}}'
    '.miaa-footer-bar {{'
    '  position: fixed;'
    '  bottom: 0;'
    '  left: 0;'
    '  right: 0;'
    '  height: 40px;'
    '  background: rgba(2, 11, 23, 0.9);'
    '  border-top: 1px solid rgba(125, 211, 252, 0.25);'
    '  display: flex;'
    '  justify-content: space-between;'
    '  align-items: center;'
    '  padding: 0 24px;'
    '  padding-right: 175px;'
    '  z-index: 980;'
    '  font-size: 0.84rem;'
    '  color: #e2e8f0;'
    '}}'
    '</style>',
    unsafe_allow_html=True
)

with st.sidebar:
    st.markdown(
        f'<div style="text-align:center;padding:8px 0 14px 0;">'
        f'<img src="{LOGO_URL}" style="height:42px;filter:brightness(0) invert(1);">'
        f'</div>',
        unsafe_allow_html=True
    )
    st.markdown("### Sistemas")
    for s in SISTEMAS:
        st.page_link(s["url"], label=s["titulo"].replace("<br>", " "))

st.markdown(
    '<div class="miaa-header-bar">'
    '<div class="miaa-brand-wrap">'
    f'<img src="{LOGO_URL}" alt="MIAA">'
    '<div class="miaa-divider"></div>'
    '<div class="miaa-heading">'
    '<h1>Sistema Integral de Monitoreo</h1>'
    '<p>Agua Potable para Aguascalientes</p>'
    '</div>'
    '</div>'
    '<div class="miaa-clock-box">'
    '<div class="miaa-clock-line"><span>📅</span><span id="live-date">26 Noviembre 2026</span></div>'
    '<div class="miaa-clock-line"><span>🕒</span><span id="live-clock">08:54:00 AM</span></div>'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)

cards_html = ['<div class="miaa-cards-grid">']
for item in SISTEMAS:
    thumb_content = (
        f'<img src="{item["imagen"]}" alt="{item["titulo"].replace("<br>", " ")}">'
        if item["imagen"]
        else '<span style="color:#7dd3fc;font-size:0.75rem;text-align:center;padding:6px;">Coloca imagen en assets/</span>'
    )
    cards_html.append(
        f'<div class="miaa-module-card" style="--g:{item["glow"]};--gr:{item["glow_rgba"]};">'
        f'<a class="miaa-module-overlay" href="{item["url"]}" target="_blank"></a>'
        f'<div class="miaa-module-thumb">{thumb_content}</div>'
        f'<div class="miaa-module-info">'
        f'<div class="miaa-module-title">{item["titulo"]}</div>'
        f'<div class="miaa-module-desc">{item["descripcion"]}</div>'
        f'</div>'
        f'<div class="miaa-module-next">&#10095;</div>'
        f'</div>'
    )
cards_html.append('</div>')
st.markdown("".join(cards_html), unsafe_allow_html=True)

st.markdown(
    '<div class="miaa-footer-bar">'
    '<div><strong>MIAA</strong> &nbsp;|&nbsp; Innovación, Tecnología y Agua para Todos</div>'
    '<div style="display:flex;gap:14px;">'
    '<span>⚙️ Configuración</span><span>|</span>'
    '<span>ℹ️ Acerca de</span><span>|</span>'
    '<span>⏻ Cerrar Sesión</span>'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)

components.html(
    """
    <script>
    function tick() {
        const doc = window.parent.document;
        const dEl = doc.getElementById("live-date");
        const tEl = doc.getElementById("live-clock");
        if (!dEl || !tEl) return;
        const now = new Date();
        const meses = [
            "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
            "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
        ];
        dEl.textContent = String(now.getDate()).padStart(2, "0") + " " + meses[now.getMonth()] + " " + now.getFullYear();
        let h = now.getHours();
        const m = String(now.getMinutes()).padStart(2, "0");
        const s = String(now.getSeconds()).padStart(2, "0");
        const ap = h >= 12 ? "PM" : "AM";
        h = h % 12;
        if (h === 0) h = 12;
        tEl.textContent = String(h).padStart(2, "0") + ":" + m + ":" + s + " " + ap;
    }
    setInterval(tick, 1000);
    tick();
    </script>
    """,
    height=0,
    width=0
)
