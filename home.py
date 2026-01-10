# home.py - VERSION AVEC DESCRIPTIONS RÉDUCTIBLES (READ MORE)
import streamlit as st
import streamlit.components.v1 as components
import base64

# =============================================================================
# 1. CONFIGURATION & THÈME
# =============================================================================
st.set_page_config(
    page_title="Logistics Intelligence",
    page_icon="🚚",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def get_theme():
    try:
        return st.get_option("theme.base") or "dark"
    except:
        return "dark"

theme = get_theme()
is_dark = theme == "dark"

# =============================================================================
# 2. SYSTÈME DE DESIGN (Orbitron & Glassmorphism)
# =============================================================================
css_vars = f"""
:root {{
    --primary: #6366f1;
    --accent: #a855f7;
    --success: #10b981;
    --bg-body: {'#0f172a' if is_dark else '#f8fafc'};
    --bg-card: {'rgba(30, 41, 59, 0.7)' if is_dark else 'rgba(255, 255, 255, 0.8)'};
    --text-main: {'#f8fafc' if is_dark else '#1e293b'};
    --text-sub: {'#94a3b8' if is_dark else '#64748b'};
    --border: {'rgba(255, 255, 255, 0.1)' if is_dark else 'rgba(0, 0, 0, 0.1)'};
}}
"""

st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&family=Orbitron:wght@500;700;900&display=swap');
    {css_vars}

    .stApp {{ background-color: var(--bg-body); font-family: 'Inter', sans-serif; }}
    section[data-testid="stSidebar"], .stSidebarCollapsedControl {{ display: none !important; }}

    /* Style des Cartes */
    .tool-card {{
        background: var(--bg-card);
        backdrop-filter: blur(12px);
        border: 1px solid var(--border);
        border-radius: 20px;
        padding: 2rem 1.2rem;
        min-height: 300px;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        transition: 0.3s ease;
    }}
    .tool-card:hover {{ transform: translateY(-5px); border-color: var(--primary); }}

    .tool-icon {{ font-size: 3rem; margin-bottom: 0.8rem; }}
    
    .tool-title {{ 
        font-family: 'Orbitron', sans-serif; 
        color: var(--text-main); 
        font-size: 1rem; 
        text-transform: uppercase; 
        letter-spacing: 1.5px;
        font-weight: 700;
        margin-bottom: 10px;
    }}

    /* Texte réduit / Tronqué */
    .tool-desc {{ 
        color: var(--text-sub); 
        font-size: 0.85rem; 
        font-family: 'Inter', sans-serif;
        line-height: 1.4;
        display: -webkit-box;
        -webkit-line-clamp: 2; /* Nombre de lignes visibles par défaut */
        -webkit-box-orient: vertical;
        overflow: hidden;
        margin-bottom: 5px;
    }}
    
    .tool-desc.expanded {{
        -webkit-line-clamp: unset;
    }}

    /* Lien "Voir plus" en Orbitron */
    .read-more-btn {{
        font-family: 'Orbitron', sans-serif;
        font-size: 0.65rem;
        color: var(--primary);
        cursor: pointer;
        text-transform: uppercase;
        margin-bottom: 15px;
        font-weight: 600;
    }}

    /* Boutons */
    div.stButton > button {{
        background: linear-gradient(135deg, var(--primary), var(--accent)) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        font-family: 'Orbitron', sans-serif !important;
        font-size: 0.8rem !important;
        letter-spacing: 1px !important;
        padding: 0.6rem !important;
        text-transform: uppercase !important;
        width: 100% !important;
    }}
</style>
""", unsafe_allow_html=True)

# =============================================================================
# 3. HEADER CARROUSEL
# =============================================================================
def get_base64_img(path):
    try:
        with open(path, "rb") as f:
            return f"data:image/jpg;base64,{base64.b64encode(f.read()).decode()}"
    except: return ""

img1, img2 = get_base64_img("pages/img1.jpg"), get_base64_img("pages/img2.jpg")
overlay = "rgba(15, 23, 42, 0.8)" if is_dark else "rgba(255, 255, 255, 0.8)"

header_html = f"""
<div style="position: relative; height: 180px; border-radius: 20px; overflow: hidden; display: flex; align-items: center; justify-content: center;">
    <div id="bg" style="position: absolute; width: 100%; height: 100%; background-size: cover; background-position: center; transition: 1.5s; background-image: url('{img1}');"></div>
    <div style="position: absolute; width: 100%; height: 100%; background: {overlay}; z-index: 1;"></div>
    <div style="position: relative; z-index: 2; text-align: center;">
        <h1 style="font-family: 'Orbitron', sans-serif; color: #6366f1; font-size: 2.2rem; margin: 0; letter-spacing: 4px; font-weight: 900;">LOGISTICS INTELLIGENCE</h1>
        <p style="font-family: 'Orbitron', sans-serif; color: {('white' if is_dark else '#1e293b')}; font-size: 0.8rem; margin-top: 5px;">ADVANCED SOLUTIONS</p>
    </div>
</div>
<script>
    const imgs = ['{img1}', '{img2}'];
    let i = 0;
    setInterval(() => {{
        i = (i + 1) % imgs.length;
        document.getElementById('bg').style.backgroundImage = `url(${{imgs[i]}})`;
    }}, 5000);
</script>
"""
components.html(header_html, height=200)

# =============================================================================
# 4. FONCTION CARTE AVEC RÉDUCTION DE TEXTE
# =============================================================================
def draw_card(icon, title, desc, key, page, soon=False):
    # On utilise du HTML pour la partie descriptive et le lien "Lire plus"
    st.markdown(f"""
    <div class="tool-card">
        <div class="tool-icon">{icon}</div>
        <div class="tool-title">{title}</div>
        <div id="desc-{key}" class="tool-desc">{desc}</div>
        <div id="btn-more-{key}" class="read-more-btn" onclick="toggleText('{key}')">Lire plus +</div>
    </div>
    
    <script>
    function toggleText(key) {{
        const desc = document.getElementById('desc-' + key);
        const btn = document.getElementById('btn-more-' + key);
        if (desc.style.display === "block" || desc.classList.contains('expanded')) {{
            desc.classList.remove('expanded');
            btn.innerText = "Lire plus +";
        }} else {{
            desc.classList.add('expanded');
            btn.innerText = "Réduire -";
        }}
    }}
    </script>
    """, unsafe_allow_html=True)
    
    if soon:
        st.button(f"COMING SOON", key=key, disabled=True)
    else:
        if st.button(title.upper(), key=key):
            st.switch_page(page)

# Grille
cols = st.columns(3)
apps = [
    ("📦", "Pallet Optimizer", "Calculez l'agencement optimal de vos boites sur une palette standard pour maximiser l'espace et la stabilité.", "p1", "pages/app1.py", False),
    ("🚛", "Container Load", "Optimisez le chargement de vos conteneurs maritimes en tenant compte du poids et du volume total disponible.", "p2", "pages/app2.py", False),
    ("📍", "Vogel System", "Application de l'approximation de Vogel pour résoudre les problèmes de transport et minimiser les coûts logistiques.", "p3", "pages/app3.py", False),
    ("⚙️", "MRP Solution", "Planification des besoins matières et calcul des stocks de sécurité pour éviter les ruptures de production.", "p4", "pages/app4.py", False),
    ("💰", "Cost Calculator", "Simulateur complet pour estimer vos coûts de transport selon les zones géographiques et le mode d'expédition.", "p5", "pages/app5.py", False),
    ("📈", "Six Sigma", "Outils statistiques pour améliorer la qualité de vos processus industriels et réduire la variabilité.", "p6", "", True)
]

for idx, app in enumerate(apps):
    with cols[idx % 3]:
        draw_card(*app)
        st.markdown("<br>", unsafe_allow_html=True)

st.markdown("<div style='text-align: center; color: var(--text-sub); font-family: Orbitron; font-size: 0.7rem; letter-spacing: 2px; padding: 20px;'>© 2026 LOGISTICS INTELLIGENCE</div>", unsafe_allow_html=True)
