import streamlit as st
from dataclasses import dataclass
from datetime import date, timedelta
import pandas as pd
import plotly.express as px
import io
import openpyxl
import streamlit.components.v1 as components

# Classes
@dataclass
class Article:
    code: str
    name: str
    type: str
    lead_time: int
    unit_cost: float

@dataclass
class BOM:
    parent: str
    component: str
    quantity: float

@dataclass
class Stock:
    article: str
    qty: float
    safety: float

@dataclass
class Demand:
    client: str
    article: str
    qty: float
    due_date: date

# Configuration
st.set_page_config(page_title="MRP/CBN SOLUTION", page_icon="🧠", layout="wide")

# CSS OPTIMISÉ - HAUTEURS RÉDUITES + DARK/LIGHT
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700&family=Inter:wght@300;400;500;600;700&display=swap');

/* SUPPRIME ESPACES INUTILES */
section[data-testid="stSidebar"] { padding-top: 0.5rem !important; }
.main .block-container { padding-top: 1rem !important; padding-bottom: 1rem !important; }
[data-testid="column"]:first-child > div > div { padding-top: 0.5rem !important; }

* { font-family: 'Inter', sans-serif; }

/* Variables Dark/Light */
:root {
    --bg-primary: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 50%, #16213e 100%);
    --bg-secondary: rgba(10,10,16,0.95);
    --text-primary: #e2e8f0;
    --text-secondary: #94a3b8;
    --accent-primary: #667eea;
    --accent-secondary: #764ba2;
    --glass-bg: rgba(255,255,255,0.95);
    --glass-border: rgba(102,126,234,0.3);
    --shadow-primary: rgba(0,0,0,0.8);
    --success-bg: rgba(16,185,129,0.2);
    --error-bg: rgba(239,68,68,0.2);
}

[data-testid="stAppViewContainer"] {
    background: var(--bg-primary) !important;
    color: var(--text-primary) !important;
}

h1, h2, h3 { 
    color: var(--text-primary) !important; 
    font-family: 'Orbitron', monospace !important; 
    text-shadow: 0 2px 10px rgba(102,126,234,0.5); 
    margin: 0.5rem 0 !important;
}

.main-header {
    padding: 1.5rem !important; /* RÉDUIT */
    background: linear-gradient(135deg, var(--bg-secondary), rgba(26,26,46,0.95));
    backdrop-filter: blur(25px); 
    border-radius: 20px !important; /* RÉDUIT */
    border-left: 6px solid var(--accent-primary) !important; /* RÉDUIT */
    box-shadow: 0 20px 40px var(--shadow-primary) !important; /* RÉDUIT */
    margin-bottom: 1rem !important; /* RÉDUIT */
}

