# home.py - Page d'accueil Logistics Intelligence ✅ DARK & LIGHT MODES ✅ CORRIGÉ
import streamlit as st
import streamlit.components.v1 as components

# CSS pour cacher sidebar
st.markdown("""
<style>
    section[data-testid="stSidebar"] { display: none !important; width: 0 !important; visibility: hidden !important; }
    .stSidebarCollapsedControl { display: none !important; }
    [data-testid="collapsedControl"] { display: none !important; }
    .css-1d391kg, .css-mkog8s { display: none !important; }
</style>
""", unsafe_allow_html=True)

# Configuration
st.set_page_config(
    page_title="Logistics Intelligence", 
    page_icon="🚚", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Fonction pour détecter le thème
def get_theme():
    try:
        return st.get_option("theme.base") or "light"
    except:
        return "light"

# Détection thème
theme = get_theme()
is_dark = theme == "dark"

# CSS adaptatif DARK/LIGHT ✅ F-STRING CORRIGÉ
css_dark = """
:root {
    --bg-primary: #0f0f23, #1a1a2e, #16213e;
    --bg-card: rgba(102,126,234,0.2), rgba(118,75,162,0.2);
    --text-primary: #e2e8f0;
    --text-secondary: #94a3b8;
    --border-color: rgba(255,255,255,0.2);
    --shadow-color: rgba(102,126,234,0.3);
    --accent-color: #667eea;
}
body { 
    background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 50%, #16213e 100%); 
    color: var(--text-primary); 
}
.main-header {
    background: linear-gradient(135deg, rgba(10,10,16,0.95), rgba(26,26,46,0.95));
    box-shadow: 0 30px 60px rgba(0,0,0,0.8);
}
.tool-card:hover { box-shadow: 0 35px 70px rgba(102,126,234,0.5); }
.soon-card {
    background: linear-gradient(145deg, rgba(34,197,94,0.25), rgba(16,185,129,0.25));
    border-color: rgba(34,197,94,0.5);
    box-shadow: 0 25px 50px rgba(34,197,94,0.4);
}
@keyframes pulse {
    0%, 100% { box-shadow: 0 25px 50px rgba(34,197,94,0.4); }
    50% { box-shadow: 0 25px 50px rgba(34,197,94,0.7); }
}
.stButton > button {
    background: linear-gradient(135deg, rgba(102,126,234,0.2), rgba(118,75,162,0.2));
    border-color: rgba(102,126,234,0.5);
    box-shadow: 0 12px 30px rgba(0,0,0,0.3);
}
.stButton > button:hover {
    background: linear-gradient(135deg, rgba(102,126,234,0.4), rgba(118,75,162,0.4));
    box-shadow: 0 20px 40px rgba(102,126,234,0.6);
}
"""

css_light = """
:root {
    --bg-primary: #f8fafc, #e2e8f0, #cbd5e1;
    --bg-card: rgba(102,126,234,0.1), rgba(118,75,162,0.1);
    --text-primary: #1e293b;
    --text-secondary: #64748b;
    --border-color: rgba(0,0,0,0.1);
    --shadow-color: rgba(102,126,234,0.2);
    --accent-color: #667eea;
}
body { 
    background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 50%, #cbd5e1 100%); 
    color: var(--text-primary); 
}
.main-header {
    background: linear-gradient(135deg, rgba(248,250,252,0.95), rgba(226,232,240,0.95));
    box-shadow: 0 20px 40px rgba(0,0,0,0.1);
}
.tool-card:hover { box-shadow: 0 35px 70px rgba(102,126,234,0.3); }
.soon-card {
    background: linear-gradient(145deg, rgba(34,197,94,0.15), rgba(16,185,129,0.15));
    border-color: rgba(34,197,94,0.3);
    box-shadow: 0 25px 50px rgba(34,197,94,0.2);
}
@keyframes pulse {
    0%, 100% { box-shadow: 0 25px 50px rgba(34,197,94,0.2); }
    50% { box-shadow: 0 25px 50px rgba(34,197,94,0.4); }
}
.stButton > button {
    background: linear-gradient(135deg, rgba(102,126,234,0.1), rgba(118,75,162,0.1));
    border-color: rgba(102,126,234,0.3);
    box-shadow: 0 12px 30px rgba(0,0,0,0.15);
}
.stButton > button:hover {
    background: linear-gradient(135deg, rgba(102,126,234,0.2), rgba(118,75,162,0.2));
    box-shadow: 0 20px 40px rgba(102,126,234,0.4);
}
"""

# CSS commun + thème spécifique
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700&family=Inter:wght@300;400;500;600;700&display=swap');

* { font-family: 'Inter', sans-serif; }
h1, h2, h3 { 
    color: var(--text-primary) !important; 
    font-family: 'Orbitron', monospace !important; 
    text-shadow: var(--text-shadow, '0 2px 10px rgba(102,126,234,0.5)');
}
.main-header {
    padding: 2.5rem; backdrop-filter: blur(25px); 
    border-radius: 24px; border-left: 8px solid var(--accent-color); 
    margin-bottom: 2rem;
}
.tool-card { 
    color: var(--text-primary) !important; 
    padding: 2.5rem 1.5rem !important; 
    border-radius: 24px !important; 
    text-align: center !important; 
    border: 2px solid var(--border-color) !important; 
    margin: 1rem 0.5rem !important;
    height: 240px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    transition: all 0.3s ease !important;
    position: relative;
    overflow: hidden;
}
.tool-card:hover {
    transform: translateY(-10px) scale(1.02) !important;
    border-color: var(--accent-color) !important;
}
.soon-card {
    padding: 2.5rem 1.5rem !important; 
    border-radius: 24px !important; 
    text-align: center !important; 
    margin: 1rem 0.5rem !important;
    height: 240px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    animation: pulse 2s infinite;
}
.tool-icon { font-size: 4rem !important; margin-bottom: 1.2rem; display: block; }
.tool-title { 
    font-size: 1.3rem !important; font-weight: 700 !important;
    font-family: 'Orbitron', monospace !important;
    margin-bottom: 0.8rem;
    text-transform: uppercase;
    letter-spacing: 1.5px;
}
.tool-desc { 
    font-size: 0.92rem !important; 
    opacity: 0.9 !important; 
    line-height: 1.5;
}
.soon-text {
    font-size: 1.1rem !important;
    color: #22c55e !important;
    font-weight: 600 !important;
    margin-top: 0.5rem;
}
.stButton > button {
    border-radius: 16px !important; 
    padding: 0.8rem 2rem !important;
    font-family: 'Orbitron', monospace !important;
    font-weight: 600 !important; 
    font-size: 0.85rem !important;
    color: var(--text-primary) !important;
    text-transform: uppercase !important; 
    letter-spacing: 1px !important;
    height: 48px !important;
    width: 100% !important;
    margin-top: 1rem !important;
    backdrop-filter: blur(20px) !important;
}
.stButton > button:hover {
    transform: translateY(-4px) scale(1.05) !important; 
    border-color: var(--accent-color) !important;
}
""" + (css_dark if is_dark else css_light), unsafe_allow_html=True)

# Header adaptatif
header_bg = "#0a0a10, #1a1a2e" if is_dark else "#f8fafc, #e2e8f0"
header_overlay = "rgba(10,10,16,0.5) 0%, rgba(26,26,46,0.7) 100%" if is_dark else "rgba(248,250,252,0.8) 0%, rgba(226,232,240,0.9) 100%"
header_shadow = "0 30px 60px rgba(0,0,0,0.8)" if is_dark else "0 20px 40px rgba(0,0,0,0.1)"
bg_opacity = "0.2" if is_dark else "0.1"

header_code = f"""
<!DOCTYPE html>
<html>
<head>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Inter:wght@400;700&display=swap" rel="stylesheet">
<style>
    body {{ margin: 0; padding: 0; background-color: transparent; font-family: 'Inter', sans-serif; overflow: hidden; }}
    .main-header {{
        position: relative; padding: 35px; 
        background: linear-gradient(135deg, {header_bg}); 
        border-radius: 24px; border-left: 12px solid #667eea; overflow: hidden; 
        box-shadow: {header_shadow}; 
        min-height: 160px; display: flex; flex-direction: column; justify-content: center;
    }}
    #bg-carousel {{ position: absolute; top: 0; left: 0; width: 100%; height: 100%;
        background-size: cover; background-position: center; opacity: {bg_opacity}; 
        transition: background-image 2s ease-in-out; z-index: 0;
    }}
    .overlay {{ position: absolute; top: 0; left: 0; width: 100%; height: 100%;
        background: linear-gradient({header_overlay});
        z-index: 1; pointer-events: none;
    }}
    .content {{ position: relative; z-index: 2; text-align: center; }}
    h1 {{ font-family: 'Orbitron', monospace; text-transform: uppercase; letter-spacing: 8px; 
        font-size: 3rem; margin: 0; background: linear-gradient(45deg, #667eea, #764ba2, #f093fb);
        background-size: 400% 400%; -webkit-background-clip: text; background-clip: text;
        -webkit-text-fill-color: transparent; animation: gradientMove 4s ease infinite;
        text-shadow: 0 0 20px rgba(102,126,234,0.6);
    }}
    .status {{ color: #667eea; font-weight: 600; letter-spacing: 4px; font-size: 1rem; 
        text-transform: uppercase; margin-top: 12px; font-family: 'Orbitron', monospace;
    }}
    @keyframes gradientMove {{ 0%,100%{{background-position:0% 50%}} 50%{{background-position:100% 50%}} }}
</style>
</head>
<body>
    <div class="main-header">
        <div id="bg-carousel"></div>
        <div class="overlay"></div>
        <div class="content">
            <h1>Logistics<span style="font-weight: 700;"> Intelligence</span></h1>
            <div class="status">Au service de l'optimisation des systèmes industriels et logistiques</div>
        </div>
    </div>
    <script>
        const images = [
            "https://images.unsplash.com/photo-1579762715215-11e8e4e570e4?w=800",
            "https://images.unsplash.com/photo-1558618047-3c8c76bbb17e?w=800", 
            "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=800"
        ];
        let index = 0;
        const bgDiv = document.getElementById('bg-carousel');
        function changeBackground() {{
            bgDiv.style.backgroundImage = `url('${{images[index]}}')`;
            index = (index + 1) % images.length;
        }}
        changeBackground();
        setInterval(changeBackground, 4000);
    </script>
</body>
</html>
"""
components.html(header_code, height=200)

# CONTENU (identique aux versions précédentes)
st.markdown("### 🚀 **Plateforme d'Optimisation Logistique**")

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('''
    <div class="tool-card">
        <span class="tool-icon">📦</span>
        <div class="tool-title">PALLET OPTIMIZER</div>
        <div class="tool-desc">Optimisation parfaite de vos palettes</div>
    </div>
    ''', unsafe_allow_html=True)
    if st.button("🚀 LANCER", key="btn_app1", use_container_width=True):
        st.switch_page("pages/app1.py")

with col2:
    st.markdown('''
    <div class="tool-card">
        <span class="tool-icon">🚛</span>
        <div class="tool-title">CONTAINER OPTIMIZER</div>
        <div class="tool-desc">Maximisez l'espace conteneurs</div>
    </div>
    ''', unsafe_allow_html=True)
    if st.button("🚀 LANCER", key="btn_app2", use_container_width=True):
        st.switch_page("pages/app2.py")

with col3:
    st.markdown('''
    <div class="tool-card">
        <span class="tool-icon">📊</span>
        <div class="tool-title">VOGEL SYSTEM</div>
        <div class="tool-desc">Algorithme approvisionnement</div>
    </div>
    ''', unsafe_allow_html=True)
    if st.button("🚀 LANCER", key="btn_app3", use_container_width=True):
        st.switch_page("pages/app3.py")

col4, col5, col6 = st.columns(3)
st.markdown("---")

with col4:
    st.markdown('''
    <div class="tool-card">
        <span class="tool-icon">⚙️</span>
        <div class="tool-title">MRP/CBN SOLUTION</div>
        <div class="tool-desc">Gestion besoins matériaux</div>
    </div>
    ''', unsafe_allow_html=True)
    if st.button("🚀 LANCER", key="btn_app4", use_container_width=True):
        st.switch_page("pages/app4.py")

with col5:
    st.markdown('''
    <div class="tool-card">
        <span class="tool-icon">💰</span>
        <div class="tool-title">CALCULATOR TRANSPORT</div>
        <div class="tool-desc">Coûts transport précis</div>
    </div>
    ''', unsafe_allow_html=True)
    if st.button("🚀 LANCER", key="btn_app5", use_container_width=True):
        st.switch_page("pages/app5.py")

with col6:
    st.markdown('''
    <div class="soon-card">
        <span class="tool-icon">📈</span>
        <div class="tool-title">SIX SIGMA</div>
        <div class="tool-desc">Réduction défauts & optimisation</div>
        <div class="soon-text">🔥 COMING SOON</div>
    </div>
    ''', unsafe_allow_html=True)

st.markdown("---")
st.markdown("*Optimisation logistique avancée - Suite complète d'outils*")
