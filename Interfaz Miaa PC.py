import base64
import io
import math
import random
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Interfaz Miaa",
    page_icon="https://www.miaa.mx/favicon.ico",
    layout="wide",
    initial_sidebar_state="collapsed"
)

LOGO_URL = "https://raw.githubusercontent.com/Miaa-Aguascalientes/Logos/38504978c8f77a4dac38ad476f74dbdee6af2cad/LogoMIAA.svg"

SISTEMAS = [
    {
        "id": "scada",
        "titulo": "SCADA<br>Pozos y Equipos",
        "titulo_plano": "SCADA Pozos y Equipos",
        "descripcion": "Monitoreo y control<br>de pozos y equipos",
        "url": "https://sistema-scada.streamlit.app/",
        "glow": "#00d4ff",
        "glow_rgb": "0, 212, 255",
        "archivo_local": "assets/icon_scada.png"
    },
    {
        "id": "medidores",
        "titulo": "Medidores<br>Inteligentes",
        "titulo_plano": "Medidores Inteligentes",
        "descripcion": "Lecturas y análisis<br>de medidores",
        "url": "https://lecturas-hes.streamlit.app/",
        "glow": "#00e5ff",
        "glow_rgb": "0, 229, 255",
        "archivo_local": "assets/icon_medidores.png"
    },
    {
        "id": "gis",
        "titulo": "Mapa y GIS",
        "titulo_plano": "Mapa y GIS",
        "descripcion": "Información geográfica<br>y sectorización",
        "url": "https://miaa-sincronizador-ver-app.streamlit.app/",
        "glow": "#10b981",
        "glow_rgb": "16, 185, 129",
        "archivo_local": "assets/icon_gis.png"
    },
    {
        "id": "mantenimiento",
        "titulo": "Mantenimiento",
        "titulo_plano": "Mantenimiento",
        "descripcion": "Gestión de<br>mantenimiento y fallas",
        "url": "https://incidencias-miaa.streamlit.app/",
        "glow": "#f59e0b",
        "glow_rgb": "245, 158, 11",
        "archivo_local": "assets/icon_mantenimiento.png"
    },
    {
        "id": "tableros",
        "titulo": "Tableros y Reportes",
        "titulo_plano": "Tableros y Reportes",
        "descripcion": "Indicadores y<br>reportes ejecutivos",
        "url": "https://tableros-miaa.streamlit.app/",
        "glow": "#8b5cf6",
        "glow_rgb": "139, 92, 246",
        "archivo_local": "assets/icon_tableros.png"
    },
    {
        "id": "hes",
        "titulo": "HES - Consumo",
        "titulo_plano": "HES - Consumo",
        "descripcion": "Lecturas y análisis<br>de consumo",
        "url": "https://hes-consumo.streamlit.app/",
        "glow": "#06b6d4",
        "glow_rgb": "6, 182, 212",
        "archivo_local": "assets/icon_hes.png"
    }
]


