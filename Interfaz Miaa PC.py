import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Interfaz Miaa",
    page_icon="https://www.miaa.mx/favicon.ico",
    layout="wide",
    initial_sidebar_state="expanded"
)

LOGO_URL = "https://raw.githubusercontent.com/Miaa-Aguascalientes/Logos/38504978c8f77a4dac38ad476f74dbdee6af2cad/LogoMIAA.svg"

SISTEMAS = [
    {
        "titulo": "SCADA<br>Pozos y Equipos",
        "descripcion": "Monitoreo y control de pozos y equipos",
        "url": "https://sistema-scada.streamlit.app/",
        "glow": "#00d4ff",
        "glow_rgba": "rgba(0, 212, 255, 0.6)",
        "icon": (
            '<svg viewBox="0 0 128 112" width="98" height="86" xmlns="http://www.w3.org/2000/svg">'
            '<defs><linearGradient id="g1" x1="0" y1="0" x2="1" y2="1">'
            '<stop offset="0%" stop-color="#38bdf8"/><stop offset="100%" stop-color="#0369a1"/>'
            '</linearGradient></defs>'
            '<rect x="46" y="10" width="68" height="44" rx="5" fill="#071b33" stroke="#38bdf8" stroke-width="2"/>'
            '<polyline points="53,41 65,27 76,34 91,18 106,25" fill="none" stroke="#22d3ee" stroke-width="2.5" stroke-linecap="round"/>'
            '<circle cx="91" cy="18" r="3" fill="#ffffff"/>'
            '<rect x="14" y="48" width="52" height="34" rx="6" fill="url(#g1)" stroke="#bae6fd" stroke-width="1.5"/>'
            '<line x1="23" y1="53" x2="23" y2="77" stroke="#06203d" stroke-width="2.5"/>'
            '<line x1="32" y1="53" x2="32" y2="77" stroke="#06203d" stroke-width="2.5"/>'
            '<line x1="41" y1="53" x2="41" y2="77" stroke="#06203d" stroke-width="2.5"/>'
            '<line x1="50" y1="53" x2="50" y2="77" stroke="#06203d" stroke-width="2.5"/>'
            '<circle cx="82" cy="65" r="20" fill="#0c4a6e" stroke="#38bdf8" stroke-width="2.5"/>'
            '<circle cx="82" cy="65" r="8" fill="#041324" stroke="#7dd3fc" stroke-width="2"/>'
            '<rect x="76" y="34" width="12" height="14" fill="#0284c7" stroke="#7dd3fc" stroke-width="1.5"/>'
            '<rect x="10" y="85" width="98" height="6" rx="2" fill="#1e3a8a"/>'
            '</svg>'
        )
    },
    {
        "titulo": "Medidores<br>Inteligentes",
        "descripcion": "Lecturas y análisis de medidores",
        "url": "https://lecturas-hes.streamlit.app/",
        "glow": "#00e5ff",
        "glow_rgba": "rgba(0, 229, 255, 0.6)",
        "icon": (
            '<svg viewBox="0 0 128 112" width="98" height="86" xmlns="http://www.w3.org/2000/svg">'
            '<defs><radialGradient id="m1" cx="45%" cy="40%" r="55%">'
            '<stop offset="0%" stop-color="#f1f5f9"/><stop offset="75%" stop-color="#94a3b8"/><stop offset="100%" stop-color="#334155"/>'
            '</radialGradient></defs>'
            '<path d="M 48 21 Q 64 8 80 21" fill="none" stroke="#22d3ee" stroke-width="3" stroke-linecap="round"/>'
            '<path d="M 54 28 Q 64 19 74 28" fill="none" stroke="#22d3ee" stroke-width="3" stroke-linecap="round"/>'
            '<rect x="12" y="57" width="104" height="16" rx="3" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>'
            '<rect x="18" y="52" width="10" height="26" rx="2" fill="#0369a1"/>'
            '<rect x="100" y="52" width="10" height="26" rx="2" fill="#0369a1"/>'
            '<circle cx="64" cy="65" r="29" fill="url(#m1)" stroke="#38bdf8" stroke-width="3"/>'
            '<circle cx="64" cy="65" r="22" fill="#0f172a" stroke="#7dd3fc" stroke-width="1.5"/>'
            '<rect x="46" y="54" width="36" height="11" rx="2" fill="#bae6fd"/>'
            '<text x="64" y="62.5" font-family="monospace" font-size="8" font-weight="bold" fill="#0c4a6e" text-anchor="middle">000254.7</text>'
            '<circle cx="64" cy="75" r="4" fill="#ef4444"/>'
            '</svg>'
        )
    },
    {
        "titulo": "Mapa y GIS",
        "descripcion": "Información geográfica y sectorización",
        "url": "https://miaa-sincronizador-ver-app.streamlit.app/",
        "glow": "#10b981",
        "glow_rgba": "rgba(16, 185, 129, 0.6)",
        "icon": (
            '<svg viewBox="0 0 128 112" width="98" height="86" xmlns="http://www.w3.org/2000/svg">'
            '<polygon points="18,40 46,30 46,84 18,94" fill="#065f46" stroke="#34d399" stroke-width="1.5"/>'
            '<polygon points="46,30 76,40 76,94 46,84" fill="#047857" stroke="#34d399" stroke-width="1.5"/>'
            '<polygon points="76,40 106,30 106,84 76,94" fill="#059669" stroke="#34d399" stroke-width="1.5"/>'
            '<polyline points="23,66 46,56 76,69 101,53" fill="none" stroke="#38bdf8" stroke-width="3" stroke-linecap="round"/>'
            '<path d="M 76 12 C 65 12 57 20 57 30 C 57 44 76 60 76 60 C 76 60 95 44 95 30 C 95 20 87 12 76 12 Z" fill="#ef4444" stroke="#ffffff" stroke-width="2"/>'
            '<circle cx="76" cy="29" r="6.5" fill="#ffffff"/>'
            '</svg>'
        )
    },
    {
        "titulo": "Mantenimiento",
        "descripcion": "Gestión de mantenimiento y fallas",
        "url": "https://incidencias-miaa.streamlit.app/",
        "glow": "#f59e0b",
        "glow_rgba": "rgba(245, 158, 11, 0.6)",
        "icon": (
            '<svg viewBox="0 0 128 112" width="98" height="86" xmlns="http://www.w3.org/2000/svg">'
            '<defs><linearGradient id="w1" x1="0" y1="0" x2="1" y2="1">'
            '<stop offset="0%" stop-color="#f8fafc"/><stop offset="60%" stop-color="#94a3b8"/><stop offset="100%" stop-color="#475569"/>'
            '</linearGradient></defs>'
            '<g transform="translate(58, 56)">'
            '<circle cx="0" cy="0" r="24" fill="none" stroke="url(#w1)" stroke-width="11" stroke-dasharray="11 7.8"/>'
            '<circle cx="0" cy="0" r="21" fill="#07192f" stroke="#cbd5e1" stroke-width="2.5"/>'
            '<circle cx="0" cy="0" r="10" fill="none" stroke="#f59e0b" stroke-width="2.5"/>'
            '</g>'
            '<g transform="rotate(-42 64 56)">'
            '<rect x="22" y="50" width="84" height="12" rx="4" fill="url(#w1)" stroke="#1e293b" stroke-width="1.5"/>'
            '<circle cx="22" cy="56" r="11" fill="url(#w1)" stroke="#1e293b" stroke-width="1.5"/>'
            '<rect x="11" y="52" width="11" height="8" fill="#07192f"/>'
            '<circle cx="106" cy="56" r="11" fill="url(#w1)" stroke="#1e293b" stroke-width="1.5"/>'
            '<rect x="106" y="52" width="11" height="8" fill="#07192f"/>'
            '</g>'
            '</svg>'
        )
    },
    {
        "titulo": "Tableros y Reportes",
        "descripcion": "Indicadores y reportes ejecutivos",
        "url": "https://tableros-miaa.streamlit.app/",
        "glow": "#8b5cf6",
        "glow_rgba": "rgba(139, 92, 246, 0.6)",
        "icon": (
            '<svg viewBox="0 0 128 112" width="98" height="86" xmlns="http://www.w3.org/2000/svg">'
            '<rect x="18" y="18" width="92" height="56" rx="6" fill="#09182e" stroke="#60a5fa" stroke-width="2.5"/>'
            '<polygon points="55,74 73,74 79,88 49,88" fill="#3b82f6"/>'
            '<rect x="41" y="88" width="46" height="5" rx="2" fill="#93c5fd"/>'
            '<rect x="28" y="52" width="7" height="14" rx="1" fill="#38bdf8"/>'
            '<rect x="39" y="42" width="7" height="24" rx="1" fill="#22d3ee"/>'
            '<rect x="50" y="47" width="7" height="19" rx="1" fill="#818cf8"/>'
            '<rect x="61" y="33" width="7" height="33" rx="1" fill="#a78bfa"/>'
            '<circle cx="88" cy="46" r="12" fill="none" stroke="#1e3a8a" stroke-width="6"/>'
            '<circle cx="88" cy="46" r="12" fill="none" stroke="#00d4ff" stroke-width="6" stroke-dasharray="48 30"/>'
            '</svg>'
        )
    },
    {
        "titulo": "HES - Consumo",
        "descripcion": "Lecturas y análisis de consumo",
        "url": "https://hes-consumo.streamlit.app/",
        "glow": "#06b6d4",
        "glow_rgba": "rgba(6, 182, 212, 0.6)",
        "icon": (
            '<svg viewBox="0 0 128 112" width="98" height="86" xmlns="http://www.w3.org/2000/svg">'
            '<defs><linearGradient id="d1" x1="0" y1="0" x2="0" y2="1">'
            '<stop offset="0%" stop-color="#38bdf8"/><stop offset="100%" stop-color="#0284c7"/>'
            '</linearGradient></defs>'
            '<polygon points="54,22 18,52 26,52 26,88 82,88 82,52 90,52" fill="#cbd5e1" stroke="#38bdf8" stroke-width="2"/>'
            '<polygon points="54,18 14,51 20,56 54,27 88,56 94,51" fill="#0284c7"/>'
            '<rect x="36" y="60" width="14" height="28" rx="2" fill="#0f172a"/>'
            '<rect x="58" y="56" width="14" height="14" rx="1" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>'
            '<path d="M 82 24 Q 94 14 106 24" fill="none" stroke="#22d3ee" stroke-width="3" stroke-linecap="round"/>'
            '<path d="M 87 31 Q 94 24 101 31" fill="none" stroke="#22d3ee" stroke-width="3" stroke-linecap="round"/>'
            '<path d="M 94 46 C 94 46 78 66 78 78 C 78 87 85 94 94 94 C 103 94 110 87 110 78 C 110 66 94 46 94 46 Z" fill="url(#d1)" stroke="#e0f2fe" stroke-width="2"/>'
            '</svg>'
        )
    }
]

