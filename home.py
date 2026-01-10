# home.py - VERSION MODERNISÉE & HOMOGÈNE
import streamlit as st
import streamlit.components.v1 as components

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
    """Détecte le thème (dark par défaut pour le look moderne)"""
    try:
        return st.get_option("theme.base") or "dark"
    except:
        return "dark"

theme = get_theme()
is_dark = theme == "dark"

# =============================================================================
# 2. SYSTÈME DE DESIGN (CSS UNIFIÉ)
# =============================================================================

# Palette de couleurs & Variables CSS
css_variables = f"""
:root {{
    --primary: #6366f1;
    --primary-hover: #4f46e5;
    --accent: #8b5cf6;
    --success: #10b981;
    
    /* Couleurs dynamiques selon le thème */
    --bg-body: {'#0f172a' if is_dark else '#f1f5f9'};
    --bg-card: {'rgba(30, 41, 59, 0.7)' if is_dark else 'rgba(255, 255, 255, 0.8)'};
    --text-main: {'#f8fafc' if is_dark else '#1e293b'};
    --text-sub: {'#94a3b8' if is_dark else '#64748b'};
    --border-card: {'rgba(255, 255, 255, 0.1)' if is_dark else 'rgba(0, 0, 0, 0.05)'};
    --shadow-card: {'0 10px 15px -3px rgba(0, 0, 0, 0.5)' if is_dark else '0 10px 15px -3px rgba(0, 0, 0, 0.1)'};
    --glow: {'0 0 20px rgba(99, 102, 241, 0.15)' if is_dark else '0 0 20px rgba(99, 102, 241, 0.05)'};
}}
"""

st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Orbitron:wght@500;700;900&display=swap');
    
    {css_variables}

    /* --- RESET & BASE --- */
    .stApp {{
        background-color: var(--bg-body);
        font-family: 'Inter', sans-serif;
    }}
    
    /* Cacher la Sidebar complètement */
    section[data-testid="stSidebar"], 
    .stSidebarCollapsedControl, 
    [data-testid="collapsedControl"] {{ 
        display: none !important; 
    }}

    /* --- COMPOSANTS UI --- */
    
    /* 1. Header Container (Espacement) */
    .header-spacer {{ margin-bottom: 2rem; }}

    /* 2. Cartes (Style Glassmorphism) */
    .tool-card {{
        background: var(--bg-card);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid var(--border-card);
        border-radius: 20px;
        padding: 2rem 1.5rem;
        height: 280px; /* Hauteur fixe pour alignement */
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: var(--shadow-card);
        position: relative;
        overflow: hidden;
    }}
    
    .tool-card:hover {{
        transform: translateY(-5px);
        border-color: var(--primary);
        box-shadow: var(--glow), var(--shadow-card);
    }}

    /* Icônes */
    .tool-icon {{
        font-size: 3.5rem;
        margin-bottom: 1rem;
        filter: drop-shadow(0 4px 6px rgba(0,0,0,0.1));
        transition: transform 0.3s ease;
    }}
    .tool-card:hover .tool-icon {{ transform: scale(1.1); }}

    /* Typographie Carte */
    .tool-title {{
        font-family: 'Orbitron', sans-serif;
        font-size: 1.1rem;
        font-weight: 700;
        color: var(--text-main);
        letter-spacing: 1px;
        margin-bottom: 0.5rem;
        text-transform: uppercase;
    }}
    
    .tool-desc {{
        font-size: 0.85rem;
        color: var(--text-sub);
        line-height: 1.4;
        max-width: 90%;
    }}

    /* Carte "Coming Soon" Spécifique */
    .soon-card {{
        border: 1px dashed var(--success);
        background: rgba(16, 185, 129, 0.05);
    }}
    .soon-badge {{
        margin-top: 1rem;
        background: rgba(16, 185, 129, 0.2);
        color: var(--success);
        padding: 4px 12px;
        border-radius: 12px;
        font-size: 0.7rem;
        font-weight: 700;
        font-family: 'Orbitron', sans-serif;
        letter-spacing: 1px;
    }}

    /* --- BOUTONS STREAMLIT --- */
    /* On cible les boutons pour qu'ils s'intègrent au design */
    div.stButton > button {{
        width: 100%;
        border: none;
        background: linear-gradient(135deg, var(--primary), var(--accent));
        color: white;
        font-family: 'Orbitron', sans-serif;
        font-weight: 600;
        font-size: 0.8rem;
        padding: 0.75rem 1rem;
        border-radius: 12px;
        margin-top: 0px; /* Collé à la carte visuellement si besoin, ou espacé */
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0,0,0,0.2);
        letter-spacing: 1px;
    }}

    div.stButton > button:hover {{
        background: linear-gradient(135deg, var(--primary-hover), var(--primary));
        box-shadow: 0 8px 12px rgba(99, 102, 241, 0.4);
        transform: translateY(-2px);
        color: white;
        border: none;
    }}

    div.stButton > button:focus {{
        color: white;
        border: none;
        box-shadow: none;
    }}
    
    div.stButton > button:disabled {{
        background: var(--bg-card);
        color: var(--text-sub);
        cursor: not-allowed;
    }}

    /* --- RESPONSIVE MOBILE --- */
    @media (max-width: 768px) {{
        .tool-card {{ height: auto; min-height: 220px; padding: 1.5rem; margin-bottom: 0.5rem; }}
        .tool-icon {{ font-size: 2.5rem; }}
        .tool-title {{ font-size: 1rem; }}
        /* Force 1 colonne sur mobile si Streamlit ne le fait pas auto */
        [data-testid="column"] {{ width: 100% !important; flex: 1 1 auto !important; min-width: 100% !important; }}
    }}

    /* Séparateur */
    hr {{ border-color: var(--border-card); margin: 3rem 0; }}
