
import streamlit as st
import streamlit.components.v1 as components
import base64
import os

# =============================================================================
# 1. CONFIGURATION DE LA PAGE
# =============================================================================
st.set_page_config(
    page_title="Logistics Intelligence",
    page_icon="🚚",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def get_theme():
    """Détecte le thème Streamlit"""
    try:
        return st.get_option("theme.base") or "dark"
    except:
        return "dark"

theme = get_theme()
is_dark = theme == "dark"

# =============================================================================
# 2. SYSTÈME DE DESIGN (CSS GLOBAL)
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
    --border: {'rgba(255, 255, 255, 0.1)' if is_dark else 'rgba(0, 0, 0, 0.05)'};
}}
"""

st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&family=Orbitron:wght@700;900&display=swap');
    {css_vars}

    .stApp {{ background-color: var(--bg-body); font-family: 'Inter', sans-serif; }}
    
    /* Masquer Sidebar */
    section[data-testid="stSidebar"], .stSidebarCollapsedControl {{ display: none !important; }}

    /* Cartes */
    .tool-card {{
        background: var(--bg-card);
        backdrop-filter: blur(12px);
        border: 1px solid var(--border);
        border-radius: 20px;
        padding: 2rem 1rem;
        height: 280px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        transition: 0.3s;
        box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1);
    }}
    .tool-card:hover {{ transform: translateY(-5px); border-color: var(--primary); }}
    .tool-icon {{ font-size: 3.5rem; margin-bottom: 1rem; }}
    .tool-title {{ font-family: 'Orbitron'; color: var(--text-main); font-size: 1.1rem; text-transform: uppercase; }}
    .tool-desc {{ color: var(--text-sub); font-size: 0.85rem; margin-top: 5px; }}
    
    .soon-card {{ border: 1px dashed var(--success); background: rgba(16, 185, 129, 0.05); }}

    /* Boutons */
    div.stButton > button {{
        background: linear-gradient(135deg, var(--primary), var(--accent));
        color: white; border: none; border-radius: 12px;
        font-family: 'Orbitron'; font-size: 0.8rem; letter-spacing: 1px;
        padding: 0.6rem; transition: 0.3s;
    }}
    div.stButton > button:hover {{ transform: scale(1.02); box-shadow: 0 5px 15px rgba(99, 102, 241, 0.4); }}
</style>
""", unsafe_allow_html=True)

# =============================================================================
# 3. HEADER AVEC CARROUSEL D'IMAGES LOCALES
# =============================================================================
def get_base64_img(path):
    try:
        with open(path, "rb") as f:
            return f"data:image/jpg;base64,{base64.b64encode(f.read()).decode()}"
    except: return ""

img1 = get_base64_img("pages/img1.jpg")
img2 = get_base64_img("pages/img2.jpg")
overlay = "rgba(15, 23, 42, 0.75)" if is_dark else "rgba(255, 255, 255, 0.75)"

header_html = f"""
<div id="header-root" style="position: relative; height: 200px; border-radius: 24px; overflow: hidden; display: flex; align-items: center; justify-content: center;">
    <div id="bg" style="position: absolute; width: 100%; height: 100%; background-size: cover; background-position: center; transition: 1.5s; background-image: url('{img1}');"></div>
    <div style="position: absolute; width: 100%; height: 100%; background: {overlay}; z-index: 1;"></div>
    <div style="position: relative; z-index: 2; text-align: center;">
        <h1 style="font-family: 'Orbitron'; color: #6366f1; font-size: 2.5rem; margin: 0; letter-spacing: 4px;">LOGISTICS INTELLIGENCE</h1>
        <p style="font-family: 'Inter'; color: {('white' if is_dark else '#1e293b')}; letter-spacing: 2px; font-weight: 600;">OPTIMISATION INDUSTRIELLE AVANCÉE</p>
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
components.html(header_html, height=220)

# =============================================================================
# 4. GRILLE D'APPLICATIONS
# =============================================================================
def app_card(icon, title, desc, key, page, soon=False):
    st.markdown(f'<div class="tool-card {"soon-card" if soon else ""}">', unsafe_allow_html=True)
    st.markdown(f'<div class="tool-icon">{icon}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="tool-title">{title}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="tool-desc">{desc}</div>', unsafe_allow_html=True)
    if soon: st.markdown('<div style="color:var(--success); font-weight:bold; margin-top:10px; font-size:0.7rem;">COMING SOON</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    if not soon:
        if st.button("LANCER", key=key, use_container_width=True):
            st.switch_page(page)
    else:
        st.button("LANCER", key=key, disabled=True, use_container_width=True)

col1, col2, col3 = st.columns(3)
with col1: app_card("📦", "Pallet Optimizer", "Optimisation 3D des palettes", "b1", "pages/app1.py")
with col2: app_card("🚛", "Container Load", "Maximisation du volume conteneur", "b2", "pages/app2.py")
with col3: app_card("📍", "Vogel System", "Algorithme d'approvisionnement", "b3", "pages/app3.py")

st.markdown("<br>", unsafe_allow_html=True)

col4, col5, col6 = st.columns(3)
with col4: app_card("⚙️", "MRP Solution", "Gestion des besoins composants", "b4", "pages/app4.py")
with col5: app_card("💰", "Transport Cost", "Calculateur de coûts logistiques", "b5", "pages/app5.py")
with col6: app_card("📈", "Six Sigma", "Analyse de performance & qualité", "b6", "", soon=True)

st.markdown("---")
st.caption("© 2026 Logistics Intelligence - Outils d'aide à la décision")
