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


def img_b64(ruta: str) -> str:
    p = Path(ruta)
    if p.exists():
        ext = p.suffix.lower().lstrip(".")
        if ext == "jpg":
            ext = "jpeg"
        return f"data:image/{ext};base64,{base64.b64encode(p.read_bytes()).decode('utf-8')}"
    return ""


FONDO_B64 = img_b64("assets/fondo_miaa.jpg")

SISTEMAS = [
    {
        "titulo": "SCADA<br>Pozos y Equipos",
        "titulo_plano": "SCADA Pozos y Equipos",
        "descripcion": "Monitoreo y control de pozos y equipos",
        "url": "https://sistema-scada.streamlit.app/",
        "imagen": img_b64("assets/icon_scada.png"),
        "glow": "#00d4ff",
        "svg": (
            '<svg viewBox="0 0 120 100" width="92" height="78" xmlns="http://www.w3.org/2000/svg">'
            '<rect x="44" y="8" width="66" height="42" rx="5" fill="#071b33" stroke="#38bdf8" stroke-width="2"/>'
            '<polyline points="50,38 62,25 72,32 86,16 102,23" fill="none" stroke="#22d3ee" stroke-width="2.5"/>'
            '<rect x="12" y="44" width="50" height="32" rx="6" fill="#0284c7" stroke="#bae6fd" stroke-width="1.5"/>'
            '<circle cx="78" cy="60" r="18" fill="#0c4a6e" stroke="#38bdf8" stroke-width="2.5"/>'
            '<circle cx="78" cy="60" r="7" fill="#041324" stroke="#7dd3fc" stroke-width="2"/>'
            '<rect x="8" y="80" width="96" height="6" rx="2" fill="#1e3a8a"/>'
            '</svg>'
        )
    },
    {
        "titulo": "Medidores<br>Inteligentes",
        "titulo_plano": "Medidores Inteligentes",
        "descripcion": "Lecturas y análisis de medidores",
        "url": "https://lecturas-hes.streamlit.app/",
        "imagen": img_b64("assets/icon_medidores.png"),
        "glow": "#00e5ff",
        "svg": (
            '<svg viewBox="0 0 120 100" width="92" height="78" xmlns="http://www.w3.org/2000/svg">'
            '<path d="M 44 18 Q 60 6 76 18" fill="none" stroke="#22d3ee" stroke-width="3" stroke-linecap="round"/>'
            '<path d="M 50 25 Q 60 16 70 25" fill="none" stroke="#22d3ee" stroke-width="3" stroke-linecap="round"/>'
            '<rect x="10" y="52" width="100" height="16" rx="3" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>'
            '<circle cx="60" cy="60" r="27" fill="#cbd5e1" stroke="#38bdf8" stroke-width="3"/>'
            '<circle cx="60" cy="60" r="20" fill="#0f172a" stroke="#7dd3fc" stroke-width="1.5"/>'
            '<rect x="43" y="50" width="34" height="10" rx="2" fill="#bae6fd"/>'
            '<text x="60" y="58" font-family="monospace" font-size="7.5" font-weight="bold" fill="#0c4a6e" text-anchor="middle">000254.7</text>'
            '<circle cx="60" cy="69" r="4" fill="#ef4444"/>'
            '</svg>'
        )
    },
    {
        "titulo": "Mapa y GIS",
        "titulo_plano": "Mapa y GIS",
        "descripcion": "Información geográfica y sectorización",
        "url": "https://miaa-sincronizador-ver-app.streamlit.app/",
        "imagen": img_b64("assets/icon_gis.png"),
        "glow": "#10b981",
        "svg": (
            '<svg viewBox="0 0 120 100" width="92" height="78" xmlns="http://www.w3.org/2000/svg">'
            '<polygon points="16,36 44,26 44,78 16,88" fill="#065f46" stroke="#34d399" stroke-width="1.5"/>'
            '<polygon points="44,26 74,36 74,88 44,78" fill="#047857" stroke="#34d399" stroke-width="1.5"/>'
            '<polygon points="74,36 104,26 104,78 74,88" fill="#059669" stroke="#34d399" stroke-width="1.5"/>'
            '<polyline points="22,60 44,50 74,63 98,48" fill="none" stroke="#38bdf8" stroke-width="3"/>'
            '<path d="M 74 10 C 64 10 56 18 56 28 C 56 41 74 56 74 56 C 74 56 92 41 92 28 C 92 18 84 10 74 10 Z" fill="#ef4444" stroke="#ffffff" stroke-width="2"/>'
            '<circle cx="74" cy="27" r="6" fill="#ffffff"/>'
            '</svg>'
        )
    },
    {
        "titulo": "Mantenimiento",
        "titulo_plano": "Mantenimiento",
        "descripcion": "Gestión de mantenimiento y fallas",
        "url": "https://incidencias-miaa.streamlit.app/",
        "imagen": img_b64("assets/icon_mantenimiento.png"),
        "glow": "#f59e0b",
        "svg": (
            '<svg viewBox="0 0 120 100" width="92" height="78" xmlns="http://www.w3.org/2000/svg">'
            '<circle cx="54" cy="50" r="22" fill="none" stroke="#cbd5e1" stroke-width="10" stroke-dasharray="10 7"/>'
            '<circle cx="54" cy="50" r="19" fill="#07192f" stroke="#94a3b8" stroke-width="2"/>'
            '<circle cx="54" cy="50" r="9" fill="none" stroke="#f59e0b" stroke-width="2.5"/>'
            '<g transform="rotate(-40 62 50)">'
            '<rect x="22" y="45" width="80" height="10" rx="3" fill="#e2e8f0" stroke="#1e293b" stroke-width="1.5"/>'
            '<circle cx="22" cy="50" r="10" fill="#e2e8f0" stroke="#1e293b" stroke-width="1.5"/>'
            '<circle cx="102" cy="50" r="10" fill="#e2e8f0" stroke="#1e293b" stroke-width="1.5"/>'
            '</g>'
            '</svg>'
        )
    },
    {
        "titulo": "Tableros y Reportes",
        "titulo_plano": "Tableros y Reportes",
        "descripcion": "Indicadores y reportes ejecutivos",
        "url": "https://tableros-miaa.streamlit.app/",
        "imagen": img_b64("assets/icon_tableros.png"),
        "glow": "#8b5cf6",
        "svg": (
            '<svg viewBox="0 0 120 100" width="92" height="78" xmlns="http://www.w3.org/2000/svg">'
            '<rect x="16" y="14" width="88" height="52" rx="6" fill="#09182e" stroke="#60a5fa" stroke-width="2.5"/>'
            '<polygon points="51,66 69,66 75,79 45,79" fill="#3b82f6"/>'
            '<rect x="38" y="79" width="44" height="5" rx="2" fill="#93c5fd"/>'
            '<rect x="26" y="46" width="7" height="12" rx="1" fill="#38bdf8"/>'
            '<rect x="37" y="36" width="7" height="22" rx="1" fill="#22d3ee"/>'
            '<rect x="48" y="41" width="7" height="17" rx="1" fill="#818cf8"/>'
            '<rect x="59" y="28" width="7" height="30" rx="1" fill="#a78bfa"/>'
            '<circle cx="84" cy="41" r="11" fill="none" stroke="#1e3a8a" stroke-width="5"/>'
            '<circle cx="84" cy="41" r="11" fill="none" stroke="#00d4ff" stroke-width="5" stroke-dasharray="42 28"/>'
            '</svg>'
        )
    },
    {
        "titulo": "HES - Consumo",
        "titulo_plano": "HES - Consumo",
        "descripcion": "Lecturas y análisis de consumo",
        "url": "https://hes-consumo.streamlit.app/",
        "imagen": img_b64("assets/icon_hes.png"),
        "glow": "#06b6d4",
        "svg": (
            '<svg viewBox="0 0 120 100" width="92" height="78" xmlns="http://www.w3.org/2000/svg">'
            '<polygon points="50,18 16,46 24,46 24,80 76,80 76,46 84,46" fill="#cbd5e1" stroke="#38bdf8" stroke-width="2"/>'
            '<polygon points="50,14 12,45 18,50 50,23 82,50 88,45" fill="#0284c7"/>'
            '<rect x="34" y="54" width="12" height="26" rx="2" fill="#0f172a"/>'
            '<path d="M 78 20 Q 90 10 102 20" fill="none" stroke="#22d3ee" stroke-width="3" stroke-linecap="round"/>'
            '<path d="M 90 42 C 90 42 75 60 75 72 C 75 81 82 88 90 88 C 98 88 105 81 105 72 C 105 60 90 42 90 42 Z" fill="#0284c7" stroke="#e0f2fe" stroke-width="2"/>'
            '</svg>'
        )
    }
]