st.markdown(
    '<style>'
    "@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap');"
    '[data-testid="stHeader"] {background: transparent !important;}'
    '[data-testid="stDecoration"] {display: none !important;}'
    '#MainMenu, footer {visibility: hidden;}'
    '[data-testid="stSidebar"] {'
    '  background: linear-gradient(180deg, #031124 0%, #051f3f 100%) !important;'
    '  border-right: 1px solid rgba(0, 212, 255, 0.25) !important;'
    '}'
    '.stApp {'
    '  background:'
    '    radial-gradient(ellipse at 72% 18%, rgba(56, 189, 248, 0.24) 0%, transparent 45%),'
    '    radial-gradient(ellipse at 50% 96%, rgba(2, 132, 199, 0.36) 0%, transparent 55%),'
    '    linear-gradient(180deg, #020a17 0%, #051e3d 38%, #041730 72%, #020b1a 100%);'
    '  font-family: "Inter", sans-serif;'
    '  color: #ffffff;'
    '}'
    '.block-container {'
    '  padding-top: 0.8rem !important;'
    '  padding-bottom: 4.2rem !important;'
    '  padding-left: 1.8rem !important;'
    '  padding-right: 1.8rem !important;'
    '  max-width: 1480px;'
    '}'
    '.miaa-top {'
    '  display: flex;'
    '  justify-content: space-between;'
    '  align-items: center;'
    '  padding: 4px 6px 16px 6px;'
    '  border-bottom: 1px solid rgba(125, 211, 252, 0.2);'
    '  margin-bottom: 20px;'
    '}'
    '.miaa-brand {display: flex; align-items: center; gap: 18px;}'
    '.miaa-brand img {height: 54px; width: auto; filter: brightness(0) invert(1) drop-shadow(0 0 10px rgba(56,189,248,0.45));}'
    '.miaa-vsep {width: 2px; height: 44px; background: rgba(255,255,255,0.55);}'
    '.miaa-titles h1 {margin: 0; font-size: 1.5rem; font-weight: 700; color: #ffffff; line-height: 1.15;}'
    '.miaa-titles p {margin: 4px 0 0 0; font-size: 1.05rem; font-weight: 400; color: #bae6fd;}'
    '.miaa-top-right {display: flex; align-items: center; gap: 16px;}'
    '.miaa-clock-card {'
    '  background: rgba(5, 22, 44, 0.75);'
    '  border: 1px solid rgba(125, 211, 252, 0.35);'
    '  border-radius: 10px;'
    '  padding: 8px 14px;'
    '  min-width: 182px;'
    '}'
    '.miaa-clock-row {display: flex; align-items: center; gap: 8px; font-size: 0.86rem; color: #e2e8f0; margin-bottom: 4px;}'
    '.miaa-clock-row:last-child {margin-bottom: 0; font-size: 1.02rem; font-weight: 700; color: #ffffff;}'
    '.miaa-grid {'
    '  display: grid;'
    '  grid-template-columns: repeat(3, minmax(0, 1fr));'
    '  gap: 20px;'
    '}'
    '@media (max-width: 1100px) {'
    '  .miaa-grid {grid-template-columns: repeat(2, minmax(0, 1fr));}'
    '}'
    '@media (max-width: 720px) {'
    '  .miaa-grid {grid-template-columns: 1fr;}'
    '}'
    '.miaa-tile {'
    '  position: relative;'
    '  display: grid;'
    '  grid-template-columns: 108px 1fr 34px;'
    '  align-items: center;'
    '  gap: 14px;'
    '  height: 156px;'
    '  padding: 16px 18px;'
    '  border-radius: 16px;'
    '  background: linear-gradient(145deg, rgba(14, 42, 78, 0.72) 0%, rgba(5, 18, 36, 0.88) 100%);'
    '  border: 1.5px solid rgba(147, 197, 253, 0.32);'
    '  box-shadow: 0 10px 26px rgba(0, 0, 0, 0.55), inset 0 1px 1px rgba(255, 255, 255, 0.18);'
    '  overflow: hidden;'
    '  transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;'
    '}'
    '.miaa-tile::after {'
    '  content: "";'
    '  position: absolute;'
    '  bottom: 0;'
    '  left: 6%;'
    '  right: 6%;'
    '  height: 4px;'
    '  background: var(--g);'
    '  border-radius: 4px 4px 0 0;'
    '  box-shadow: 0 -2px 14px var(--gr), 0 0 22px var(--gr);'
    '}'
    '.miaa-tile:hover {'
    '  transform: translateY(-4px);'
    '  border-color: var(--g);'
    '  box-shadow: 0 14px 32px rgba(0, 0, 0, 0.7), 0 0 18px var(--gr);'
    '}'
    '.miaa-tile-link {'
    '  position: absolute;'
    '  inset: 0;'
    '  z-index: 3;'
    '  text-decoration: none !important;'
    '}'
    '.miaa-tile-icon {'
    '  width: 108px;'
    '  height: 108px;'
    '  display: flex;'
    '  align-items: center;'
    '  justify-content: center;'
    '  background: rgba(3, 14, 29, 0.55);'
    '  border: 1px solid rgba(186, 230, 253, 0.14);'
    '  border-radius: 12px;'
    '  z-index: 1;'
    '}'
    '.miaa-tile-text {z-index: 1; min-width: 0;}'
    '.miaa-tile-title {font-size: 1.2rem; font-weight: 700; color: #ffffff; line-height: 1.18; margin-bottom: 6px;}'
    '.miaa-tile-desc {font-size: 0.86rem; font-weight: 400; color: #cbd5e1; line-height: 1.28;}'
    '.miaa-tile-arrow {'
    '  width: 32px;'
    '  height: 32px;'
    '  border-radius: 50%;'
    '  border: 2px solid var(--g);'
    '  display: flex;'
    '  align-items: center;'
    '  justify-content: center;'
    '  color: #ffffff;'
    '  font-size: 0.95rem;'
    '  font-weight: 700;'
    '  align-self: end;'
    '  background: rgba(2, 11, 23, 0.5);'
    '  z-index: 1;'
    '}'
    '.miaa-bottom-bar {'
    '  position: fixed;'
    '  bottom: 0;'
    '  left: 0;'
    '  right: 0;'
    '  height: 38px;'
    '  background: rgba(2, 11, 23, 0.94);'
    '  border-top: 1px solid rgba(125, 211, 252, 0.25);'
    '  display: flex;'
    '  justify-content: space-between;'
    '  align-items: center;'
    '  padding: 0 24px;'
    '  padding-right: 175px;'
    '  z-index: 980;'
    '  font-size: 0.82rem;'
    '  color: #cbd5e1;'
    '}'
    '.miaa-bottom-left {display: flex; align-items: center; gap: 10px;}'
    '.miaa-bars {display: flex; align-items: flex-end; gap: 2.5px; height: 13px;}'
    '.miaa-bars span {width: 3px; background: #38bdf8; border-radius: 1px;}'
    '.miaa-bottom-right {display: flex; align-items: center; gap: 14px;}'
    '.miaa-sep {color: rgba(255, 255, 255, 0.25);}'
    '</style>',
    unsafe_allow_html=True
)

