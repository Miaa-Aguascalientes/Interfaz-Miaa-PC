import base64
import io
from pathlib import Path
from PIL import Image
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Interfaz Miaa",
    page_icon="https://www.miaa.mx/favicon.ico",
    layout="wide",
    initial_sidebar_state="collapsed"
)

LOGO_URL = "https://raw.githubusercontent.com/Miaa-Aguascalientes/Logos/38504978c8f77a4dac38ad476f74dbdee6af2cad/LogoMIAA.svg"


def _img_file_to_b64(path: Path) -> str:
    buf = io.BytesIO()
    with Image.open(path) as im:
        im = im.convert("RGB")
        im.save(buf, format="JPEG", quality=92)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode("ascii")


@st.cache_data(show_spinner=False)
def cargar_recursos_visuales() -> dict:
    """
    Si colocas una imagen de referencia en assets/referencia.jpg (o .png),
    recorta automáticamente el fondo y las 6 miniaturas de las tarjetas.
    Si no existe, devuelve cadenas vacías para usar el estilo HUD degradado.
    """
    recursos = {
        "bg": "",
        "icons": [""] * 6
    }
    candidatos = [
        Path("assets/referencia.jpg"),
        Path("assets/referencia.png"),
        Path("assets/fondo.jpg"),
        Path("assets/fondo.png"),
    ]
    ref_path = next((p for p in candidatos if p.exists()), None)
    if not ref_path:
        return recursos

    with Image.open(ref_path) as im:
        im = im.convert("RGB")
        w, h = im.size

        # Fondo sin tarjetas (franja superior con tanque + franja inferior de agua)
        top_strip = im.crop((0, 0, w, int(h * 0.25)))
        bot_strip = im.crop((0, int(h * 0.78), w, h))
        mid_strip = im.crop((0, int(h * 0.24), w, int(h * 0.79))).resize((w, int(h * 0.54)))

        bg_canvas = Image.new("RGB", (w, h), (4, 24, 52))
        bg_canvas.paste(top_strip, (0, 0))
        bg_canvas.paste(mid_strip, (0, int(h * 0.25)))
        bg_canvas.paste(bot_strip, (0, h - bot_strip.height))

        bg_buf = io.BytesIO()
        bg_canvas.save(bg_buf, format="JPEG", quality=92)
        recursos["bg"] = "data:image/jpeg;base64," + base64.b64encode(bg_buf.getvalue()).decode("ascii")

        # Recorte aproximado de las 6 miniaturas de tarjetas (3 columnas x 2 filas)
        boxes = [
            (0.055, 0.285, 0.142, 0.485),
            (0.382, 0.285, 0.468, 0.485),
            (0.708, 0.285, 0.795, 0.485),
            (0.055, 0.525, 0.142, 0.725),
            (0.382, 0.525, 0.468, 0.725),
            (0.708, 0.525, 0.795, 0.725),
        ]
        for idx, (x0, y0, x1, y1) in enumerate(boxes):
            crop = im.crop((int(w * x0), int(h * y0), int(w * x1), int(h * y1)))
            cbuf = io.BytesIO()
            crop.save(cbuf, format="JPEG", quality=92)
            recursos["icons"][idx] = "data:image/jpeg;base64," + base64.b64encode(cbuf.getvalue()).decode("ascii")

    return recursos


RES = cargar_recursos_visuales()