fondo_style = (
    f"background-image:url('{FONDO_B64}');background-size:cover;background-position:center;background-attachment:fixed;"
    if FONDO_B64
    else "background:linear-gradient(180deg,#020b18 0%,#052245 45%,#03152c 100%);"
)

st.markdown(
    f'<div style="position:fixed;inset:0;z-index:-1;{fondo_style}"></div>'
    '<div style="position:fixed;inset:0;z-index:-1;background:radial-gradient(ellipse at 75% 18%,rgba(0,180,255,0.22) 0%,transparent 48%),rgba(2,10,22,0.52);"></div>',
    unsafe_allow_html=True
)

with st.sidebar:
    st.markdown(
        f'<div style="text-align:center;padding:8px 0 12px 0;border-bottom:1px solid rgba(56,189,248,0.25);">'
        f'<img src="{LOGO_URL}" width="150" height="44" style="width:150px;height:44px;object-fit:contain;filter:brightness(0) invert(1);">'
        f'</div>',
        unsafe_allow_html=True
    )
    st.markdown("#### Sistemas")
    for s in SISTEMAS:
        st.markdown(
            f'<div style="margin:6px 0;"><a href="{s["url"]}" target="_blank" '
            f'style="color:#bae6fd;text-decoration:none;font-size:0.92rem;">• {s["titulo_plano"]}</a></div>',
            unsafe_allow_html=True
        )

