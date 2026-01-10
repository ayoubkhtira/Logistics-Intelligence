# home.py - Page d'accueil Logistics Intelligence (avec Six Sigma)
import streamlit as st
import streamlit.components.v1 as components

# Configuration
st.set_page_config(
    page_title="Logistics Intelligence", 
    page_icon="🚚", 
    layout="wide"
)

# CSS Styling
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700&family=Inter:wght@300;400;500;600;700&display=swap');

* { font-family: 'Inter', sans-serif; }
body { 
    background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 50%, #16213e 100%); 
    color: #e2e8f0; 
}

h1, h2, h3 { 
    color: #f8fafc !important; 
    font-family: 'Orbitron', monospace !important; 
    text-shadow: 0 2px 10px rgba(102,126,234,0.5); 
}

.main-header {
    padding: 2.5rem; 
    background: linear-gradient(135deg, rgba(10,10,16,0.95), rgba(26,26,46,0.95));
    backdrop-filter: blur(25px); 
    border-radius: 24px; 
    border-left: 8px solid #667eea; 
    box-shadow: 0 30px 60px rgba(0,0,0,0.8); 
    margin-bottom: 2rem;
}
.header-title {
    font-size: 3rem; 
    font-weight: 700; 
    letter-spacing: 6px; 
    text-transform: uppercase;
    background: linear-gradient(45deg, #667eea, #764ba2, #f093fb, #667eea);
    background-size: 400% 400%; 
    -webkit-background-clip: text; 
    background-clip: text; 
    -webkit-text-fill-color: transparent; 
    animation: gradientMove 5s ease infinite;
    text-align: center;
}

.tool-card { 
    background: linear-gradient(145deg, rgba(102,126,234,0.2), rgba(118,75,162,0.2)) !important;
    backdrop-filter: blur(20px); 
    color: white !important; 
    padding: 2.5rem 1.5rem !important; 
    border-radius: 24px !important; 
    text-align: center !important; 
    border: 2px solid rgba(255,255,255,0.2) !important; 
    box-shadow: 0 25px 50px rgba(102,126,234,0.3) !important; 
    margin: 1rem 0.5rem !important;
    height: 220px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    transition: all 0.3s ease !important;
}
.tool-card:hover {
    transform: translateY(-8px) scale(1.02) !important;
    box-shadow: 0 35px 70px rgba(102,126,234,0.5) !important;
    border-color: #667eea !important;
}

.soon-card {
    background: linear-gradient(145deg, rgba(34,197,94,0.2), rgba(16,185,129,0.2)) !important;
    backdrop-filter: blur(20px); 
    color: #e2e8f0 !important; 
    padding: 2.5rem 1.5rem !important; 
    border-radius: 24px !important; 
    text-align: center !important; 
    border: 2px solid rgba(34,197,94,0.4) !important; 
    box-shadow: 0 25px 50px rgba(34,197,94,0.3) !important; 
    margin: 1rem 0.5rem !important;
    height: 220px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    animation: pulse 2s infinite;
}
@keyframes pulse {
    0% { box-shadow: 0 25px 50px rgba(34,197,94,0.3); }
    50% { box-shadow: 0 25px 50px rgba(34,197,94,0.6); }
    100% { box-shadow: 0 25px 50px rgba(34,197,94,0.3); }
}

.tool-icon { 
    font-size: 3.5rem !important; 
    margin-bottom: 1rem;
    display: block;
}
.tool-title { 
    font-size: 1.4rem !important; 
    font-weight: 700 !important;
    font-family: 'Orbitron', monospace !important;
    margin-bottom: 0.8rem;
    text-transform: uppercase;
    letter-spacing: 1px;
}
.tool-desc { 
    font-size: 0.95rem !important; 
    opacity: 0.9 !important; 
    line-height: 1.5;
}
.soon-text {
    font-size: 1.1rem !important;
    color: #22c55e !important;
    font-weight: 600 !important;
}

.stButton > button {
    background: linear-gradient(135deg, rgba(102,126,234,0.2), rgba(118,75,162,0.2)) !important;
    backdrop-filter: blur(20px) !important; 
    border: 2px solid rgba(102,126,234,0.5) !important;
    border-radius: 16px !important; 
    padding: 0.8rem 2rem !important;
    font-family: 'Orbitron', monospace !important;
    font-weight: 600 !important; 
    font-size: 0.85rem !important;
    color: #e2e8f0 !important;
    text-transform: uppercase !important; 
    box-shadow: 0 12px 30px rgba(0,0,0,0.3) !important;
    letter-spacing: 1px !important;
    height: 48px !important;
    width: 100% !important;
    margin-top: 1rem !important;
}
.stButton > button:hover {
    transform: translateY(-4px) scale(1.05) !important; 
    background: linear-gradient(135deg, rgba(102,126,234,0.4), rgba(118,75,162,0.4)) !important;
    box-shadow: 0 20px 40px rgba(102,126,234,0.6) !important; 
    border-color: #667eea !important;
}

@keyframes gradientMove { 
    0%,100%{background-position:0% 50%} 
    50%{background-position:100% 50%}
}
</style>
""", unsafe_allow_html=True)

# Header
header_code = """
<!DOCTYPE html>
<html>
<head>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Inter:wght@400;700&display=swap" rel="stylesheet">
<style>
    body { margin: 0; padding: 0; background-color: transparent; font-family: 'Inter', sans-serif; overflow: hidden; }
    .main-header {
        position: relative; padding: 35px; background: linear-gradient(135deg, #0a0a10, #1a1a2e); 
        border-radius: 24px; border-left: 12px solid #667eea; overflow: hidden; 
        box-shadow: 0 30px 60px rgba(0,0,0,0.8); min-height: 160px; 
        display: flex; flex-direction: column; justify-content: center;
    }
    #bg-carousel { position: absolute; top: 0; left: 0; width: 100%; height: 100%;
        background-size: cover; background-position: center; opacity: 0.2; 
        transition: background-image 2s ease-in-out; z-index: 0;
    }
    .overlay { position: absolute; top: 0; left: 0; width: 100%; height: 100%;
        background: linear-gradient(rgba(10,10,16,0.5) 0%, rgba(26,26,46,0.7) 100%);
        z-index: 1; pointer-events: none;
    }
    .content { position: relative; z-index: 2; text-align: center; }
    h1 { font-family: 'Orbitron', monospace; text-transform: uppercase; letter-spacing: 8px; 
        font-size: 3rem; margin: 0; background: linear-gradient(45deg, #667eea, #764ba2, #f093fb);
        background-size: 400% 400%; -webkit-background-clip: text; background-clip: text;
        -webkit-text-fill-color: transparent; animation: gradientMove 4s ease infinite;
        text-shadow: 0 0 20px rgba(102,126,234,0.6);
    }
    .status { color: #667eea; font-weight: 600; letter-spacing: 4px; font-size: 1rem; 
        text-transform: uppercase; margin-top: 12px; font-family: 'Orbitron', monospace;
    }
    @keyframes gradientMove { 0%,100%{background-position:0% 50%} 50%{background-position:100% 50%} }
</style>
</head>
<body>
    <div class="main-header">
        <div id="bg-carousel"></div>
        <div class="overlay"></div>
        <div class="content">
            <h1>Logistics<span style="font-weight: 700;">  Intelligence</span></h1>
            <div class="status">L’intelligence au service de l’optimisation des systèmes industriels et logistiques</div>
        </div>
    </div>
    <script>
        const images = [
            "https://cdn.pixabay.com/photo/2012/03/04/00/06/business-21755_1280.jpg",
            "https://cdn.pixabay.com/photo/2022/08/07/11/33/port-7370411_1280.jpg", 
        ];
        let index = 0;
        const bgDiv = document.getElementById('bg-carousel');
        function changeBackground() {
            bgDiv.style.backgroundImage = `url('${images[index]}')`;
            index = (index + 1) % images.length;
        }
        changeBackground();
        setInterval(changeBackground, 4000);
    </script>
</body>
</html>
"""

components.html(header_code, height=200)

# Outils
st.markdown("### 🚀 Plateforme d'Optimisation Logistique")

# Grille 3x2
col1, col2, col3 = st.columns(3)

tools = [
    {"icon": "📦", "title": "PALLET OPTIMIZER", "desc": "Optimisation 3D palettes", "page": "app1"},
    {"icon": "🚛", "title": "CONTAINER OPTIMIZER", "desc": "Maximisation conteneurs", "page": "app2"},
    {"icon": "📊", "title": "VOGEL SYSTEM", "desc": "Algorithme approvisionnement", "page": "app3"}
]

# Première ligne
with col1:
    tool = tools[0]
    st.markdown(f'''
    <div class="tool-card">
        <span class="tool-icon">{tool["icon"]}</span>
        <div class="tool-title">{tool["title"]}</div>
        <div class="tool-desc">{tool["desc"]}</div>
    </div>
    ''', unsafe_allow_html=True)
    if st.button("🚀 LANCER L'OUTIL", key=f"btn_{tool['page']}", use_container_width=True):
        st.switch_page(f"pages/{tool['page']}.py")

with col2:
    tool = tools[1]
    st.markdown(f'''
    <div class="tool-card">
        <span class="tool-icon">{tool["icon"]}</span>
        <div class="tool-title">{tool["title"]}</div>
        <div class="tool-desc">{tool["desc"]}</div>
    </div>
    ''', unsafe_allow_html=True)
    if st.button("🚀 LANCER L'OUTIL", key=f"btn_{tool['page']}", use_container_width=True):
        st.switch_page(f"pages/{tool['page']}.py")

with col3:
    tool = tools[2]
    st.markdown(f'''
    <div class="tool-card">
        <span class="tool-icon">{tool["icon"]}</span>
        <div class="tool-title">{tool["title"]}</div>
        <div class="tool-desc">{tool["desc"]}</div>
    </div>
    ''', unsafe_allow_html=True)
    if st.button("🚀 LANCER L'OUTIL", key=f"btn_{tool['page']}", use_container_width=True):
        st.switch_page(f"pages/{tool['page']}.py")

# Deuxième ligne
col4, col5, col6 = st.columns(3)
st.markdown("---")

with col4:
    tool = {"icon": "⚙️", "title": "MRP/CBN SOLUTION", "desc": "Gestion besoins matériaux", "page": "app4"}
    st.markdown(f'''
    <div class="tool-card">
        <span class="tool-icon">{tool["icon"]}</span>
        <div class="tool-title">{tool["title"]}</div>
        <div class="tool-desc">{tool["desc"]}</div>
    </div>
    ''', unsafe_allow_html=True)
    if st.button("🚀 LANCER L'OUTIL", key=f"btn_{tool['page']}", use_container_width=True):
        st.switch_page(f"pages/{tool['page']}.py")

with col5:
    tool = {"icon": "💰", "title": "CALCULATOR TRANSPORT", "desc": "Coûts transport précis", "page": "app5"}
    st.markdown(f'''
    <div class="tool-card">
        <span class="tool-icon">{tool["icon"]}</span>
        <div class="tool-title">{tool["title"]}</div>
        <div class="tool-desc">{tool["desc"]}</div>
    </div>
    ''', unsafe_allow_html=True)
    if st.button("🚀 LANCER L'OUTIL", key=f"btn_{tool['page']}", use_container_width=True):
        st.switch_page(f"pages/{tool['page']}.py")

with col6:
    # Bloc Six Sigma "Coming Soon"
    st.markdown('''
    <div class="soon-card">
        <span class="tool-icon">📈</span>
        <div class="tool-title">SIX SIGMA</div>
        <div class="tool-desc">Réduction des défauts & optimisation processus</div>
        <div class="soon-text">🔥 COMING SOON</div>
    </div>
    ''', unsafe_allow_html=True)


