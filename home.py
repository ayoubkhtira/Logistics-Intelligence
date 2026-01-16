import streamlit as st
import streamlit.components.v1 as components

# =============================================================================
# 1. CONFIGURATION DE LA PAGE
# =============================================================================
st.set_page_config(
    page_title="Logistics Intelligence",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def get_theme():
    """Détecte le thème (dark par défaut pour le look moderne)"""
    try:
        # Tentative de récupération du thème
        if hasattr(st, 'theme'):
            return st.theme.base or "dark"
        return "dark"
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
    --bg-body: {'rgba(15, 23, 42, 0.85)' if is_dark else 'rgba(241, 245, 249, 0.85)'};
    --bg-card: {'rgba(30, 41, 59, 0.85)' if is_dark else 'rgba(255, 255, 255, 0.85)'};
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

    /* --- BACKGROUND IMAGE --- */
    .stApp {{
        background: linear-gradient(rgba(15, 23, 42, 0.85), rgba(15, 23, 42, 0.9)),
                    url('https://img.freepik.com/free-photo/young-man-working-warehouse-with-boxes_1303-16616.jpg?t=st=1768576297~exp=1768579897~hmac=b751ddd6c6ba764a76c5865607befdccd242fe4ad7516559cf72232156eff7d0&w=1480') no-repeat center center fixed;
        background-size: cover;
        background-attachment: fixed;
        font-family: 'Inter', sans-serif;
        color: var(--text-main);
        min-height: 100vh;
    }}
    
    /* Assurer que tout le contenu est visible */
    .main .block-container {{
        padding-top: 2rem;
        padding-bottom: 2rem;
        background: transparent;
    }}
    
    /* Cacher la Sidebar complètement */
    section[data-testid="stSidebar"], 
    .stSidebarCollapsedControl, 
    [data-testid="collapsedControl"] {{ 
        display: none !important; 
    }}
    
    /* Cacher les éléments par défaut de Streamlit */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}

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
        height: 280px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: var(--shadow-card);
        position: relative;
        overflow: hidden;
        margin-bottom: 1rem;
    }}
    
    .tool-card:hover {{
        transform: translateY(-5px);
        border-color: var(--primary);
        box-shadow: var(--glow), var(--shadow-card);
    }}

    /* Icônes textuelles (remplacement des emojis) */
    .tool-icon {{
        font-family: 'Orbitron', sans-serif;
        font-size: 2.2rem;
        font-weight: 900;
        margin-bottom: 1rem;
        color: transparent;
        background: linear-gradient(135deg, var(--primary), var(--accent));
        -webkit-background-clip: text;
        background-clip: text;
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
        background: rgba(16, 185, 129, 0.1);
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
        margin-top: 10px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0,0,0,0.2);
        letter-spacing: 1px;
        cursor: pointer;
    }}

    div.stButton > button:hover {{
        background: linear-gradient(135deg, var(--primary-hover), var(--primary));
        box-shadow: 0 8px 12px rgba(99, 102, 241, 0.4);
        transform: translateY(-2px);
        color: white;
        border: none;
    }}

    /* Style pour bouton désactivé */
    div.stButton > button:disabled {{
        background: #6b7280;
        cursor: not-allowed;
        transform: none;
        box-shadow: none;
    }}

    /* --- RESPONSIVE MOBILE --- */
    @media (max-width: 768px) {{
        .tool-card {{ 
            height: auto; 
            min-height: 220px; 
            padding: 1.5rem; 
            margin-bottom: 1.5rem; 
        }}
        .tool-icon {{ font-size: 1.8rem; }}
        .tool-title {{ font-size: 1rem; }}
        [data-testid="column"] {{ 
            width: 100% !important; 
            flex: 1 1 auto !important; 
            min-width: 100% !important; 
        }}
    }}

    /* Séparateur */
    hr {{ 
        border-color: var(--border-card); 
        margin: 3rem 0; 
        opacity: 0.3;
    }}
    
    /* Footer */
    .footer {{
        text-align: center;
        color: var(--text-sub);
        font-size: 0.8rem;
        padding: 20px;
        margin-top: 2rem;
    }}
    
    /* Titre section */
    .section-title {{
        font-family: 'Orbitron', sans-serif;
        font-size: 1.5rem;
        color: var(--text-main);
        margin-bottom: 1.5rem;
        text-align: center;
    }}