with st.sidebar:
    st.markdown(
        f'<div style="text-align:center;padding:6px 0 12px 0;">'
        f'<img src="{LOGO_URL}" style="height:40px;filter:brightness(0) invert(1);">'
        f'</div>',
        unsafe_allow_html=True
    )
    st.markdown("### Sistemas")
    for s in SISTEMAS:
        st.page_link(s["url"], label=s["titulo"].replace("<br>", " "))

tank_svg = (
    '<svg width="74" height="64" viewBox="0 0 90 80" style="opacity:0.75;" xmlns="http://www.w3.org/2000/svg">'
    '<path d="M 18 12 Q 45 4 72 12 L 72 36 Q 45 42 18 36 Z" fill="#1e4976" stroke="#7dd3fc" stroke-width="1.5"/>'
    '<text x="45" y="28" font-family="Inter,sans-serif" font-size="11" font-weight="800" fill="#041528" text-anchor="middle">miaa</text>'
    '<line x1="24" y1="37" x2="20" y2="75" stroke="#7dd3fc" stroke-width="2"/>'
    '<line x1="37" y1="39" x2="35" y2="75" stroke="#7dd3fc" stroke-width="2"/>'
    '<line x1="53" y1="39" x2="55" y2="75" stroke="#7dd3fc" stroke-width="2"/>'
    '<line x1="66" y1="37" x2="70" y2="75" stroke="#7dd3fc" stroke-width="2"/>'
    '<line x1="22" y1="56" x2="68" y2="56" stroke="#7dd3fc" stroke-width="1.2"/>'
    '</svg>'
)

