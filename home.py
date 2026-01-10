# home.py - CORRIGÉ ✅ RESPONSIVE MOBILE + PC ✅ DARK/LIGHT ✅ SIDEBAR INVISIBLE
import streamlit as st
import streamlit.components.v1 as components

# =============================================================================
# CONFIGURATION GÉNÉRALE
# =============================================================================
st.set_page_config(
    page_title="Logistics Intelligence", 
    page_icon="🚚", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# =============================================================================
# FONCTIONS UTILITAIRES
# =============================================================================
def get_theme():
    """Détecte le thème Streamlit (dark/light)"""
    try:
        return st.get_option("theme.base") or "light"
    except:
        return "light"

def inject_css(css_content):
    """Injecte du CSS de manière propre"""
    st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)

# =============================================================================
# CSS - RESPONSIVE & SIDEBAR INVISIBLE
# =============================================================================
responsive_css = """
/* SIDEBAR INVISIBLE */
section[data-testid="stSidebar"] { 
    display: none !important; width: 0 !important; height: 0 !important;
    visibility: hidden !important; opacity: 0 !important;
}
.stSidebarCollapsedControl, [data-testid="collapsedControl"] { display: none !important; }
.css-1d391kg, .css-mkog8s { display: none !important; }

/* RESPONSIVE MOBILE FIRST */
@media (max-width: 768px) {
    .main-header { padding: 1.5rem !important; min-height: 120px !important; border-left-width: 6px !important; }
    .main-header h1 { font-size: 2rem !important; letter-spacing: 4px !important; }
    .status { font-size: 0.85rem !important; letter-spacing: 2px !important; }
    
    .tool-card, .soon-card { height: 200px !important; padding: 1.5rem 1rem !important; margin: 0.5rem 0 !important; }
    .tool-icon { font-size: 2.5rem !important; margin-bottom: 0.8rem !important; }
    .tool-title { font-size: 1.1rem !important; letter-spacing: 1px !important; }
    .tool-desc { font-size: 0.8rem !important; }
    
    .stButton > button { height: 42px !important; font-size: 0.75rem !important; padding: 0.6rem 1.2rem !important; }
    [data-testid="column"]:nth-child(1n+4) { width: 100% !important; }
    [data-testid="column"]:nth-child(2), [data-testid="column"]:nth-child(3) { display: none !important; }
}

@media (min-width: 769px) and (max-width: 1200px) {
    .tool-card, .soon-card { height: 240px !important; padding: 2rem 1.2rem !important; }
    .tool-icon { font-size: 3.5rem !important; }
    [data-testid="column"]:nth-child(3n) { width: 100% !important; margin-top: 1rem !important; }
}

@media (min-width: 1201px) {
    .tool-card, .soon-card { height: 260px !important; }
}
"""
inject_css(responsive_css)

# =============================================================================
# CSS - THÈMES DARK/LIGHT
# =============================================================================
theme = get_theme()
is_dark = theme == "dark"

CSS_DARK = """
:root { 
    --bg-primary: #0f0f23, #1a1a2e, #16213e; 
    --bg-card: rgba(102,126,234,0.2), rgba(118,75,162,0.2); 
    --text-primary: #e2e8f0; 
    --text-secondary: #94a3b8; 
    --border-color: rgba(255,255,255,0.2); 
    --shadow-color: rgba(102,126,234,0.3); 
    --accent-color: #667eea; 
}
body { background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 50%, #16213e 100%); color: var(--text-primary); }
.main-header { background: linear-gradient(135deg, rgba(10,10,16,0.95), rgba(26,26,46,0.95)); box-shadow: 0 30px 60px rgba(0,0,0,0.8); }
.tool-card { background: linear-gradient(145deg, var(--bg-card)); backdrop-filter: blur(20px); box-shadow: 0 25px 50px var(--shadow-color); }
.tool-card:hover { box-shadow: 0 35px 70px rgba(102,126,234,0.5); }
.soon-card { background: linear-gradient(145deg, rgba(34,197,94,0.25), rgba(16,185,129,0.25)); border: 2px solid rgba(34,197,94,0.5); box-shadow: 0 25px 50px rgba(34,197,94,0.4); }
@keyframes pulse { 0%,100%{box-shadow:0 25px 50px rgba(34,197,94,0.4);} 50%{box-shadow:0 25px 50px rgba(34,197,94,0.7);} }
.stButton > button { background: linear-gradient(135deg, rgba(102,126,234,0.2), rgba(118,75,162,0.2)); border: 2px solid rgba(102,126,234,0.5); box-shadow: 0 12px 30px rgba(0,0,0,0.3); }
.stButton > button:hover { background: linear-gradient(135deg, rgba(102,126,234,0.4), rgba(118,75,162,0.4)); box-shadow: 0 20px 40px rgba(102,126,234,0.6); }
"""