@st.cache_data(show_spinner=False)
def obtener_fondo_base64() -> str:
    ruta_fondo = Path("assets/fondo_miaa.jpg")
    if ruta_fondo.exists():
        return f"data:image/jpeg;base64,{base64.b64encode(ruta_fondo.read_bytes()).decode('utf-8')}"

    w, h = 1600, 900
    img = Image.new("RGB", (w, h), (3, 16, 36))
    draw = ImageDraw.Draw(img, "RGBA")

    for y in range(h):
        t = y / h
        r = int(4 + 14 * math.sin(t * math.pi))
        g = int(20 + 52 * math.sin(t * math.pi))
        b = int(48 + 95 * math.sin(t * math.pi))
        draw.line([(0, y), (w, y)], fill=(r, g, b, 255))

    halo = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    hdraw = ImageDraw.Draw(halo)
    hdraw.ellipse((980, -60, 1460, 360), fill=(35, 145, 235, 110))
    hdraw.ellipse((1060, 10, 1380, 290), fill=(110, 200, 255, 95))
    halo = halo.filter(ImageFilter.GaussianBlur(45))
    img.paste(halo, (0, 0), halo)

    rng = random.Random(42)
    for tx in range(960, 1600, 28):
        th = rng.randint(45, 95)
        draw.ellipse((tx - 24, 240 - th, tx + 24, 265), fill=(6, 26, 48, 220))

    cx = 1235
    patas = [
        (cx - 56, 130, cx - 68, 250),
        (cx - 20, 134, cx - 24, 250),
        (cx + 20, 134, cx + 24, 250),
        (cx + 56, 130, cx + 68, 250)
    ]
    for x1, y1, x2, y2 in patas:
        draw.line([(x1, y1), (x2, y2)], fill=(95, 155, 205, 210), width=5)
    for y_cross in (170, 210):
        draw.line([(cx - 62, y_cross), (cx + 62, y_cross)], fill=(80, 140, 190, 180), width=3)
    draw.line([(cx - 58, 135), (cx - 22, 170)], fill=(80, 140, 190, 150), width=2)
    draw.line([(cx + 58, 135), (cx + 22, 170)], fill=(80, 140, 190, 150), width=2)
    draw.line([(cx - 22, 170), (cx + 22, 210)], fill=(80, 140, 190, 150), width=2)
    draw.line([(cx + 22, 170), (cx - 22, 210)], fill=(80, 140, 190, 150), width=2)

    draw.ellipse((cx - 78, 34, cx + 78, 62), fill=(115, 175, 225, 235))
    draw.rectangle((cx - 78, 48, cx + 78, 126), fill=(72, 132, 188, 235))
    draw.rectangle((cx - 78, 48, cx - 28, 126), fill=(118, 178, 228, 165))
    draw.ellipse((cx - 78, 112, cx + 78, 140), fill=(52, 106, 160, 240))
    draw.polygon([(cx, 56), (cx - 10, 72), (cx + 10, 72)], fill=(12, 58, 110, 220))
    draw.ellipse((cx - 10, 66, cx + 10, 82), fill=(12, 58, 110, 220))

    wave_layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    wdraw = ImageDraw.Draw(wave_layer)

    pts_top = [(0, 270)]
    for x in range(0, w + 20, 20):
        y = 215 + 32 * math.sin(x * 0.0045) + 14 * math.cos(x * 0.011)
        pts_top.append((x, y))
    pts_top.extend([(w, 340), (0, 340)])
    wdraw.polygon(pts_top, fill=(8, 72, 148, 195))

    crest_top = [(x, 215 + 32 * math.sin(x * 0.0045) + 14 * math.cos(x * 0.011)) for x in range(0, w + 10, 10)]
    wdraw.line(crest_top, fill=(140, 225, 255, 230), width=5)
    wdraw.line([(x, y + 6) for x, y in crest_top], fill=(30, 165, 255, 180), width=8)

    for _ in range(55):
        sx = rng.randint(120, 1480)
        sy = int(175 + 32 * math.sin(sx * 0.0045) + rng.randint(-28, 18))
        sr = rng.randint(2, 6)
        wdraw.ellipse((sx - sr, sy - sr, sx + sr, sy + sr), fill=(185, 240, 255, 215))

    pts_bot = [(0, h)]
    for x in range(0, w + 20, 20):
        y = 755 + 24 * math.sin(x * 0.0052 + 1.2) + 12 * math.cos(x * 0.013)
        pts_bot.append((x, y))
    pts_bot.append((w, h))
    wdraw.polygon(pts_bot, fill=(6, 65, 140, 230))

    crest_bot = [(x, 755 + 24 * math.sin(x * 0.0052 + 1.2) + 12 * math.cos(x * 0.013)) for x in range(0, w + 10, 10)]
    wdraw.line(crest_bot, fill=(165, 235, 255, 240), width=5)
    wdraw.line([(x, y + 8) for x, y in crest_bot], fill=(25, 155, 248, 190), width=10)

    for _ in range(18):
        rx = rng.randint(40, w - 180)
        ry = rng.randint(775, 845)
        rw = rng.randint(70, 190)
        wdraw.arc((rx, ry, rx + rw, ry + 24), start=190, end=350, fill=(135, 220, 255, 130), width=3)

    wave_blur = wave_layer.filter(ImageFilter.GaussianBlur(1.2))
    img.paste(wave_blur, (0, 0), wave_blur)

    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=90)
    return f"data:image/jpeg;base64,{base64.b64encode(buf.getvalue()).decode('utf-8')}"


