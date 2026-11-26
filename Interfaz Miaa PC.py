import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Interfaz Miaa",
    page_icon="https://www.miaa.mx/favicon.ico",
    layout="wide",
    initial_sidebar_state="expanded"
)

SISTEMAS = [
    {
        "titulo": "SCADA<br>Pozos y Equipos",
        "descripcion": "Monitoreo y control de pozos y equipos",
        "url": "https://sistema-scada.streamlit.app/",
        "color_acento": "#00d4ff",
        "icono_svg": """<svg viewBox="0 0 120 110" width="96" height="88" xmlns="http://www.w3.org/2000/svg"><defs><linearGradient id="pumpGrad" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#00d4ff"/><stop offset="100%" stop-color="#0052cc"/></linearGradient></defs><rect x="42" y="10" width="66" height="44" rx="5" fill="#06182c" stroke="#00d4ff" stroke-width="2"/><polyline points="49,40 60,28 70,35 84,18 98,25" fill="none" stroke="#00f2fe" stroke-width="2.5" stroke-linecap="round"/><circle cx="84" cy="18" r="3" fill="#ffffff"/><rect x="14" y="48" width="54" height="34" rx="6" fill="url(#pumpGrad)" stroke="#7ae7ff" stroke-width="1.5"/><line x1="24" y1="53" x2="24" y2="77" stroke="#031222" stroke-width="2.5"/><line x1="33" y1="53" x2="33" y2="77" stroke="#031222" stroke-width="2.5"/><line x1="42" y1="53" x2="42" y2="77" stroke="#031222" stroke-width="2.5"/><line x1="51" y1="53" x2="51" y2="77" stroke="#031222" stroke-width="2.5"/><circle cx="82" cy="65" r="20" fill="#0b3b75" stroke="#00d4ff" stroke-width="2.5"/><circle cx="82" cy="65" r="9" fill="#041527" stroke="#00d4ff" stroke-width="2"/><rect x="76" y="34" width="12" height="14" fill="#0099ff" stroke="#7ae7ff" stroke-width="1.5"/><rect x="10" y="84" width="94" height="7" rx="2" fill="#1e4976"/></svg>"""
    },
    {
        "titulo": "Medidores<br>Inteligentes",
        "descripcion": "Lecturas y análisis de medidores",
        "url": "https://lecturas-hes.streamlit.app/",
        "color_acento": "#00e5ff",
        "icono_svg": """<svg viewBox="0 0 120 110" width="96" height="88" xmlns="http://www.w3.org/2000/svg"><defs><radialGradient id="meterBody" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#e2e8f0"/><stop offset="80%" stop-color="#94a3b8"/><stop offset="100%" stop-color="#475569"/></radialGradient></defs><path d="M 44 22 Q 60 8 76 22" fill="none" stroke="#00f2fe" stroke-width="3" stroke-linecap="round"/><path d="M 50 29 Q 60 19 70 29" fill="none" stroke="#00f2fe" stroke-width="3" stroke-linecap="round"/><rect x="10" y="56" width="100" height="18" rx="3" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/><rect x="16" y="51" width="10" height="28" rx="2" fill="#0369a1"/><rect x="94" y="51" width="10" height="28" rx="2" fill="#0369a1"/><circle cx="60" cy="65" r="30" fill="url(#meterBody)" stroke="#00d4ff" stroke-width="3"/><circle cx="60" cy="65" r="23" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/><rect x="42" y="53" width="36" height="12" rx="2" fill="#bae6fd"/><text x="60" y="62" font-family="monospace" font-size="8.5" font-weight="bold" fill="#0369a1" text-anchor="middle">000254.7</text><circle cx="60" cy="75" r="4" fill="#ef4444"/><path d="M 57 75 L 63 75" stroke="#ffffff" stroke-width="1.5"/></svg>"""
    },
    {
        "titulo": "Mapa y GIS",
        "descripcion": "Información geográfica y sectorización",
        "url": "https://miaa-sincronizador-ver-app.streamlit.app/",
        "color_acento": "#10b981",
        "icono_svg": """<svg viewBox="0 0 120 110" width="96" height="88" xmlns="http://www.w3.org/2000/svg"><polygon points="15,38 43,28 43,82 15,92" fill="#065f46" stroke="#34d399" stroke-width="1.5"/><polygon points="43,28 73,38 73,92 43,82" fill="#047857" stroke="#34d399" stroke-width="1.5"/><polygon points="73,38 103,28 103,82 73,92" fill="#059669" stroke="#34d399" stroke-width="1.5"/><polyline points="20,65 43,55 73,68 98,52" fill="none" stroke="#38bdf8" stroke-width="3" stroke-linecap="round"/><polyline points="35,35 55,62 65,85" fill="none" stroke="#a7f3d0" stroke-width="2" stroke-dasharray="3,2"/><path d="M 73 12 C 62 12 54 20 54 30 C 54 44 73 60 73 60 C 73 60 92 44 92 30 C 92 20 84 12 73 12 Z" fill="#ef4444" stroke="#ffffff" stroke-width="2"/><circle cx="73" cy="29" r="7" fill="#ffffff"/></svg>"""
    },
    {
        "titulo": "Mantenimiento",
        "descripcion": "Gestión de mantenimiento y fallas",
        "url": "https://incidencias-miaa.streamlit.app/",
        "color_acento": "#f59e0b",
        "icono_svg": """<svg viewBox="0 0 120 110" width="96" height="88" xmlns="http://www.w3.org/2000/svg"><defs><linearGradient id="metalGrad" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#f1f5f9"/><stop offset="50%" stop-color="#94a3b8"/><stop offset="100%" stop-color="#475569"/></linearGradient></defs><g transform="translate(56, 55)"><circle cx="0" cy="0" r="24" fill="none" stroke="url(#metalGrad)" stroke-width="11" stroke-dasharray="11 7.8"/><circle cx="0" cy="0" r="21" fill="#0a192f" stroke="#cbd5e1" stroke-width="3"/><circle cx="0" cy="0" r="11" fill="none" stroke="#f59e0b" stroke-width="2.5"/></g><g transform="rotate(-42 60 55)"><rect x="20" y="49" width="80" height="12" rx="4" fill="url(#metalGrad)" stroke="#1e293b" stroke-width="1.5"/><circle cx="20" cy="55" r="11" fill="url(#metalGrad)" stroke="#1e293b" stroke-width="1.5"/><rect x="9" y="51" width="11" height="8" fill="#0a192f"/><circle cx="100" cy="55" r="11" fill="url(#metalGrad)" stroke="#1e293b" stroke-width="1.5"/><rect x="100" y="51" width="11" height="8" fill="#0a192f"/></g></svg>"""
    },
    {
        "titulo": "Tableros y Reportes",
        "descripcion": "Indicadores y reportes ejecutivos",
        "url": "https://tableros-miaa.streamlit.app/",
        "color_acento": "#8b5cf6",
        "icono_svg": """<svg viewBox="0 0 120 110" width="96" height="88" xmlns="http://www.w3.org/2000/svg"><rect x="16" y="18" width="88" height="56" rx="6" fill="#091526" stroke="#60a5fa" stroke-width="2.5"/><polygon points="52,74 68,74 74,88 46,88" fill="#3b82f6"/><rect x="38" y="88" width="44" height="5" rx="2" fill="#93c5fd"/><rect x="26" y="52" width="7" height="14" rx="1" fill="#38bdf8"/><rect x="37" y="42" width="7" height="24" rx="1" fill="#00f2fe"/><rect x="48" y="47" width="7" height="19" rx="1" fill="#818cf8"/><rect x="59" y="33" width="7" height="33" rx="1" fill="#a78bfa"/><circle cx="84" cy="46" r="12" fill="none" stroke="#1e3a8a" stroke-width="6"/><circle cx="84" cy="46" r="12" fill="none" stroke="#00d4ff" stroke-width="6" stroke-dasharray="48 30"/><polyline points="26,38 42,29 58,32 72,24" fill="none" stroke="#34d399" stroke-width="2" stroke-linecap="round"/></svg>"""
    },
    {
        "titulo": "HES - Consumo",
        "descripcion": "Lecturas y análisis de consumo",
        "url": "https://hes-consumo.streamlit.app/",
        "color_acento": "#06b6d4",
        "icono_svg": """<svg viewBox="0 0 120 110" width="96" height="88" xmlns="http://www.w3.org/2000/svg"><defs><linearGradient id="dropGrad" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#38bdf8"/><stop offset="100%" stop-color="#0284c7"/></linearGradient></defs><polygon points="52,22 16,52 24,52 24,88 80,88 80,52 88,52" fill="#cbd5e1" stroke="#38bdf8" stroke-width="2"/><polygon points="52,18 12,51 18,56 52,27 86,56 92,51" fill="#0284c7"/><rect x="34" y="60" width="14" height="28" rx="2" fill="#0f172a"/><rect x="56" y="56" width="14" height="14" rx="1" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/><line x1="63" y1="56" x2="63" y2="70" stroke="#38bdf8" stroke-width="1"/><line x1="56" y1="63" x2="70" y2="63" stroke="#38bdf8" stroke-width="1"/><path d="M 78 24 Q 90 14 102 24" fill="none" stroke="#00f2fe" stroke-width="3" stroke-linecap="round"/><path d="M 83 31 Q 90 24 97 31" fill="none" stroke="#00f2fe" stroke-width="3" stroke-linecap="round"/><path d="M 90 46 C 90 46 74 66 74 78 C 74 87 81 94 90 94 C 99 94 106 87 106 78 C 106 66 90 46 90 46 Z" fill="url(#dropGrad)" stroke="#e0f2fe" stroke-width="2"/><path d="M 82 76 Q 82 84 88 87" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round" opacity="0.8"/></svg>"""
    }
]