CSS_LIGHT = """
:root { 
    --bg-primary: #f8fafc, #e2e8f0, #cbd5e1; 
    --bg-card: rgba(102,126,234,0.1), rgba(118,75,162,0.1); 
    --text-primary: #1e293b; 
    --text-secondary: #64748b; 
    --border-color: rgba(0,0,0,0.1); 
    --shadow-color: rgba(102,126,234,0.2); 
    --accent-color: #667eea; 
}
body { background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 50%, #cbd5e1 100%); color: var(--text-primary); }
.main-header { background: linear-gradient(135deg, rgba(248,250,252,0.95), rgba(226,232,240,0.95)); box-shadow: 0 20px 40px rgba(0,0,0,0.1); }
.tool-card { background: linear-gradient(145deg, var(--bg-card)); backdrop-filter: blur(20px); box-shadow: 0 25px 50px var(--shadow-color); }
.tool-card:hover { box-shadow: 0 35px 70px rgba(102,126,234,0.3); }
.soon-card { background: linear-gradient(145deg, rgba(34,197,94,0.15), rgba(16,185,129,0.15)); border: 2px solid rgba(34,197,94,0.3); box-shadow: 0 25px 50px rgba(34,197,94,0.2); }
@keyframes pulse { 0%,100%{box-shadow:0 25px 50px rgba(34,197,94,0.2);} 50%{box-shadow:0 25px 50px rgba(34,197,94,0.4);} }
.stButton > button { background: linear-gradient(135deg, rgba(102,126,234,0.1), rgba(118,75,162,0.1)); border: 2px solid rgba(102,126,234,0.3); box-shadow: 0 12px 30px rgba(0,0,0,0.15); }
.stButton > button:hover { background: linear-gradient(135deg, rgba(102,126,234,0.2), rgba(118,75,162,0.2)); box-shadow: 0 20px 40px rgba(102,126,234,0.4); }
"""

# CSS TYPOGRAPHIE & COMPONENTS
base_css = """
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700&family=Inter:wght@300;400;500;600;700&display=swap');
* { font-family: 'Inter', sans-serif; }
h1,h2,h3 { color: var(--text-primary) !important; font-family: 'Orbitron', monospace !important; }
.main-header { padding: 2.5rem; backdrop-filter: blur(25px); border-radius: 24px; border-left: 8px solid var(--accent-color); margin-bottom: 2rem; }
.tool-card { color: var(--text-primary) !important; padding: 2.5rem 1.5rem !important; border-radius: 24px !important; text-align: center !important; border: 2px solid var(--border-color) !important; margin: 1rem 0.5rem !important; height: 260px; display: flex; flex-direction: column; justify-content: center; transition: all 0.3s ease !important; position: relative; overflow: hidden; backdrop-filter: blur(20px) !important; }
.tool-card:hover { transform: translateY(-10px) scale(1.02) !important; border-color: var(--accent-color) !important; }
.soon-card { padding: 2.5rem 1.5rem !important; border-radius: 24px !important; text-align: center !important; margin: 1rem 0.5rem !important; height: 260px; display: flex; flex-direction: column; justify-content: center; animation: pulse 2s infinite; }
.tool-icon { font-size: 4rem !important; margin-bottom: 1.2rem; display: block; }
.tool-title { font-size: 1.3rem !important; font-weight: 700 !important; font-family: 'Orbitron', monospace !important; margin-bottom: 0.8rem; text-transform: uppercase; letter-spacing: 1.5px; }
.tool-desc { font-size: 0.92rem !important; opacity: 0.9 !important; line-height: 1.5; }
.soon-text { font-size: 1.1rem !important; color: #22c55e !important; font-weight: 600 !important; margin-top: 0.5rem; }
.stButton > button { border-radius: 16px !important; padding: 0.8rem 2rem !important; font-family: 'Orbitron', monospace !important; font-weight: 600 !important; font-size: 0.85rem !important; color: var(--text-primary) !important; text-transform: uppercase !important; letter-spacing: 1px !important; height: 48px !important; width: 100% !important; margin-top: 1rem !important; backdrop-filter: blur(20px) !important; }
.stButton > button:hover { transform: translateY(-4px) scale(1.05) !important; border-color: var(--accent-color) !important; }
"""