@st.cache_data(show_spinner=False)
def obtener_icono_tarjeta(sys_id: str, ruta_local: str) -> str:
    p = Path(ruta_local)
    if p.exists():
        ext = p.suffix.lower().lstrip(".")
        if ext == "jpg":
            ext = "jpeg"
        return f"data:image/{ext};base64,{base64.b64encode(p.read_bytes()).decode('utf-8')}"

    w, h = 280, 230
    img = Image.new("RGBA", (w, h), (6, 24, 48, 255))
    d = ImageDraw.Draw(img)

    for r in range(130, 0, -4):
        alpha = int(120 * (1 - r / 130))
        d.ellipse((w // 2 - r, h // 2 - r, w // 2 + r, h // 2 + r), fill=(18, 95, 175, alpha))

    if sys_id == "scada":
        d.rounded_rectangle((96, 22, 254, 118), radius=10, fill=(8, 30, 58, 255), outline=(56, 189, 248, 255), width=3)
        d.line([(112, 92), (140, 62), (168, 76), (202, 42), (238, 56)], fill=(34, 211, 238, 255), width=4)
        d.ellipse((197, 37, 207, 47), fill=(255, 255, 255, 255))
        d.rounded_rectangle((28, 96, 152, 172), radius=14, fill=(14, 116, 210, 255), outline=(125, 211, 252, 255), width=3)
        d.rectangle((36, 102, 144, 122), fill=(56, 189, 248, 170))
        for rx in range(48, 138, 18):
            d.line([(rx, 108), (rx, 160)], fill=(5, 32, 66, 255), width=4)
        d.ellipse((142, 86, 228, 172), fill=(12, 82, 160, 255), outline=(56, 189, 248, 255), width=4)
        d.ellipse((166, 110, 204, 148), fill=(6, 26, 52, 255), outline=(186, 230, 253, 255), width=3)
        d.rectangle((172, 64, 198, 92), fill=(2, 132, 199, 255), outline=(125, 211, 252, 255), width=2)
        d.rounded_rectangle((20, 174, 244, 190), radius=4, fill=(30, 64, 135, 255))

    elif sys_id == "medidores":
        d.rectangle((16, 108, 264, 146), fill=(3, 105, 161, 255), outline=(56, 189, 248, 255), width=2)
        d.rounded_rectangle((28, 96, 52, 158), radius=4, fill=(2, 132, 199, 255), outline=(125, 211, 252, 255), width=2)
        d.rounded_rectangle((228, 96, 252, 158), radius=4, fill=(2, 132, 199, 255), outline=(125, 211, 252, 255), width=2)
        d.arc((102, 14, 178, 72), start=210, end=330, fill=(34, 211, 238, 255), width=5)
        d.arc((116, 28, 164, 72), start=210, end=330, fill=(34, 211, 238, 255), width=5)
        d.ellipse((74, 58, 206, 190), fill=(203, 213, 225, 255), outline=(56, 189, 248, 255), width=5)
        d.ellipse((88, 72, 192, 176), fill=(15, 23, 42, 255), outline=(148, 163, 184, 255), width=3)
        d.rounded_rectangle((102, 102, 178, 128), radius=4, fill=(186, 230, 253, 255))
        d.text((112, 109), "000254.7", fill=(7, 89, 133, 255))
        d.ellipse((132, 140, 148, 156), fill=(239, 68, 68, 255))

    elif sys_id == "gis":
        d.polygon([(30, 74), (102, 52), (102, 178), (30, 200)], fill=(16, 125, 92, 255), outline=(110, 231, 183, 255))
        d.polygon([(102, 52), (176, 74), (176, 200), (102, 178)], fill=(11, 98, 74, 255), outline=(110, 231, 183, 255))
        d.polygon([(176, 74), (248, 52), (248, 178), (176, 200)], fill=(18, 142, 104, 255), outline=(110, 231, 183, 255))
        d.line([(42, 132), (102, 108), (176, 138), (236, 104)], fill=(56, 189, 248, 255), width=6)
        d.line([(72, 68), (124, 132), (146, 186)], fill=(253, 224, 71, 220), width=4)
        px, py = 176, 62
        d.polygon([(px - 32, py + 8), (px + 32, py + 8), (px, py + 66)], fill=(220, 38, 38, 255))
        d.ellipse((px - 34, py - 30, px + 34, py + 36), fill=(239, 68, 68, 255), outline=(255, 255, 255, 255), width=3)
        d.ellipse((px - 14, py - 10, px + 14, py + 18), fill=(255, 255, 255, 255))

    elif sys_id == "mantenimiento":
        cx, cy = 126, 116
        for i in range(10):
            ang = i * (2 * math.pi / 10)
            x1 = cx + math.cos(ang) * 44
            y1 = cy + math.sin(ang) * 44
            x2 = cx + math.cos(ang) * 64
            y2 = cy + math.sin(ang) * 64
            d.line([(x1, y1), (x2, y2)], fill=(203, 213, 225, 255), width=16)
        d.ellipse((cx - 50, cy - 50, cx + 50, cy + 50), fill=(148, 163, 184, 255), outline=(241, 245, 249, 255), width=3)
        d.ellipse((cx - 26, cy - 26, cx + 26, cy + 26), fill=(10, 28, 54, 255), outline=(245, 158, 11, 255), width=4)
        d.line([(68, 174), (206, 52)], fill=(226, 232, 240, 255), width=18)
        d.ellipse((46, 154, 92, 198), fill=(226, 232, 240, 255))
        d.ellipse((184, 32, 230, 76), fill=(226, 232, 240, 255))
        d.ellipse((198, 42, 224, 66), fill=(10, 28, 54, 255))

    elif sys_id == "tableros":
        d.rounded_rectangle((30, 24, 250, 154), radius=12, fill=(10, 25, 50, 255), outline=(96, 165, 250, 255), width=4)
        d.polygon([(122, 154), (158, 154), (172, 186), (108, 186)], fill=(59, 130, 246, 255))
        d.rounded_rectangle((88, 186, 192, 196), radius=4, fill=(147, 197, 253, 255))
        barras = [
            (52, 110, 138, (56, 189, 248)),
            (74, 88, 138, (34, 211, 238)),
            (96, 98, 138, (129, 140, 248)),
            (118, 66, 138, (167, 139, 250))
        ]
        for x1, y1, y2, col in barras:
            d.rounded_rectangle((x1, y1, x1 + 14, y2), radius=3, fill=col + (255,))
        d.ellipse((164, 62, 226, 124), outline=(30, 58, 138, 255), width=14)
        d.arc((164, 62, 226, 124), start=-90, end=145, fill=(0, 212, 255, 255), width=14)

    elif sys_id == "hes":
        d.polygon(
            [(118, 34), (42, 98), (58, 98), (58, 182), (178, 182), (178, 98), (194, 98)],
            fill=(203, 213, 225, 255),
            outline=(56, 189, 248, 255)
        )
        d.polygon([(118, 24), (32, 96), (44, 108), (118, 46), (192, 108), (204, 96)], fill=(2, 132, 199, 255))
        d.rounded_rectangle((82, 120, 114, 182), radius=3, fill=(15, 23, 42, 255))
        d.rounded_rectangle((130, 114, 162, 146), radius=3, fill=(15, 23, 42, 255), outline=(56, 189, 248, 255), width=2)
        d.arc((176, 26, 236, 74), start=210, end=330, fill=(34, 211, 238, 255), width=5)
        d.arc((188, 38, 224, 74), start=210, end=330, fill=(34, 211, 238, 255), width=5)
        gx, gy = 206, 146
        d.polygon([(gx, gy - 54), (gx - 34, gy), (gx + 34, gy)], fill=(14, 165, 233, 255))
        d.ellipse((gx - 36, gy - 24, gx + 36, gy + 44), fill=(2, 132, 199, 255), outline=(224, 242, 254, 255), width=3)
        d.arc((gx - 22, gy - 8, gx + 10, gy + 28), start=120, end=220, fill=(255, 255, 255, 210), width=4)

    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return f"data:image/png;base64,{base64.b64encode(buf.getvalue()).decode('utf-8')}"


FONDO_B64 = obtener_fondo_base64()
for s in SISTEMAS:
    s["img_b64"] = obtener_icono_tarjeta(s["id"], s["archivo_local"])

# Eliminar franjas grises de Streamlit sin dejar huecos
st.markdown(
    """
    <style>
        [data-testid="stHeader"],
        [data-testid="stToolbar"],
        [data-testid="stDecoration"],
        [data-testid="stStatusWidget"],
        [data-testid="stSidebar"],
        [data-testid="collapsedControl"],
        #MainMenu,
        footer {
            display: none !important;
            visibility: hidden !important;
            height: 0 !important;
            width: 0 !important;
        }
        html, body,
        [data-testid="stAppViewContainer"],
        .stApp,
        .main,
        [data-testid="block-container"] {
            background: #020b18 !important;
            padding: 0 !important;
            margin: 0 !important;
            max-width: 100vw !important;
            width: 100vw !important;
            height: 100vh !important;
            overflow: hidden !important;
        }
        iframe {
            display: block !important;
            width: 100vw !important;
            height: 100vh !important;
            border: none !important;
            margin: 0 !important;
            padding: 0 !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

tarjetas_html = []
for s in SISTEMAS:
    tarjetas_html.append(f"""
    <a class="card" href="{s['url']}" target="_blank" rel="noopener noreferrer"
       style="--glow:{s['glow']}; --glow-rgb:{s['glow_rgb']};">
        <div class="card-media">
            <img src="{s['img_b64']}" alt="{s['titulo_plano']}">
        </div>
        <div class="card-content">
            <div class="card-title">{s['titulo']}</div>
            <div class="card-desc">{s['descripcion']}</div>
        </div>
        <div class="card-arrow">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
                <polyline points="9 18 15 12 9 6"></polyline>
            </svg>
        </div>
    </a>
    """)

portal_html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<style>
    * {{
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }}
    html, body {{
        width: 100%;
        height: 100%;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        color: #ffffff;
        background: #020b18 url('{FONDO_B64}') center center / cover no-repeat;
        overflow: hidden;
    }}
    .wrapper {{
        width: 100%;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        background: linear-gradient(180deg, rgba(2,10,24,0.28) 0%, rgba(2,12,28,0.14) 50%, rgba(2,10,24,0.38) 100%);
    }}
    .topbar {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 18px 36px 8px 36px;
    }}
    .brand-group {{
        display: flex;
        align-items: center;
        gap: 22px;
    }}
    .brand-logo {{
        height: 64px;
        width: auto;
        filter: brightness(0) invert(1) drop-shadow(0 3px 12px rgba(0, 0, 0, 0.65));
    }}
    .brand-sep {{
        width: 2px;
        height: 52px;
        background: rgba(255, 255, 255, 0.72);
    }}
    .brand-titles h1 {{
        font-size: 1.6rem;
        font-weight: 700;
        color: #ffffff;
        letter-spacing: 0.2px;
        text-shadow: 0 2px 10px rgba(0, 0, 0, 0.75);
    }}
    .brand-titles p {{
        font-size: 1.14rem;
        font-weight: 400;
        color: #cbd5e1;
        margin-top: 2px;
        text-shadow: 0 2px 10px rgba(0, 0, 0, 0.75);
    }}
    .clock-widget {{
        background: rgba(5, 19, 38, 0.68);
        border: 1px solid rgba(186, 230, 253, 0.32);
        border-radius: 10px;
        padding: 9px 18px;
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.45);
        min-width: 200px;
    }}
    .clock-row {{
        display: flex;
        align-items: center;
        gap: 10px;
        font-size: 0.9rem;
        color: #e2e8f0;
    }}
    .clock-row + .clock-row {{
        margin-top: 5px;
        font-size: 1.08rem;
        font-weight: 700;
        color: #ffffff;
    }}
    .grid-container {{
        padding: 8px 36px;
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 22px;
        max-width: 1560px;
        width: 100%;
        margin: 0 auto;
    }}
    .card {{
        position: relative;
        display: flex;
        align-items: center;
        gap: 18px;
        height: 186px;
        padding: 15px 20px;
        border-radius: 18px;
        text-decoration: none;
        color: #ffffff;
        background: linear-gradient(135deg, rgba(16, 48, 88, 0.62) 0%, rgba(6, 22, 46, 0.82) 100%);
        border: 1.5px solid rgba(255, 255, 255, 0.34);
        backdrop-filter: blur(14px);
        -webkit-backdrop-filter: blur(14px);
        box-shadow:
            0 14px 32px rgba(0, 0, 0, 0.58),
            inset 0 1px 1px rgba(255, 255, 255, 0.28);
        overflow: hidden;
        transition: transform 0.24s ease, border-color 0.24s ease, box-shadow 0.24s ease;
    }}
    .card::before {{
        content: "";
        position: absolute;
        left: 0;
        right: 0;
        bottom: 0;
        height: 42px;
        background: linear-gradient(0deg, rgba(var(--glow-rgb), 0.38) 0%, transparent 100%);
        pointer-events: none;
    }}
    .card::after {{
        content: "";
        position: absolute;
        left: 4%;
        right: 4%;
        bottom: 0;
        height: 4px;
        background: var(--glow);
        border-radius: 4px 4px 0 0;
        box-shadow: 0 -2px 16px var(--glow), 0 0 28px var(--glow);
    }}
    .card:hover {{
        transform: translateY(-5px);
        border-color: var(--glow);
        box-shadow:
            0 18px 38px rgba(0, 0, 0, 0.72),
            0 0 24px rgba(var(--glow-rgb), 0.45),
            inset 0 1px 2px rgba(255, 255, 255, 0.38);
    }}
    .card-media {{
        flex: 0 0 150px;
        width: 150px;
        height: 146px;
        border-radius: 14px;
        overflow: hidden;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 6px 16px rgba(0, 0, 0, 0.45);
        z-index: 1;
    }}
    .card-media img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        display: block;
    }}
    .card-content {{
        flex: 1;
        min-width: 0;
        z-index: 1;
    }}
    .card-title {{
        font-size: 1.28rem;
        font-weight: 700;
        line-height: 1.18;
        color: #ffffff;
        margin-bottom: 8px;
        text-shadow: 0 2px 8px rgba(0, 0, 0, 0.65);
    }}
    .card-desc {{
        font-size: 0.9rem;
        font-weight: 400;
        line-height: 1.3;
        color: #dbeafe;
        text-shadow: 0 1px 4px rgba(0, 0, 0, 0.65);
    }}
    .card-arrow {{
        flex: 0 0 36px;
        width: 36px;
        height: 36px;
        border-radius: 50%;
        border: 2px solid var(--glow);
        display: flex;
        align-items: center;
        justify-content: center;
        align-self: flex-end;
        color: #ffffff;
        background: rgba(3, 14, 30, 0.55);
        box-shadow: 0 0 12px rgba(var(--glow-rgb), 0.45);
        z-index: 1;
        transition: transform 0.2s ease, background 0.2s ease;
    }}
    .card:hover .card-arrow {{
        background: var(--glow);
        color: #020b18;
        transform: translateX(3px);
    }}
    .bottombar {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 36px;
        background: rgba(3, 14, 30, 0.82);
        border-top: 1px solid rgba(186, 230, 253, 0.22);
        backdrop-filter: blur(12px);
        font-size: 0.88rem;
        color: #e2e8f0;
    }}
    .bottom-left {{
        display: flex;
        align-items: center;
        gap: 12px;
    }}
    .bars {{
        display: flex;
        align-items: flex-end;
        gap: 3px;
        height: 14px;
    }}
    .bars span {{
        width: 3.5px;
        background: #ffffff;
        border-radius: 1px;
    }}
    .bottom-right {{
        display: flex;
        align-items: center;
        gap: 18px;
    }}
    .bottom-action {{
        display: flex;
        align-items: center;
        gap: 7px;
        cursor: pointer;
        opacity: 0.92;
    }}
    .bottom-action:hover {{
        opacity: 1;
        color: #38bdf8;
    }}
    .sep {{
        color: rgba(255, 255, 255, 0.3);
    }}
</style>
</head>
<body>
<div class="wrapper">
    <header class="topbar">
        <div class="brand-group">
            <img class="brand-logo" src="{LOGO_URL}" alt="MIAA">
            <div class="brand-sep"></div>
            <div class="brand-titles">
                <h1>Sistema Integral de Monitoreo</h1>
                <p>Agua Potable para Aguascalientes</p>
            </div>
        </div>
        <div class="clock-widget">
            <div class="clock-row">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                    <line x1="16" y1="2" x2="16" y2="6"></line>
                    <line x1="8" y1="2" x2="8" y2="6"></line>
                    <line x1="3" y1="10" x2="21" y2="10"></line>
                </svg>
                <span id="live-date">26 Noviembre 2026</span>
            </div>
            <div class="clock-row">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <circle cx="12" cy="12" r="10"></circle>
                    <polyline points="12 6 12 12 16 14"></polyline>
                </svg>
                <span id="live-clock">09:02:00 AM</span>
            </div>
        </div>
    </header>

    <main class="grid-container">
        {''.join(tarjetas_html)}
    </main>

    <footer class="bottombar">
        <div class="bottom-left">
            <div class="bars">
                <span style="height:5px;"></span>
                <span style="height:8px;"></span>
                <span style="height:11px;"></span>
                <span style="height:14px;"></span>
            </div>
            <span><strong>MIAA</strong> &nbsp;|&nbsp; Innovación, Tecnología y Agua para Todos</span>
        </div>
        <div class="bottom-right">
            <div class="bottom-action">⚙ Configuración</div>
            <span class="sep">|</span>
            <div class="bottom-action">ⓘ Acerca de</div>
            <span class="sep">|</span>
            <div class="bottom-action">⏻ Cerrar Sesión</div>
        </div>
    </footer>
</div>

<script>
    function updateClock() {{
        const dateEl = document.getElementById('live-date');
        const clockEl = document.getElementById('live-clock');
        const now = new Date();
        const meses = [
            "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
            "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
        ];
        const dia = String(now.getDate()).padStart(2, '0');
        dateEl.textContent = `${{dia}} ${{meses[now.getMonth()]}} ${{now.getFullYear()}}`;

        let h = now.getHours();
        const m = String(now.getMinutes()).padStart(2, '0');
        const s = String(now.getSeconds()).padStart(2, '0');
        const ap = h >= 12 ? 'PM' : 'AM';
        h = h % 12;
        if (h === 0) h = 12;
        clockEl.textContent = `${{String(h).padStart(2, '0')}}:${{m}}:${{s}} ${{ap}}`;
    }}
    setInterval(updateClock, 1000);
    updateClock();
</script>
</body>
</html>
"""

components.html(portal_html, height=760, scrolling=False)