</style>
""", unsafe_allow_html=True)

# =============================================================================
# 3. HEADER ANIMÉ (HTML/JS OPTIMISÉ)
# =============================================================================
# Note: J'ai épuré le HTML pour qu'il soit plus léger et utilise les mêmes polices
header_bg_grad = "linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%)" if is_dark else "linear-gradient(135deg, #f8fafc 0%, #e0e7ff 100%)"
text_color = "#f8fafc" if is_dark else "#1e293b"

html_header = f"""
<!DOCTYPE html>
<html>
<head>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@900&family=Inter:wght@400&display=swap" rel="stylesheet">
    <style>
        body {{ margin: 0; padding: 10px; background: transparent; font-family: 'Inter', sans-serif; overflow: hidden; display: flex; align-items: center; justify-content: center; height: 160px; }}
        .container {{
            width: 100%; height: 100%;
            background: {header_bg_grad};
            border-radius: 24px;
            position: relative;
            overflow: hidden;
            box-shadow: 0 10px 25px rgba(0,0,0,0.1);
            display: flex; flex-direction: column; align-items: center; justify-content: center;
            border: 1px solid rgba(255,255,255,0.05);
        }}
        .bg-anim {{
            position: absolute; top: -50%; left: -50%; width: 200%; height: 200%;
            background: radial-gradient(circle, rgba(99,102,241,0.15) 0%, transparent 70%);
            animation: rotate 15s linear infinite;
        }}
        @keyframes rotate {{ 0% {{ transform: rotate(0deg); }} 100% {{ transform: rotate(360deg); }} }}
        h1 {{
            font-family: 'Orbitron', sans-serif; font-size: 2.5em; margin: 0; z-index: 2;
            background: linear-gradient(to right, #818cf8, #c084fc, #34d399);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
            text-transform: uppercase; letter-spacing: 4px; font-weight: 900;
            text-shadow: 0 4px 10px rgba(0,0,0,0.2);
        }}
        p {{
            color: {text_color}; opacity: 0.8; font-size: 0.9em; margin-top: 10px; z-index: 2; letter-spacing: 2px; text-transform: uppercase; font-weight: 600;
        }}
        @media (max-width: 600px) {{ h1 {{ font-size: 1.8em; letter-spacing: 2px; }} p {{ font-size: 0.7em; }} }}
    </style>
</head>
<body>
    <div class="container">
        <div class="bg-anim"></div>
        <h1>Logistics Intelligence</h1>
        <p>Advanced Industrial Optimization</p>
    </div>
</body>
</html>
"""
components.html(html_header, height=180)

# =============================================================================
# 4. GRILLE D'APPLICATIONS
# =============================================================================

# Fonction helper pour créer une carte
def app_card(icon, title, desc, btn_key, page_path, is_coming_soon=False):
    # Partie visuelle (HTML)
    if is_coming_soon:
        card_html = f"""
        <div class="tool-card soon-card">
            <div class="tool-icon">{icon}</div>
            <div class="tool-title">{title}</div>
            <div class="tool-desc">{desc}</div>
            <div class="soon-badge">COMING SOON</div>
        </div>
        """
        st.markdown(card_html, unsafe_allow_html=True)
    else:
        card_html = f"""
        <div class="tool-card">
            <div class="tool-icon">{icon}</div>
            <div class="tool-title">{title}</div>
            <div class="tool-desc">{desc}</div>
        </div>
        """
        st.markdown(card_html, unsafe_allow_html=True)
        
        # Bouton Streamlit (Séparé du HTML mais collé visuellement via CSS)
        try:
            if st.button("OUVRIR L'OUTIL", key=btn_key, use_container_width=True):
                st.switch_page(page_path)
        except Exception:
            # Fallback si la page n'existe pas encore en dev
            st.button("OUVRIR L'OUTIL", key=btn_key+"_dis", disabled=True, use_container_width=True)

# Ligne 1
col1, col2, col3 = st.columns(3)
with col1:
    app_card("📦", "Pallet Optimizer", "Maximisez le remplissage de vos palettes 3D", "btn_1", "pages/app1.py")
with col2:
    app_card("🚛", "Container Load", "Planification de chargement conteneur", "btn_2", "pages/app2.py")
with col3:
    app_card("📍", "Vogel System", "Algorithme d'approvisionnement optimisé", "btn_3", "pages/app3.py")

# Espacement
st.markdown("<div style='height: 24px'></div>", unsafe_allow_html=True)

# Ligne 2
col4, col5, col6 = st.columns(3)
with col4:
    app_card("⚙️", "MRP / CBN Solution", "Gestion des besoins en composants", "btn_4", "pages/app4.py")
with col5:
    app_card("💰", "Cost Calculator", "Estimation précise des coûts logistiques", "btn_5", "pages/app5.py")
with col6:
    # Carte Coming Soon
    app_card("📈", "Six Sigma", "Analyse de qualité et réduction défauts", "btn_6", "", is_coming_soon=True)

# Footer discret
st.markdown("---")
st.markdown(
    f"<div style='text-align: center; color: var(--text-sub); font-size: 0.8rem; padding: 20px;'>"
    f"© 2024 Logistics Intelligence Suite • Version 2.0"
    f"</div>", 
    unsafe_allow_html=True
)