tank_svg = (
    '<svg width="74" height="64" viewBox="0 0 90 80" style="width:74px;height:64px;opacity:0.8;" xmlns="http://www.w3.org/2000/svg">'
    '<path d="M 18 12 Q 45 4 72 12 L 72 36 Q 45 42 18 36 Z" fill="#1e4976" stroke="#7dd3fc" stroke-width="1.5"/>'
    '<text x="45" y="28" font-family="sans-serif" font-size="11" font-weight="800" fill="#041528" text-anchor="middle">miaa</text>'
    '<line x1="24" y1="37" x2="20" y2="75" stroke="#7dd3fc" stroke-width="2"/>'
    '<line x1="37" y1="39" x2="35" y2="75" stroke="#7dd3fc" stroke-width="2"/>'
    '<line x1="53" y1="39" x2="55" y2="75" stroke="#7dd3fc" stroke-width="2"/>'
    '<line x1="66" y1="37" x2="70" y2="75" stroke="#7dd3fc" stroke-width="2"/>'
    '<line x1="22" y1="56" x2="68" y2="56" stroke="#7dd3fc" stroke-width="1.2"/>'
    '</svg>'
)

st.markdown(
    f'<div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:16px;'
    f'padding:6px 4px 16px 4px;border-bottom:1px solid rgba(125,211,252,0.22);margin-bottom:20px;">'
    f'<div style="display:flex;align-items:center;gap:18px;">'
    f'<img src="{LOGO_URL}" width="175" height="54" alt="MIAA" '
    f'style="width:175px;height:54px;object-fit:contain;filter:brightness(0) invert(1);">'
    f'<div style="width:2px;height:46px;background:rgba(255,255,255,0.55);"></div>'
    f'<div>'
    f'<div style="font-size:1.5rem;font-weight:700;color:#ffffff;line-height:1.15;">Sistema Integral de Monitoreo</div>'
    f'<div style="font-size:1.05rem;font-weight:400;color:#bae6fd;margin-top:3px;">Agua Potable para Aguascalientes</div>'
    f'</div>'
    f'</div>'
    f'<div style="display:flex;align-items:center;gap:16px;">'
    f'{tank_svg}'
    f'<div style="background:rgba(4,18,38,0.82);border:1px solid rgba(125,211,252,0.35);border-radius:10px;padding:8px 14px;min-width:185px;">'
    f'<div style="color:#e2e8f0;font-size:0.86rem;margin-bottom:3px;">📅 <span id="live-date">26 Noviembre 2026</span></div>'
    f'<div style="color:#ffffff;font-size:1.02rem;font-weight:700;">🕒 <span id="live-clock">08:55:00 AM</span></div>'
    f'</div>'
    f'</div>'
    f'</div>',
    unsafe_allow_html=True
)