# INJECTION CSS COMPLÈTE
inject_css(base_css + (CSS_DARK if is_dark else CSS_LIGHT))

# =============================================================================
# HEADER CARROUSEL
# =============================================================================
def render_header():
    """Rend le header avec carrousel d'images"""
    header_bg = "#0a0a10, #1a1a2e" if is_dark else "#f8fafc, #e2e8f0"
    header_html = f"""
    <!DOCTYPE html><html><head><link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Inter:wght@400;700&display=swap" rel="stylesheet">
    <style>
    body{{margin:0;padding:0;background:transparent;font-family:'Inter',sans-serif;overflow:hidden;}}
    .main-header{{position:relative;padding:35px;background:linear-gradient(135deg,{header_bg});border-radius:24px;border-left:12px solid #667eea;overflow:hidden;box-shadow:0 25px 50px rgba(0,0,0,0.6);min-height:160px;display:flex;flex-direction:column;justify-content:center;}}
    @media(max-width:768px){{.main-header{{padding:20px;border-left-width:6px;min-height:120px;}}}}
    #bg-carousel{{position:absolute;top:0;left:0;width:100%;height:100%;background-size:cover;background-position:center;opacity:.15;transition:background-image 2s ease-in-out;z-index:0;}}
    .overlay{{position:absolute;top:0;left:0;width:100%;height:100%;background:linear-gradient(rgba(10,10,16,.6) 0%, rgba(26,26,46,.8) 100%);z-index:1;pointer-events:none;}}
    @media(max-width:768px){{.overlay{{background:linear-gradient(rgba(10,10,16,.8) 0%, rgba(26,26,46,.9) 100%);}}}}
    .content{{position:relative;z-index:2;text-align:center;}}
    h1{{font-family:'Orbitron',monospace;text-transform:uppercase;letter-spacing:8px;font-size:3rem;margin:0;background:linear-gradient(45deg,#667eea,#764ba2,#f093fb);background-size:400% 400%;-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;animation:gradientMove 4s ease infinite;text-shadow:0 0 20px rgba(102,126,234,.6);}}
    @media(max-width:768px){{h1{{font-size:2rem;letter-spacing:4px;}}}}
    .status{{color:#667eea;font-weight:600;letter-spacing:4px;font-size:1rem;text-transform:uppercase;margin-top:12px;font-family:'Orbitron',monospace;}}
    @media(max-width:768px){{.status{{font-size:.85rem;letter-spacing:2px;}}}}
    @keyframes gradientMove{{0%,100%{{background-position:0% 50%}}50%{{background-position:100% 50%}}}}
    </style></head><body>
    <div class="main-header">
        <div id="bg-carousel"></div><div class="overlay"></div>
        <div class="content">
            <h1>Logistics<span style="font-weight:700;"> Intelligence</span></h1>
            <div class="status">Au service de l'optimisation des systèmes industriels et logistiques</div>
        </div>
    </div>
    <script>
    const images=["https://images.unsplash.com/photo-1579762715215-11e8e4e570e4?w=800","https://images.unsplash.com/photo-1558618047-3c8c76bbb17e?w=800","https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=800"];
    let index=0; const bgDiv=document.getElementById('bg-carousel');
    function changeBackground(){{bgDiv.style.backgroundImage=`url('${{images[index]}}')`;index=(index+1)%images.length;}}
    changeBackground();setInterval(changeBackground,4000);
    </script></body></html>
    """
    components.html(header_html, height=180)