</style>
""", unsafe_allow_html=True)

# =============================================================================
# 3. HEADER ANIMÉ (HTML/JS OPTIMISÉ)
# =============================================================================
header_bg_grad = "linear-gradient(135deg, rgba(15, 23, 42, 0.9) 0%, rgba(30, 27, 75, 0.9) 100%)"
text_color = "#f8fafc"

html_header = f"""
<!DOCTYPE html>
<html>
<head>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@900&family=Inter:wght@400&display=swap" rel="stylesheet">
    <style>
        body {{ 
            margin: 0; 
            padding: 10px; 
            background: transparent; 
            font-family: 'Inter', sans-serif; 
            overflow: hidden; 
            display: flex; 
            align-items: center; 
            justify-content: center; 
            height: 160px; 
        }}
        .container {{
            width: 100%; 
            height: 100%;
            background: {header_bg_grad};
            border-radius: 24px;
            position: relative;
            overflow: hidden;
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);
            display: flex; 
            flex-direction: column; 
            align-items: center; 
            justify-content: center;
            border: 1px solid rgba(255,255,255,0.05);
            backdrop-filter: blur(10px);
        }}
        .bg-anim {{
            position: absolute; 
            top: -50%; 
            left: -50%; 
            width: 200%; 
            height: 200%;
            background: radial-gradient(circle, rgba(99,102,241,0.15) 0%, transparent 70%);
            animation: rotate 15s linear infinite;
        }}
        @keyframes rotate {{ 
            0% {{ transform: rotate(0deg); }} 
            100% {{ transform: rotate(360deg); }} 
        }}
        h1 {{
            font-family: 'Orbitron', sans-serif; 
            font-size: 2.5em; 
            margin: 0; 
            z-index: 2;
            background: linear-gradient(to right, #818cf8, #c084fc, #34d399);
            -webkit-background-clip: text; 
            -webkit-text-fill-color: transparent;
            text-transform: uppercase; 
            letter-spacing: 4px; 
            font-weight: 900;
            text-shadow: 0 4px 10px rgba(0,0,0,0.2);
        }}
        p {{
            color: {text_color}; 
            opacity: 0.8; 
            font-size: 0.9em; 
            margin-top: 10px; 
            z-index: 2; 
            letter-spacing: 2px; 
            text-transform: uppercase; 
            font-weight: 600;
        }}
        @media (max-width: 600px) {{ 
            h1 {{ font-size: 1.8em; letter-spacing: 2px; }} 
            p {{ font-size: 0.7em; }} 
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="bg-anim"></div>
        <h1>Logistics Intelligence</h1>
        
    </div>
</body>
</html>
"""
components.html(html_header, height=180)

# =============================================================================
# 4. GRILLE D'APPLICATIONS
# =============================================================================

# Fonction helper pour créer une carte
def app_card(icon_text, title, desc, btn_key, page_path, is_coming_soon=False):
    """Crée une carte d'application avec design moderne"""
    
    # Partie visuelle (HTML)
    if is_coming_soon:
        card_html = f"""
        <div class="tool-card soon-card">
            <div class="tool-icon">{icon_text}</div>
            <div class="tool-title">{title}</div>
            <div class="tool-desc">{desc}</div>
            <div class="soon-badge">Bientôt Disponible</div>
        </div>
        """
        st.markdown(card_html, unsafe_allow_html=True)
        # Bouton désactivé pour "Coming Soon"
        st.button("Accéder à l'outil", key=f"{btn_key}_disabled", disabled=True, use_container_width=True)
    else:
        card_html = f"""
        <div class="tool-card">
            <div class="tool-icon">{icon_text}</div>
            <div class="tool-title">{title}</div>
            <div class="tool-desc">{desc}</div>
        </div>
        """
        st.markdown(card_html, unsafe_allow_html=True)
        
        # Bouton Streamlit fonctionnel
        if st.button("Accéder à l'outil", key=btn_key, use_container_width=True):
            try:
                st.switch_page(page_path)
            except Exception as e:
                st.error(f"Impossible d'ouvrir la page: {e}")

# Section Applications
st.markdown('<div class="section-title">Outils d\'Optimisation Logistique</div>', unsafe_allow_html=True)
st.markdown('<div style="margin: 20px 0;"></div>', unsafe_allow_html=True)

# Ligne 1 - Applications principales
col1, col2, col3 = st.columns(3)

with col1:
    app_card("PO", "Optimisation de Palettes", 
             "Maximisez le remplissage de vos palettes 3D avec nos algorithmes avancés", 
             "btn_1", "pages/app1.py")

with col2:
    app_card("CL", "Chargement Conteneurs", 
             "Planification intelligente du chargement de conteneurs pour optimiser l'espace", 
             "btn_2", "pages/app2.py")

with col3:
    app_card("VS", "Système de Vogel", 
             "Algorithme d'approvisionnement optimisé pour réduire les coûts de transport", 
             "btn_3", "pages/app3.py")

# Espacement
st.markdown("<div style='height: 30px'></div>", unsafe_allow_html=True)

# Ligne 2 - Autres applications
col4, col5, col6 = st.columns(3)

with col4:
    app_card("MRP", "Solution MRP/CBN", 
             "Gestion des besoins en composants et planification des ressources", 
             "btn_4", "pages/app4.py")

with col5:
    app_card("CC", "Calcul des Coûts", 
             "Estimation précise des coûts logistiques et analyse des économies", 
             "btn_5", "pages/app5.py")

with col6:
    app_card("SS", "Méthode Six Sigma", 
             "Analyse de qualité et réduction des défauts dans les processus", 
             "btn_6", "", is_coming_soon=True)

# Footer
st.markdown("---")
st.markdown(
    '<div class="footer">'
    '© Logistics Intelligence •'
    '<span style="color: #6366f1;"></span>'
    '</div>', 
    unsafe_allow_html=True
)