for fila in range(0, len(SISTEMAS), 3):
    cols = st.columns(3, gap="medium")
    for idx, col in enumerate(cols):
        if fila + idx < len(SISTEMAS):
            item = SISTEMAS[fila + idx]
            if item["imagen"]:
                media_html = (
                    f'<img src="{item["imagen"]}" width="104" height="96" '
                    f'style="width:104px;height:96px;object-fit:cover;border-radius:10px;">'
                )
            else:
                media_html = item["svg"]

            card_html = (
                f'<a href="{item["url"]}" target="_blank" style="text-decoration:none;display:block;margin-bottom:14px;">'
                f'<div style="position:relative;display:flex;align-items:center;justify-content:space-between;gap:14px;'
                f'height:154px;padding:14px 18px;border-radius:16px;'
                f'background:linear-gradient(145deg,rgba(14,42,78,0.82) 0%,rgba(5,18,36,0.92) 100%);'
                f'border:1.5px solid rgba(147,197,253,0.35);'
                f'box-shadow:0 10px 24px rgba(0,0,0,0.55),inset 0 -4px 14px -2px {item["glow"]};overflow:hidden;">'
                f'<div style="flex:0 0 104px;width:104px;height:104px;display:flex;align-items:center;justify-content:center;'
                f'background:rgba(3,14,29,0.65);border:1px solid rgba(186,230,253,0.16);border-radius:12px;">'
                f'{media_html}'
                f'</div>'
                f'<div style="flex:1;min-width:0;">'
                f'<div style="font-size:1.18rem;font-weight:700;color:#ffffff;line-height:1.18;margin-bottom:6px;">{item["titulo"]}</div>'
                f'<div style="font-size:0.86rem;font-weight:400;color:#cbd5e1;line-height:1.28;">{item["descripcion"]}</div>'
                f'</div>'
                f'<div style="flex:0 0 32px;width:32px;height:32px;border-radius:50%;border:2px solid {item["glow"]};'
                f'display:flex;align-items:center;justify-content:center;color:#ffffff;font-size:0.95rem;font-weight:700;'
                f'align-self:flex-end;background:rgba(2,11,23,0.6);">&#10095;</div>'
                f'</div>'
                f'</a>'
            )
            col.markdown(card_html, unsafe_allow_html=True)

st.markdown(
    '<div style="margin-top:16px;padding:10px 18px;border-radius:10px;'
    'background:rgba(2,11,23,0.85);border:1px solid rgba(125,211,252,0.22);'
    'display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;'
    'font-size:0.84rem;color:#cbd5e1;">'
    '<div><strong style="color:#ffffff;">MIAA</strong> &nbsp;|&nbsp; Innovación, Tecnología y Agua para Todos</div>'
    '<div style="display:flex;gap:14px;">'
    '<span>⚙️ Configuración</span><span style="opacity:0.35;">|</span>'
    '<span>ℹ️ Acerca de</span><span style="opacity:0.35;">|</span>'
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