# =============================================================================
# OUTILS - CONFIGURATION ✅ CORRIGÉE
# =============================================================================
TOOLS = [
    {
        "icon": "📦", 
        "title": "PALLET OPTIMIZER", 
        "desc": "Optimisation parfaite de vos palettes",
        "page": "pages/app1.py", 
        "key": "btn_app1",
        "is_soon": False
    },
    {
        "icon": "🚛", 
        "title": "CONTAINER OPTIMIZER", 
        "desc": "Maximisez l'espace conteneurs",
        "page": "pages/app2.py", 
        "key": "btn_app2",
        "is_soon": False
    },
    {
        "icon": "📊", 
        "title": "VOGEL SYSTEM", 
        "desc": "Algorithme approvisionnement",
        "page": "pages/app3.py", 
        "key": "btn_app3",
        "is_soon": False
    },
    {
        "icon": "⚙️", 
        "title": "MRP/CBN SOLUTION", 
        "desc": "Gestion besoins matériaux",
        "page": "pages/app4.py", 
        "key": "btn_app4",
        "is_soon": False
    },
    {
        "icon": "💰", 
        "title": "CALCULATOR TRANSPORT", 
        "desc": "Coûts transport précis",
        "page": "pages/app5.py", 
        "key": "btn_app5",
        "is_soon": False
    },
    {
        "icon": "📈", 
        "title": "SIX SIGMA", 
        "desc": "Réduction défauts & optimisation",
        "page": None, 
        "key": None,
        "is_soon": True
    }
]

def render_tool_card(tool, col_idx):
    """Rend une carte outil - ✅ KEYERROR CORRIGÉ"""
    # ✅ Vérification explicite de la clé "is_soon"
    is_soon = tool.get("is_soon", False)
    
    if is_soon:
        html = f'''
        <div class="soon-card">
            <span class="tool-icon">{tool["icon"]}</span>
            <div class="tool-title">{tool["title"]}</div>
            <div class="tool-desc">{tool["desc"]}</div>
            <div class="soon-text">🔥 COMING SOON</div>
        </div>
        '''
    else:
        html = f'''
        <div class="tool-card">
            <span class="tool-icon">{tool["icon"]}</span>
            <div class="tool-title">{tool["title"]}</div>
            <div class="tool-desc">{tool["desc"]}</div>
        </div>
        '''
    
    components.html(html, height=280)
    
    # ✅ Vérification explicite avant accès aux clés page/key
    if not is_soon and tool.get("page") and tool.get("key"):
        if st.button("🚀 LANCER", key=tool["key"], use_container_width=True):
            st.switch_page(tool["page"])

# =============================================================================
# RENDU PRINCIPAL
# =============================================================================
def main():
    # Header
    render_header()
    
    # Grille 1 - 3 premiers outils
    cols1 = st.columns([1, 1, 1])
    for i, col in enumerate(cols1):
        with col:
            render_tool_card(TOOLS[i], i)
    
    st.markdown("---")
    
    # Grille 2 - 3 derniers outils
    cols2 = st.columns([1, 1, 1])
    for i, col in enumerate(cols2):
        with col:
            render_tool_card(TOOLS[i+3], i+3)
    
    st.markdown("---*Optimisation logistique avancée - Suite complète d'outils*")

if __name__ == "__main__":
    main()