TARJETAS = [
    {
        "titulo": "SCADA<br>Pozos y Equipos",
        "desc": "Monitoreo y control<br>de pozos y equipos",
        "url": "https://sistema-scada.streamlit.app/",
        "color": "#00d4ff",
        "rgb": "0, 212, 255",
        "img": RES["icons"][0],
        "svg": '<svg viewBox="0 0 96 84" width="68" height="60" xmlns="http://www.w3.org/2000/svg"><rect x="36" y="8" width="52" height="34" rx="4" fill="#061930" stroke="#38bdf8" stroke-width="2"/><polyline points="42,32 52,21 60,27 72,14 82,20" fill="none" stroke="#22d3ee" stroke-width="2.5"/><rect x="10" y="38" width="40" height="26" rx="5" fill="#0284c7" stroke="#bae6fd" stroke-width="1.5"/><circle cx="64" cy="51" r="15" fill="#0c4a6e" stroke="#38bdf8" stroke-width="2.2"/><circle cx="64" cy="51" r="6" fill="#041324" stroke="#7dd3fc" stroke-width="1.8"/><rect x="8" y="67" width="78" height="5" rx="2" fill="#1e3a8a"/></svg>'
    },
    {
        "titulo": "Medidores<br>Inteligentes",
        "desc": "Lecturas y análisis<br>de medidores",
        "url": "#medidores",
        "color": "#00e5ff",
        "rgb": "0, 229, 255",
        "img": RES["icons"][1],
        "svg": '<svg viewBox="0 0 96 84" width="68" height="60" xmlns="http://www.w3.org/2000/svg"><path d="M 35 15 Q 48 5 61 15" fill="none" stroke="#22d3ee" stroke-width="2.5" stroke-linecap="round"/><path d="M 40 21 Q 48 14 56 21" fill="none" stroke="#22d3ee" stroke-width="2.5" stroke-linecap="round"/><rect x="8" y="42" width="80" height="13" rx="2.5" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/><circle cx="48" cy="49" r="22" fill="#cbd5e1" stroke="#38bdf8" stroke-width="2.5"/><circle cx="48" cy="49" r="16" fill="#0f172a" stroke="#7dd3fc" stroke-width="1.2"/><rect x="34" y="41" width="28" height="8.5" rx="1.5" fill="#bae6fd"/><text x="48" y="47.5" font-family="monospace" font-size="6.2" font-weight="bold" fill="#0c4a6e" text-anchor="middle">000254.7</text><circle cx="48" cy="56.5" r="3.2" fill="#ef4444"/></svg>'
    },
    {
        "titulo": "Mapa y GIS",
        "desc": "Información geográfica<br>y sectorización",
        "url": "#gis",
        "color": "#10b981",
        "rgb": "16, 185, 129",
        "img": RES["icons"][2],
        "svg": '<svg viewBox="0 0 96 84" width="68" height="60" xmlns="http://www.w3.org/2000/svg"><polygon points="12,30 35,22 35,66 12,74" fill="#065f46" stroke="#34d399" stroke-width="1.3"/><polygon points="35,22 60,30 60,74 35,66" fill="#047857" stroke="#34d399" stroke-width="1.3"/><polygon points="60,30 84,22 84,66 60,74" fill="#059669" stroke="#34d399" stroke-width="1.3"/><polyline points="17,50 35,42 60,53 80,40" fill="none" stroke="#38bdf8" stroke-width="2.5"/><path d="M 60 8 C 52 8 45 14 45 23 C 45 34 60 47 60 47 C 60 47 75 34 75 23 C 75 14 68 8 60 8 Z" fill="#ef4444" stroke="#ffffff" stroke-width="1.8"/><circle cx="60" cy="22" r="5" fill="#ffffff"/></svg>'
    },
    {
        "titulo": "Mantenimiento",
        "desc": "Gestión de<br>mantenimiento y fallas",
        "url": "#mantenimiento",
        "color": "#f59e0b",
        "rgb": "245, 158, 11",
        "img": RES["icons"][3],
        "svg": '<svg viewBox="0 0 96 84" width="68" height="60" xmlns="http://www.w3.org/2000/svg"><circle cx="44" cy="42" r="18" fill="none" stroke="#cbd5e1" stroke-width="8.5" stroke-dasharray="8 5.8"/><circle cx="44" cy="42" r="15.5" fill="#07192f" stroke="#94a3b8" stroke-width="1.8"/><circle cx="44" cy="42" r="7.5" fill="none" stroke="#f59e0b" stroke-width="2.2"/><g transform="rotate(-40 50 42)"><rect x="18" y="38" width="66" height="8.5" rx="2.5" fill="#e2e8f0" stroke="#1e293b" stroke-width="1.2"/><circle cx="18" cy="42.2" r="8" fill="#e2e8f0" stroke="#1e293b" stroke-width="1.2"/><circle cx="84" cy="42.2" r="8" fill="#e2e8f0" stroke="#1e293b" stroke-width="1.2"/></g></svg>'
    },
    {
        "titulo": "Tableros y Reportes",
        "desc": "Indicadores y<br>reportes ejecutivos",
        "url": "#tableros",
        "color": "#8b5cf6",
        "rgb": "139, 92, 246",
        "img": RES["icons"][4],
        "svg": '<svg viewBox="0 0 96 84" width="68" height="60" xmlns="http://www.w3.org/2000/svg"><rect x="12" y="12" width="72" height="44" rx="5" fill="#09182e" stroke="#60a5fa" stroke-width="2"/><polygon points="41,56 55,56 60,67 36,67" fill="#3b82f6"/><rect x="30" y="67" width="36" height="4" rx="1.5" fill="#93c5fd"/><rect x="21" y="38" width="5.5" height="10" rx="1" fill="#38bdf8"/><rect x="30" y="30" width="5.5" height="18" rx="1" fill="#22d3ee"/><rect x="39" y="34" width="5.5" height="14" rx="1" fill="#818cf8"/><rect x="48" y="24" width="5.5" height="24" rx="1" fill="#a78bfa"/><circle cx="68" cy="34" r="9" fill="none" stroke="#1e3a8a" stroke-width="4.2"/><circle cx="68" cy="34" r="9" fill="none" stroke="#00d4ff" stroke-width="4.2" stroke-dasharray="35 22"/></svg>'
    },
    {
        "titulo": "HES - Consumo",
        "desc": "Lecturas y análisis<br>de consumo",
        "url": "#hes",
        "color": "#06b6d4",
        "rgb": "6, 182, 212",
        "img": RES["icons"][5],
        "svg": '<svg viewBox="0 0 96 84" width="68" height="60" xmlns="http://www.w3.org/2000/svg"><polygon points="40,15 12,38 19,38 19,66 61,66 61,38 68,38" fill="#cbd5e1" stroke="#38bdf8" stroke-width="1.6"/><polygon points="40,11 9,37 14,41 40,19 66,41 71,37" fill="#0284c7"/><rect x="27" y="44" width="10" height="22" rx="1.5" fill="#0f172a"/><path d="M 63 17 Q 73 9 83 17" fill="none" stroke="#22d3ee" stroke-width="2.5" stroke-linecap="round"/><path d="M 73 35 C 73 35 61 50 61 60 C 61 67 67 73 73 73 C 79 73 85 67 85 60 C 85 50 73 35 73 35 Z" fill="#0284c7" stroke="#e0f2fe" stroke-width="1.6"/></svg>'
    }
]