.header-title {
    font-size: 2.2rem !important; /* RÉDUIT */
    font-weight: 700; 
    letter-spacing: 4px !important; /* RÉDUIT */
    text-transform: uppercase;
    background: linear-gradient(45deg, var(--accent-primary), var(--accent-secondary), #f093fb, var(--accent-primary));
    background-size: 400% 400%; 
    -webkit-background-clip: text; 
    background-clip: text; 
    -webkit-text-fill-color: transparent; 
    animation: gradientMove 5s ease infinite;
    text-align: center;
}

/* BOUTONS COMPACTS */
.stButton > button {
    background: linear-gradient(135deg, rgba(102,126,234,0.15), rgba(118,75,162,0.15)) !important;
    backdrop-filter: blur(20px) !important; 
    border: 2px solid var(--glass-border) !important;
    border-radius: 16px !important; /* RÉDUIT */
    padding: 0.5rem 0.8rem !important; /* RÉDUIT */
    margin: 0.2rem !important; /* RÉDUIT */
    min-width: 100px !important; /* RÉDUIT */
    max-width: 120px !important; /* RÉDUIT */
    font-family: 'Orbitron', monospace !important;
    font-weight: 600 !important; 
    font-size: 0.75rem !important; /* RÉDUIT */
    color: var(--text-primary) !important;
    text-transform: uppercase !important; 
    box-shadow: 0 8px 25px rgba(0,0,0,0.3) !important; /* RÉDUIT */
    height: 38px !important; /* RÉDUIT */
    letter-spacing: 0.4px !important; /* RÉDUIT */
    transition: all 0.3s cubic-bezier(0.4,0,0.2,1) !important;
}

.stButton > button:hover {
    transform: translateY(-4px) scale(1.02) !important; /* RÉDUIT */
    background: linear-gradient(135deg, rgba(102,126,234,0.3), rgba(118,75,162,0.3)) !important;
    box-shadow: 0 15px 30px rgba(102,126,234,0.5) !important; 
    border-color: var(--accent-primary) !important;
}

/* CARTES MÉTRIQUES COMPACTES */
.metric-card { 
    background: linear-gradient(145deg, rgba(102,126,234,0.2), rgba(118,75,162,0.2)) !important;
    backdrop-filter: blur(20px); 
    color: white !important; 
    padding: 1.2rem !important; /* RÉDUIT */
    border-radius: 16px !important; /* RÉDUIT */
    text-align: center !important; 
    border: 2px solid rgba(255,255,255,0.2) !important; 
    box-shadow: 0 15px 30px rgba(102,126,234,0.4) !important; /* RÉDUIT */
    margin: 0.5rem !important; /* RÉDUIT */
}
.metric-value { 
    font-size: 2rem !important; /* RÉDUIT */
    font-weight: 700 !important; 
}
.metric-label { 
    font-size: 0.85rem !important; /* RÉDUIT */
    opacity: 0.95 !important; 
}

/* INPUTS COMPACTS */
.stTextInput > div > div > input, 
.stNumberInput > div > div > input, 
.stSelectbox > div > div > select, 
.stDateInput > div > div > input {
    background: var(--glass-bg) !important; 
    border-radius: 12px !important; /* RÉDUIT */
    border: 2px solid var(--glass-border) !important; 
    padding: 0.8rem !important; /* RÉDUIT */
    font-weight: 500 !important; 
    color: #1e293b !important;
    font-size: 0.95rem !important; /* RÉDUIT */
}

/* DATAFRAME COMPACT */
.stDataFrame { 
    background: var(--glass-bg) !important; 
    border-radius: 16px !important; /* RÉDUIT */
    box-shadow: 0 15px 40px rgba(0,0,0,0.2) !important; /* RÉDUIT */
}
.element-container .row-widget { padding: 0.5rem 0 !important; }

/* MESSAGES COMPACTS */
.success-box, .error-box {
    padding: 1rem !important; /* RÉDUIT */
    border-radius: 12px !important; /* RÉDUIT */
    margin: 0.5rem 0 !important; /* RÉDUIT */
    backdrop-filter: blur(15px); 
    border-left: 5px solid !important; /* RÉDUIT */
}
.success-box { 
    background: linear-gradient(135deg, var(--success-bg), rgba(5,150,105,0.2)) !important; 
    color: white !important; 
    border-left-color: #10b981 !important; 
}
.error-box { 
    background: linear-gradient(135deg, var(--error-bg), rgba(220,38,38,0.2)) !important; 
    color: white !important; 
    border-left-color: #ef4444 !important; 
}

@keyframes gradientMove { 
    0%,100%{background-position:0% 50%} 
    50%{background-position:100% 50%}
}
</style>
""", unsafe_allow_html=True)

# Header COMPACT
header_code = """
<!DOCTYPE html>
<html>
<head>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Inter:wght@400;700&display=swap" rel="stylesheet">
<style>
body { margin: 0; padding: 0; background-color: transparent; font-family: 'Inter', sans-serif; overflow: hidden; }
.main-header {
    position: relative; padding: 20px !important; /* RÉDUIT */
    background: linear-gradient(135deg, rgba(10,10,16,0.95), rgba(26,26,46,0.95)); 
    border-radius: 20px !important; /* RÉDUIT */
    border-left: 8px solid #667eea !important; /* RÉDUIT */
    overflow: hidden; box-shadow: 0 20px 40px rgba(0,0,0,0.8) !important; /* RÉDUIT */
    min-height: 110px !important; /* RÉDUIT */
    display: flex; flex-direction: column; justify-content: center;
}
#bg-carousel { position: absolute; top: 0; left: 0; width: 100%; height: 100%; background-size: cover; background-position: center; opacity: 0.25; transition: background-image 2s ease-in-out; z-index: 0; }
.overlay { position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(rgba(10,10,16,0.4) 0%, rgba(26,26,46,0.6) 100%); z-index: 1; pointer-events: none; }
.content { position: relative; z-index: 2; text-align: center; }
h1 { font-family: 'Orbitron', monospace; text-transform: uppercase; letter-spacing: 4px !important; font-size: 2rem !important; /* RÉDUIT */ margin: 0; 
    background: linear-gradient(45deg, #667eea, #764ba2, #f093fb); background-size: 400% 400%; -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent; 
    animation: gradientMove 4s ease infinite; text-shadow: 0 0 20px rgba(102,126,234,0.6); }
.status { color: #667eea; font-weight: 600; letter-spacing: 2px !important; /* RÉDUIT */ font-size: 0.8rem !important; /* RÉDUIT */ text-transform: uppercase; margin-top: 5px !important; /* RÉDUIT */ font-family: 'Orbitron', monospace; }
@keyframes gradientMove { 0%,100%{background-position:0% 50%} 50%{background-position:100% 50%} }
@keyframes blink { 0% { opacity: 1; } 50% { opacity: 0.3; } 100% { opacity: 1; } }
.active-dot { display: inline-block; width: 10px !important; /* RÉDUIT */ height: 10px !important; /* RÉDUIT */ background: #667eea; border-radius: 50%; margin-left: 10px !important; /* RÉDUIT */ animation: blink 2s infinite; box-shadow: 0 0 10px #667eea; }
</style>
</head>
<body>
    <div class="main-header">
        <div id="bg-carousel"></div>
        <div class="overlay"></div>
        <div class="content">
            <h1>MRP/CBN <span style="font-weight: 700;">Solution</span></h1>
            <div class="status">Manufacturing Excellence <span class="active-dot"></span></div>
        </div>
    </div>
    <script>
        const images = ["https://www.azart.fr/photo/art/grande/9724951-15680569.jpg?v=1466608504","https://ts2.mm.bing.net/th?id=OIP.3lcfFwaiQLjVRmVEnIJgRQHaE7&pid=15.1","https://ts1.mm.bing.net/th?id=OIP.w3xJ3p8KSGx-PmSJz-HxHwHaE8&pid=15.1"];
        let index = 0; const bgDiv = document.getElementById('bg-carousel');
        function changeBackground() { bgDiv.style.backgroundImage = `url('${images[index]}')`; index = (index + 1) % images.length; }
        changeBackground(); setInterval(changeBackground, 4000);
    </script>
</body>
</html>
"""
components.html(header_code, height=130)  # RÉDUIT

# Session State
if 'current_tab' not in st.session_state:
    st.session_state.current_tab = 0
    st.session_state.state = {
        'articles': {}, 'boms': [], 'stocks': {}, 'demands': [], 'mrp_results': pd.DataFrame()
    }

state = st.session_state.state

# Navigation COMPACTE
cols = st.columns(7)
tabs = ["Dashboard", "Articles", "Stocks", "BOM", "Demande", "MRP", "Export"]
for i, (col, tab_name) in enumerate(zip(cols, tabs)):
    with col:
        if st.button(tab_name, key=f"nav_{i}", use_container_width=True):
            st.session_state.current_tab = i
            st.rerun()

st.markdown("---")

# MRP Functions (inchangées)
def explode_bom(article_code: str, qty: float, visited=None):
    if visited is None: visited = set()
    if article_code in visited: return {}
    visited = visited.copy(); visited.add(article_code)
    needs = {}
    for bom in state['boms']:
        if bom.parent == article_code:
            required = qty * bom.quantity
            needs[bom.component] = needs.get(bom.component, 0) + required
            sub_needs = explode_bom(bom.component, required, visited)
            for k, v in sub_needs.items():
                needs[k] = needs.get(k, 0) + v
    return needs

def calculate_mrp():
    results = []
    for d in state['demands']:
        gross_needs = {d.article: d.qty}
        exploded = explode_bom(d.article, d.qty)
        gross_needs.update(exploded)
        for art_code, qty in gross_needs.items():
            if art_code not in state['articles']: continue
            art = state['articles'][art_code]
            stock = state['stocks'].get(art_code, Stock(art_code, 0, 0))
            net = max(qty - stock.qty + stock.safety, 0)
            lead = art.lead_time
            order_date = d.due_date - timedelta(days=lead)
            results.append({
                "Article": art.name, "Code": art_code, "Besoin Brut": qty,
                "Stock": stock.qty, "Sécurité": stock.safety, "Besoin Net": net,
                "Date Ordre": order_date.strftime('%Y-%m-%d'),
                "Type": "🛒 OA" if art.type == "BRUT" else "🏭 OF",
                "Coût": round(net * art.unit_cost, 2)
            })
    df = pd.DataFrame(results)
    state['mrp_results'] = df.sort_values('Date Ordre') if not df.empty else df
    return df

# Tab Content
current_tab = st.session_state.current_tab

if current_tab == 0:  # Dashboard
    st.markdown("### 🎯 Vue d'ensemble", unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    total_stock = sum(s.qty for s in state['stocks'].values())
    
    with col1:
        st.markdown(f'<div class="metric-card"><div class="metric-value">{len(state["demands"])}</div><div class="metric-label">📈 Demandes</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="metric-card"><div class="metric-value">{len(state["articles"])}</div><div class="metric-label">📦 Articles</div></div>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<div class="metric-card"><div class="metric-value">{len(state["stocks"])}</div><div class="metric-label">🏬 Stocks</div></div>', unsafe_allow_html=True)
    with col4:
        st.markdown(f'<div class="metric-card"><div class="metric-value">{total_stock:.0f}</div><div class="metric-label">📊 Total Stock</div></div>', unsafe_allow_html=True)

elif current_tab == 1:  # Articles
    st.markdown("### 📦 Gestion Articles")
    col1, col2 = st.columns(2)
    with col1:
        code = st.text_input("💾 Code", key="art_code")
        art_type = st.selectbox("Type", ["BRUT", "COMPOSE"], key="art_type")
    with col2:
        name = st.text_input("📝 Nom", key="art_name")
        lead = st.number_input("⏱️ Délai", value=5, key="art_lead")
        cost = st.number_input("💰 Coût", value=10.0, key="art_cost")
    
    if st.button("➕ Ajouter", key="add_article", use_container_width=True):
        if code:
            state['articles'][code] = Article(code, name or "N/A", art_type, int(lead), float(cost))
            st.markdown('<div class="success-box">✅ Article ajouté!</div>', unsafe_allow_html=True)
            st.rerun()
    
    if state['articles']:
        st.markdown("### 📋 Liste Articles")
        st.dataframe(pd.DataFrame([vars(a) for a in state['articles'].values()]), use_container_width=True)

elif current_tab == 2:  # Stocks
    st.markdown("### 🏬 Gestion des Stocks")
    col1, col2, col3 = st.columns(3)
    with col1: article = st.text_input("📦 Article", key="stock_article")
    with col2: quantity = st.number_input("📈 Quantité", min_value=0.0, value=0.0, format="%.2f", key="stock_qty")
    with col3: safety_stock = st.number_input("🛡️ Stock sécurité", min_value=0.0, value=0.0, format="%.2f", key="stock_safety")
    
    if st.button("💾 METTRE À JOUR", key="update_stock", use_container_width=True):
        if article and article in state['articles']:
            state['stocks'][article] = Stock(article, float(quantity), float(safety_stock))
            st.markdown('<div class="success-box">✅ Stock mis à jour!</div>', unsafe_allow_html=True)
            st.rerun()
        elif article:
            st.markdown('<div class="error-box">❌ Article non trouvé!</div>', unsafe_allow_html=True)
    
    if state['stocks']:
        stock_df = pd.DataFrame([{
            'Article': s.article, 
            'Nom': state['articles'].get(s.article, type('obj', (), {'name': 'N/A'})).name,
            'Stock': s.qty, 'Sécurité': s.safety, 'Disponible': s.qty - s.safety,
            'Statut': '🟢 OK' if s.qty >= s.safety else '🔴 BAS'
        } for s in state['stocks'].values()])
        st.dataframe(stock_df, use_container_width=True)

elif current_tab == 3:  # Nomenclatures
    st.markdown("### 🧱 Nomenclatures")
    col1, col2 = st.columns(2)
    with col1: parent = st.text_input("👑 Parent", key="bom_parent")
    with col2: 
        component = st.text_input("🔧 Composant", key="bom_component")
        bom_qty = st.number_input("📊 Qté", value=1.0, key="bom_qty")
    
    if st.button("➕ BOM", key="add_bom", use_container_width=True):
        if parent and component:
            state['boms'].append(BOM(parent, component, float(bom_qty)))
            st.markdown('<div class="success-box">✅ BOM ajouté!</div>', unsafe_allow_html=True)
            st.rerun()
    
    if state['boms']:
        st.dataframe(pd.DataFrame([vars(b) for b in state['boms']]), use_container_width=True)

elif current_tab == 4:  # Demandes
    st.markdown("### 📈 Demandes Clients")
    col1, col2, col3, col4 = st.columns(4)
    with col1: client = st.text_input("👥 Client", key="demand_client")
    with col2: article = st.text_input("📦 Article", key="demand_article")
    with col3: demand_qty = st.number_input("📊 Qté", value=10.0, key="demand_qty")
    with col4: due = st.date_input("📅 Date", value=pd.Timestamp.now().date(), key="demand_date")
    
    if st.button("➕ Demande", key="add_demand", use_container_width=True):
        if client and article:
            state['demands'].append(Demand(client, article, float(demand_qty), due))
            st.markdown('<div class="success-box">✅ Demande ajoutée!</div>', unsafe_allow_html=True)
            st.rerun()
    
    if state['demands']:
        st.dataframe(pd.DataFrame([vars(d) | {'due_date': d.due_date.strftime('%Y-%m-%d')} for d in state['demands']]), use_container_width=True)

elif current_tab == 5:  # MRP
    st.markdown("### ⚡ Résultats MRP")
    if st.button("🧮 CALCULER MRP", key="calc_mrp", use_container_width=True):
        with st.spinner("Calcul MRP avec explosion BOM..."): calculate_mrp()
        st.success("✅ MRP calculé!")
        st.rerun()
    
    if not state['mrp_results'].empty:
        st.dataframe(state['mrp_results'], use_container_width=True)
        fig = px.bar(state['mrp_results'], x='Article', y='Besoin Net', color='Type')
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("⚠️ Ajoutez des données et calculez MRP!")

elif current_tab == 6:  # Export
    st.markdown("### 📊 Export Excel")
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        if state['articles']: pd.DataFrame([vars(a) for a in state['articles'].values()]).to_excel(writer, 'Articles', index=False)
        pd.DataFrame([vars(b) for b in state['boms']]).to_excel(writer, 'BOMs', index=False)
        if state['stocks']: pd.DataFrame([vars(s) for s in state['stocks'].values()]).to_excel(writer, 'Stocks', index=False)
        if state['demands']: pd.DataFrame([vars(d) | {'due_date': d.due_date.strftime('%Y-%m-%d')} for d in state['demands']]).to_excel(writer, 'Demandes', index=False)
        if not state['mrp_results'].empty: state['mrp_results'].to_excel(writer, 'MRP', index=False)
    
    st.download_button("📥 Télécharger Excel", output.getvalue(), f"MRP_v3.12_{date.today().strftime('%Y%m%d')}.xlsx", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", use_container_width=True)