LOGO_URL = "https://raw.githubusercontent.com/Miaa-Aguascalientes/Logos/38504978c8f77a4dac38ad476f74dbdee6af2cad/LogoMIAA.svg"

st.markdown(f"""<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap');

/* Mantener header transparente y botón de sidebar visible */
[data-testid="stHeader"] {{
    background: transparent !important;
}}
[data-testid="stToolbar"] {{
    right: 1rem;
}}
[data-testid="stSidebar"] {{
    background-color: #031022 !important;
    border-right: 1px solid rgba(0, 212, 255, 0.25) !important;
    min-width: 250px !important;
}}
[data-testid="stSidebarCollapseButton"],
[data-testid="collapsedControl"] {{
    color: #00d4ff !important;
    background-color: rgba(6, 24, 48, 0.85) !important;
    border: 1px solid rgba(0, 212, 255, 0.35) !important;
    border-radius: 8px !important;
    visibility: visible !important;
    opacity: 1 !important;
}}

#MainMenu {{visibility: hidden;}}
footer {{visibility: hidden;}}

.stApp {{
    background:
        radial-gradient(ellipse at 75% 18%, rgba(0, 180, 255, 0.22) 0%, transparent 45%),
        radial-gradient(ellipse at 20% 85%, rgba(0, 140, 255, 0.28) 0%, transparent 50%),
        linear-gradient(180deg, #020b18 0%, #041d3a 35%, #03152b 70%, #020c1b 100%);
    font-family: 'Inter', sans-serif;
    color: #ffffff;
}}

.block-container {{
    padding-top: 1rem !important;
    padding-bottom: 4.5rem !important;
    padding-left: 2.2rem !important;
    padding-right: 2.2rem !important;
    max-width: 1500px;
}}

.miaa-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 8px 4px 20px 4px;
    border-bottom: 1px solid rgba(0, 212, 255, 0.18);
    margin-bottom: 24px;
}}

.header-left {{
    display: flex;
    align-items: center;
    gap: 20px;
}}

.miaa-logo {{
    height: 58px;
    width: auto;
    filter: brightness(0) invert(1) drop-shadow(0 0 10px rgba(0, 212, 255, 0.45));
}}

.header-divider {{
    width: 2px;
    height: 48px;
    background: linear-gradient(180deg, transparent, rgba(255,255,255,0.65), transparent);
}}

.header-titles h1 {{
    margin: 0;
    font-size: 1.55rem;
    font-weight: 700;
    color: #ffffff;
    line-height: 1.2;
}}

.header-titles p {{
    margin: 4px 0 0 0;
    font-size: 1.08rem;
    font-weight: 400;
    color: #a5d8ff;
}}

.header-right-group {{
    display: flex;
    align-items: center;
    gap: 20px;
}}

.tank-watermark {{
    opacity: 0.78;
    filter: drop-shadow(0 0 15px rgba(0, 195, 255, 0.35));
}}

.datetime-box {{
    background: rgba(6, 24, 48, 0.72);
    border: 1px solid rgba(0, 212, 255, 0.3);
    border-radius: 12px;
    padding: 9px 16px;
    backdrop-filter: blur(10px);
    min-width: 190px;
}}

.dt-row {{
    display: flex;
    align-items: center;
    gap: 9px;
    color: #e2e8f0;
    font-size: 0.9rem;
    margin-bottom: 4px;
}}

.dt-row:last-child {{
    margin-bottom: 0;
    font-size: 1.05rem;
    font-weight: 700;
    color: #ffffff;
}}

a.system-card {{
    text-decoration: none !important;
    color: inherit !important;
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: linear-gradient(135deg, rgba(13, 38, 70, 0.75) 0%, rgba(6, 20, 40, 0.88) 100%);
    border: 1px solid rgba(120, 200, 255, 0.28);
    border-radius: 18px;
    padding: 18px 20px;
    min-height: 168px;
    margin-bottom: 18px;
    backdrop-filter: blur(12px);
    box-shadow: 0 10px 28px rgba(0, 0, 0, 0.5), inset 0 1px 1px rgba(255, 255, 255, 0.16);
    position: relative;
    overflow: hidden;
    transition: all 0.25s ease;
}}

a.system-card::after {{
    content: "";
    position: absolute;
    bottom: 0;
    left: 8%;
    right: 8%;
    height: 4px;
    background: var(--accent-color);
    border-radius: 4px 4px 0 0;
    box-shadow: 0 -2px 14px var(--accent-color), 0 0 22px var(--accent-color);
}}

a.system-card:hover {{
    transform: translateY(-5px);
    border-color: var(--accent-color);
    box-shadow: 0 14px 34px rgba(0, 0, 0, 0.65), 0 0 20px rgba(0, 212, 255, 0.22);
}}

.card-icon-box {{
    flex: 0 0 104px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: rgba(3, 14, 28, 0.5);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 14px;
    height: 118px;
    padding: 6px;
}}

.card-text-box {{
    flex: 1;
    padding: 0 12px 0 16px;
}}

.card-title {{
    font-size: 1.22rem;
    font-weight: 700;
    color: #ffffff;
    line-height: 1.2;
    margin-bottom: 6px;
}}

.card-desc {{
    font-size: 0.88rem;
    color: #cbd5e1;
    line-height: 1.3;
}}

.card-arrow {{
    flex: 0 0 34px;
    width: 34px;
    height: 34px;
    border-radius: 50%;
    border: 2px solid var(--accent-color);
    display: flex;
    align-items: center;
    justify-content: center;
    color: #ffffff;
    font-size: 1rem;
    font-weight: bold;
    align-self: flex-end;
    background: rgba(0, 0, 0, 0.35);
}}

.miaa-footer {{
    position: fixed;
    bottom: 0;
    left: 0;
    right: 220px;
    height: 42px;
    background: rgba(3, 13, 27, 0.92);
    border-top: 1px solid rgba(0, 212, 255, 0.25);
    backdrop-filter: blur(12px);
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 28px;
    z-index: 990;
    font-size: 0.85rem;
    color: #cbd5e1;
}}

.footer-left {{
    display: flex;
    align-items: center;
    gap: 10px;
}}

.signal-bars {{
    display: flex;
    align-items: flex-end;
    gap: 3px;
    height: 14px;
}}

.signal-bars span {{
    width: 3px;
    background: #00d4ff;
    border-radius: 1px;
}}

.footer-right {{
    display: flex;
    align-items: center;
    gap: 16px;
}}

.footer-item {{
    display: flex;
    align-items: center;
    gap: 6px;
    color: #e2e8f0;
}}

.footer-sep {{
    color: rgba(255, 255, 255, 0.25);
}}
</style>""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown(f"""<div style="text-align:center; padding: 10px 0 16px 0; border-bottom: 1px solid rgba(0,212,255,0.2);"><img src="{LOGO_URL}" style="height: 44px; filter: brightness(0) invert(1);"><p style="color:#7dd3fc; font-size:0.82rem; margin:8px 0 0 0;">Portal Central de Sistemas</p></div>""", unsafe_allow_html=True)
    st.markdown("### Accesos Directos")
    for s in SISTEMAS:
        titulo_limpio = s["titulo"].replace("<br>", " ")
        st.markdown(f"- [{titulo_limpio}]({s['url']})")
    st.markdown("---")
    st.caption("Dirección de Planeación • Subdirección de Tecnología e Innovación")

st.markdown(f"""<div class="miaa-header"><div class="header-left"><img src="{LOGO_URL}" alt="Logo MIAA" class="miaa-logo"><div class="header-divider"></div><div class="header-titles"><h1>Sistema Integral de Monitoreo</h1><p>Agua Potable para Aguascalientes</p></div></div><div class="header-right-group"><svg class="tank-watermark" width="78" height="68" viewBox="0 0 90 80" xmlns="http://www.w3.org/2000/svg"><path d="M 20 12 Q 45 4 70 12 L 70 36 Q 45 42 20 36 Z" fill="#1e4976" stroke="#38bdf8" stroke-width="1.5"/><text x="45" y="28" font-family="Inter, sans-serif" font-size="11" font-weight="800" fill="#020b18" text-anchor="middle">miaa</text><line x1="25" y1="37" x2="21" y2="75" stroke="#38bdf8" stroke-width="2"/><line x1="38" y1="39" x2="36" y2="75" stroke="#38bdf8" stroke-width="2"/><line x1="52" y1="39" x2="54" y2="75" stroke="#38bdf8" stroke-width="2"/><line x1="65" y1="37" x2="69" y2="75" stroke="#38bdf8" stroke-width="2"/><line x1="23" y1="55" x2="67" y2="55" stroke="#38bdf8" stroke-width="1.2"/></svg><div class="datetime-box"><div class="dt-row"><span>📅</span><span id="live-date">26 Noviembre 2026</span></div><div class="dt-row"><span>🕒</span><span id="live-clock">08:47:00 AM</span></div></div></div></div>""", unsafe_allow_html=True)

for fila in range(0, len(SISTEMAS), 3):
    cols = st.columns(3, gap="medium")
    for idx, col in enumerate(cols):
        if fila + idx < len(SISTEMAS):
            sys_item = SISTEMAS[fila + idx]
            with col:
                card_html = (
                    f'<a href="{sys_item["url"]}" target="_blank" class="system-card" style="--accent-color: {sys_item["color_acento"]};">'
                    f'<div class="card-icon-box">{sys_item["icono_svg"]}</div>'
                    f'<div class="card-text-box">'
                    f'<div class="card-title">{sys_item["titulo"]}</div>'
                    f'<div class="card-desc">{sys_item["descripcion"]}</div>'
                    f'</div>'
                    f'<div class="card-arrow">&#10095;</div>'
                    f'</a>'
                )
                st.markdown(card_html, unsafe_allow_html=True)

st.markdown("""<div class="miaa-footer"><div class="footer-left"><div class="signal-bars"><span style="height:5px;"></span><span style="height:8px;"></span><span style="height:11px;"></span><span style="height:14px;"></span></div><span><strong>MIAA</strong> &nbsp;|&nbsp; Innovación, Tecnología y Agua para Todos</span></div><div class="footer-right"><div class="footer-item">⚙️ <span>Configuración</span></div><span class="footer-sep">|</span><div class="footer-item">ℹ️ <span>Acerca de</span></div><span class="footer-sep">|</span><div class="footer-item">⏻ <span>Cerrar Sesión</span></div></div></div>""", unsafe_allow_html=True)

components.html("""
<script>
    function updateClock() {
        const doc = window.parent.document;
        const dateEl = doc.getElementById('live-date');
        const clockEl = doc.getElementById('live-clock');
        if (!dateEl || !clockEl) return;

        const now = new Date();
        const meses = [
            "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
            "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
        ];
        const dia = String(now.getDate()).padStart(2, '0');
        const mes = meses[now.getMonth()];
        const anio = now.getFullYear();
        dateEl.textContent = `${dia} ${mes} ${anio}`;

        let horas = now.getHours();
        const minutos = String(now.getMinutes()).padStart(2, '0');
        const segundos = String(now.getSeconds()).padStart(2, '0');
        const ampm = horas >= 12 ? 'PM' : 'AM';
        horas = horas % 12;
        horas = horas ? horas : 12;
        const horasStr = String(horas).padStart(2, '0');
        clockEl.textContent = `${horasStr}:${minutos}:${segundos} ${ampm}`;
    }
    setInterval(updateClock, 1000);
    updateClock();
</script>
""", height=0, width=0)