bg_rule = (
    f"background: #03152e url('{RES['bg']}') center center / cover no-repeat fixed;"
    if RES["bg"]
    else "background: radial-gradient(ellipse at 76% 14%, rgba(0, 185, 255, 0.28) 0%, transparent 45%), radial-gradient(ellipse at 50% 98%, rgba(0, 145, 255, 0.35) 0%, transparent 55%), linear-gradient(180deg, #020c1c 0%, #052347 42%, #031730 78%, #020b18 100%);"
)

css_parts = [
    "<style>",
    "[data-testid='stHeader'], [data-testid='stToolbar'], [data-testid='stDecoration'], [data-testid='stStatusWidget'], [data-testid='stSidebar'], [data-testid='collapsedControl'], #MainMenu, footer { display: none !important; }",
    ".stApp, [data-testid='stAppViewContainer'], .main { " + bg_rule + " padding: 0 !important; margin: 0 !important; }",
    "[data-testid='block-container'] { padding: 18px 34px 14px 34px !important; max-width: 100% !important; margin: 0 auto !important; }",
    ".hud-top { display: flex; justify-content: space-between; align-items: center; gap: 16px; margin-bottom: 22px; }",
    ".hud-brand { display: flex; align-items: center; gap: 20px; }",
    ".hud-logo { height: 60px; width: auto; filter: brightness(0) invert(1) drop-shadow(0 2px 10px rgba(0,0,0,0.65)); }",
    ".hud-line { width: 2px; height: 48px; background: rgba(255,255,255,0.65); }",
    ".hud-title { font-size: 1.58rem; font-weight: 700; color: #ffffff; line-height: 1.15; text-shadow: 0 2px 8px rgba(0,0,0,0.7); }",
    ".hud-sub { font-size: 1.12rem; font-weight: 400; color: #cbd5e1; margin-top: 3px; text-shadow: 0 2px 8px rgba(0,0,0,0.7); }",
    ".hud-clock { background: rgba(4, 18, 38, 0.72); border: 1px solid rgba(186, 230, 253, 0.32); border-radius: 10px; padding: 9px 16px; min-width: 192px; backdrop-filter: blur(10px); }",
    ".hud-clock-d { color: #e2e8f0; font-size: 0.88rem; margin-bottom: 4px; }",
    ".hud-clock-t { color: #ffffff; font-size: 1.06rem; font-weight: 700; }",
    ".hud-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 20px; }",
    "@media (max-width: 1050px) { .hud-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); } }",
    "@media (max-width: 700px) { .hud-grid { grid-template-columns: 1fr; } }",
    ".hud-card { position: relative; display: flex; align-items: center; gap: 16px; height: 174px; padding: 14px 18px; border-radius: 16px; text-decoration: none !important; color: #ffffff !important; background: linear-gradient(135deg, rgba(15, 45, 84, 0.68) 0%, rgba(5, 20, 42, 0.86) 100%); border: 1.5px solid rgba(255, 255, 255, 0.30); backdrop-filter: blur(12px); box-shadow: 0 12px 28px rgba(0,0,0,0.55), inset 0 1px 1px rgba(255,255,255,0.22); overflow: hidden; transition: transform 0.2s ease, border-color 0.2s ease; }",
    ".hud-card:hover { transform: translateY(-4px); border-color: var(--c); }",
    ".hud-card::after { content: ''; position: absolute; left: 4%; right: 4%; bottom: 0; height: 4px; background: var(--c); border-radius: 4px 4px 0 0; box-shadow: 0 -2px 14px rgba(var(--rgb), 0.75), 0 0 24px rgba(var(--rgb), 0.75); }",
    ".hud-thumb { flex: 0 0 104px; width: 104px; height: 104px; border-radius: 12px; background: rgba(3, 14, 30, 0.55); border: 1px solid rgba(255,255,255,0.16); display: flex; align-items: center; justify-content: center; overflow: hidden; }",
    ".hud-thumb img { width: 100%; height: 100%; object-fit: cover; display: block; }",
    ".hud-info { flex: 1; min-width: 0; }",
    ".hud-card-title { font-size: 1.24rem; font-weight: 700; color: #ffffff; line-height: 1.18; margin-bottom: 7px; }",
    ".hud-card-desc { font-size: 0.88rem; color: #dbeafe; line-height: 1.28; }",
    ".hud-arr { flex: 0 0 32px; width: 32px; height: 32px; border-radius: 50%; border: 2px solid var(--c); display: flex; align-items: center; justify-content: center; align-self: flex-end; color: #ffffff; font-size: 0.95rem; font-weight: 700; background: rgba(2,11,23,0.5); }",
    ".hud-foot { margin-top: 20px; padding: 10px 18px; border-radius: 10px; background: rgba(3, 14, 30, 0.78); border: 1px solid rgba(186, 230, 253, 0.22); display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; font-size: 0.88rem; color: #e2e8f0; }",
    "</style>",
]
st.markdown("".join(css_parts), unsafe_allow_html=True)