st.markdown(
    '<div class="miaa-top">'
    '<div class="miaa-brand">'
    f'<img src="{LOGO_URL}" alt="MIAA">'
    '<div class="miaa-vsep"></div>'
    '<div class="miaa-titles">'
    '<h1>Sistema Integral de Monitoreo</h1>'
    '<p>Agua Potable para Aguascalientes</p>'
    '</div>'
    '</div>'
    '<div class="miaa-top-right">'
    f'{tank_svg}'
    '<div class="miaa-clock-card">'
    '<div class="miaa-clock-row"><span>📅</span><span id="live-date">26 Noviembre 2026</span></div>'
    '<div class="miaa-clock-row"><span>🕒</span><span id="live-clock">08:51:00 AM</span></div>'
    '</div>'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)

tiles_parts = ['<div class="miaa-grid">']
for item in SISTEMAS:
    tiles_parts.append(
        f'<div class="miaa-tile" style="--g:{item["glow"]};--gr:{item["glow_rgba"]};">'
        f'<a class="miaa-tile-link" href="{item["url"]}" target="_blank" aria-label="{item["titulo"].replace("<br>", " ")}"></a>'
        f'<div class="miaa-tile-icon">{item["icon"]}</div>'
        f'<div class="miaa-tile-text">'
        f'<div class="miaa-tile-title">{item["titulo"]}</div>'
        f'<div class="miaa-tile-desc">{item["descripcion"]}</div>'
        f'</div>'
        f'<div class="miaa-tile-arrow">&#10095;</div>'
        f'</div>'
    )
tiles_parts.append('</div>')
st.markdown("".join(tiles_parts), unsafe_allow_html=True)

st.markdown(
    '<div class="miaa-bottom-bar">'
    '<div class="miaa-bottom-left">'
    '<div class="miaa-bars">'
    '<span style="height:4px;"></span>'
    '<span style="height:7px;"></span>'
    '<span style="height:10px;"></span>'
    '<span style="height:13px;"></span>'
    '</div>'
    '<span><strong>MIAA</strong> &nbsp;|&nbsp; Innovación, Tecnología y Agua para Todos</span>'
    '</div>'
    '<div class="miaa-bottom-right">'
    '<span>⚙️ Configuración</span>'
    '<span class="miaa-sep">|</span>'
    '<span>ℹ️ Acerca de</span>'
    '<span class="miaa-sep">|</span>'
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