header_html = (
    "<div class='hud-top'>"
    "<div class='hud-brand'>"
    f"<img class='hud-logo' src='{LOGO_URL}' alt='MIAA'>"
    "<div class='hud-line'></div>"
    "<div>"
    "<div class='hud-title'>Sistema Integral de Monitoreo</div>"
    "<div class='hud-sub'>Agua Potable para Aguascalientes</div>"
    "</div>"
    "</div>"
    "<div class='hud-clock'>"
    "<div class='hud-clock-d'>📅 <span id='miaa-date'>26 Noviembre 2026</span></div>"
    "<div class='hud-clock-t'>🕒 <span id='miaa-clock'>09:04:00 AM</span></div>"
    "</div>"
    "</div>"
)
st.markdown(header_html, unsafe_allow_html=True)

grid_items = ["<div class='hud-grid'>"]
for t in TARJETAS:
    media = f"<img src='{t['img']}' alt=''>" if t["img"] else t["svg"]
    grid_items.append(
        f"<a class='hud-card' href='{t['url']}' target='_blank' style='--c:{t['color']};--rgb:{t['rgb']};'>"
        f"<div class='hud-thumb'>{media}</div>"
        f"<div class='hud-info'>"
        f"<div class='hud-card-title'>{t['titulo']}</div>"
        f"<div class='hud-card-desc'>{t['desc']}</div>"
        f"</div>"
        f"<div class='hud-arr'>&#10095;</div>"
        f"</a>"
    )
grid_items.append("</div>")
st.markdown("".join(grid_items), unsafe_allow_html=True)

footer_html = (
    "<div class='hud-foot'>"
    "<div><strong>MIAA</strong> &nbsp;|&nbsp; Innovación, Tecnología y Agua para Todos</div>"
    "<div style='display:flex;gap:14px;'>"
    "<span>⚙ Configuración</span><span style='opacity:0.35;'>|</span>"
    "<span>ⓘ Acerca de</span><span style='opacity:0.35;'>|</span>"
    "<span>⏻ Cerrar Sesión</span>"
    "</div>"
    "</div>"
)
st.markdown(footer_html, unsafe_allow_html=True)

components.html(
    """
    <script>
    (function() {
        const meses = [
            "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
            "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
        ];
        function sync() {
            const d = window.parent.document;
            const dEl = d.getElementById("miaa-date");
            const tEl = d.getElementById("miaa-clock");
            if (!dEl || !tEl) return;
            const now = new Date();
            dEl.textContent = String(now.getDate()).padStart(2, "0") + " " + meses[now.getMonth()] + " " + now.getFullYear();
            let h = now.getHours();
            const m = String(now.getMinutes()).padStart(2, "0");
            const s = String(now.getSeconds()).padStart(2, "0");
            const ap = h >= 12 ? "PM" : "AM";
            h = h % 12 || 12;
            tEl.textContent = String(h).padStart(2, "0") + ":" + m + ":" + s + " " + ap;
        }
        sync();
        setInterval(sync, 1000);
    })();
    </script>
    """,
    height=0,
    width=0
)
