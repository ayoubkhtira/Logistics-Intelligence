import streamlit as st
from dataclasses import dataclass
import pandas as pd
import plotly.express as px
from datetime import date
import io
import openpyxl
import numpy as np


# Configuration
st.set_page_config(page_title="Calculateur Transport", page_icon="🚚", layout="wide")


# CSS Styling professionnel
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700&family=Inter:wght@300;400;500;600;700&display=swap');
* { font-family: 'Inter', sans-serif; }
body { background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 50%, #16213e 100%); color: #e2e8f0; }
h1, h2, h3 { color: #f8fafc !important; font-family: 'Orbitron', monospace !important; text-shadow: 0 2px 10px rgba(102,126,234,0.5); }
.main-header { padding: 3rem; background: linear-gradient(135deg, rgba(10,10,16,0.95), rgba(26,26,46,0.95)); backdrop-filter: blur(25px); border-radius: 24px; border-left: 8px solid #667eea; box-shadow: 0 30px 60px rgba(0,0,0,0.8); margin-bottom: 2rem; }
.header-title { font-size: 3.2rem; font-weight: 700; letter-spacing: 6px; text-transform: uppercase; background: linear-gradient(45deg, #667eea, #764ba2, #f093fb, #667eea); background-size: 400% 400%; -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent; animation: gradientMove 5s ease infinite; text-align: center; }

/* === ONGLETS PREMIUM - Style Box 3D === */
.stTabs {
    background: linear-gradient(145deg, rgba(15,15,35,0.9), rgba(26,26,46,0.9)) !important;
    backdrop-filter: blur(25px) !important;
    border-radius: 24px !important;
    border: 2px solid rgba(102,126,234,0.4) !important;
    box-shadow: 
        0 25px 50px rgba(0,0,0,0.6),
        inset 0 1px 0 rgba(255,255,255,0.1) !important;
    padding: 4px !important;
    margin: 1rem 0 !important;
    overflow: hidden !important;
}

.stTabs [data-baseweb="tab-list"] {
    gap: 4px !important;
    padding: 8px !important;
    border-radius: 20px !important;
    background: rgba(255,255,255,0.02) !important;
}

.stTabs [data-baseweb="tab"] {
    height: 60px !important;
    background: linear-gradient(145deg, rgba(102,126,234,0.08), rgba(118,75,162,0.08)) !important;
    backdrop-filter: blur(20px) !important;
    border: 2px solid rgba(102,126,234,0.2) !important;
    border-radius: 20px !important;
    padding: 0 24px !important;
    font-family: 'Orbitron', monospace !important;
    font-weight: 600 !important;
    font-size: 14px !important;
    color: #b8bed9 !important;
    text-transform: uppercase !important;
    letter-spacing: 1px !important;
    white-space: nowrap !important;
    transition: all 0.4s cubic-bezier(0.4,0,0.2,1) !important;
    position: relative !important;
    overflow: hidden !important;
}

.stTabs [data-baseweb="tab"]:hover {
    background: linear-gradient(145deg, rgba(102,126,234,0.2), rgba(118,75,162,0.2)) !important;
    border-color: rgba(102,126,234,0.5) !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 15px 30px rgba(102,126,234,0.3) !important;
    color: #e2e8f0 !important;
}

.stTabs [aria-selected="true"] {
    background: linear-gradient(145deg, rgba(102,126,234,0.3), rgba(118,75,162,0.3)) !important;
    border-color: #667eea !important;
    color: #ffffff !important;
    transform: translateY(-4px) !important;
    box-shadow: 
        0 20px 40px rgba(102,126,234,0.5),
        0 0 30px rgba(102,126,234,0.3),
        inset 0 1px 0 rgba(255,255,255,0.3) !important;
}
.stTabs [data-baseweb="tab-highlight"] {
    background: transparent !important;
    background-color: rgba(255,255,255,0) !important;
    border: none !important;
    box-shadow: none !important;
}
            
.stTabs [aria-selected="true"]::before {
    content: '' !important;
    position: absolute !important;
    top: 0 !important;
    left: -100% !important;
    width: 100% !important;
    height: 100% !important;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent) !important;
    transition: left 0.6s !important;
}

.stTabs [aria-selected="true"]:hover::before {
    left: 100% !important;
}

/* BOUTONS */
.stButton > button { 
    background: linear-gradient(135deg, rgba(102,126,234,0.15), rgba(118,75,162,0.15)) !important; 
    backdrop-filter: blur(20px) !important; 
    border: 2px solid rgba(102,126,234,0.4) !important; 
    border-radius: 20px !important; 
    padding: 0.8rem 1.5rem !important; 
    font-family: 'Orbitron', monospace !important; 
    font-weight: 600 !important; 
    color: #e2e8f0 !important; 
    text-transform: uppercase !important; 
    box-shadow: 0 10px 30px rgba(0,0,0,0.3) !important; 
    transition: all 0.4s cubic-bezier(0.4,0,0.2,1) !important; 
}
.stButton > button:hover {
    background: linear-gradient(135deg, rgba(102,126,234,0.25), rgba(118,75,162,0.25)) !important;
    box-shadow: 0 15px 35px rgba(102,126,234,0.4) !important;
    transform: translateY(-2px) !important;
}

/* CARTES METRIC */
.metric-card { 
    background: linear-gradient(145deg, rgba(102,126,234,0.2), rgba(118,75,162,0.2)) !important; 
    backdrop-filter: blur(20px); 
    color: white !important; 
    padding: 2.5rem !important; 
    border-radius: 24px !important; 
    text-align: center !important; 
    border: 2px solid rgba(255,255,255,0.2) !important; 
    box-shadow: 0 25px 50px rgba(102,126,234,0.4) !important; 
}
.metric-value { font-size: 2.5rem !important; font-weight: 700 !important; color: #667eea !important; }
.metric-label { font-size: 1rem !important; opacity: 0.9 !important; margin-top: 0.5rem !important; }

/* SECTIONS INPUT */
.input-section { 
    background: rgba(255,255,255,0.05); 
    padding: 2rem; 
    border-radius: 20px; 
    border: 1px solid rgba(102,126,234,0.3); 
    margin: 1rem 0; 
}

/* EDIT ROW */
.edit-row { 
    background: linear-gradient(135deg, rgba(102,126,234,0.1), rgba(118,75,162,0.1)) !important; 
    border-left: 4px solid #667eea !important; 
}

/* ANIMATIONS */
@keyframes gradientMove { 
    0%,100%{background-position:0% 50%} 
    50%{background-position:100% 50%} 
}

/* RESPONSIVE */
@media (max-width: 768px) {
    .stTabs [data-baseweb="tab"] {
        height: 50px !important;
        padding: 0 16px !important;
        font-size: 12px !important;
    }
    .header-title { font-size: 2.2rem !important; }
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
    * { font-family: 'Inter', sans-serif !important; }
    body { 
        margin: 0; 
        padding: 0; 
        background: transparent; 
        overflow: hidden; 
    }
    .main-header {
        position: relative; 
        padding: 2.5rem; 
        background: linear-gradient(135deg, rgba(10,10,16,0.95), rgba(26,26,46,0.95)) !important; 
        backdrop-filter: blur(25px) !important;
        border-radius: 24px !important;
        border-left: 12px solid #667eea !important; 
        overflow: hidden; 
        box-shadow: 0 30px 60px rgba(0,0,0,0.8) !important;
        min-height: 160px; 
        display: flex; 
        flex-direction: column; 
        justify-content: center;
        margin-bottom: 2rem !important;
    }
    #bg-carousel {
        position: absolute; 
        top: 0; 
        left: 0; 
        width: 100%; 
        height: 100%;
        background-size: cover !important; 
        background-position: center !important; 
        opacity: 0.15 !important; 
        transition: background-image 2s ease-in-out !important; 
        z-index: 0;
    }
    .overlay {
        position: absolute; 
        top: 0; 
        left: 0; 
        width: 100%; 
        height: 100%;
        background: linear-gradient(rgba(102,126,234,0.1) 0%, rgba(26,26,46,0.8) 100%) !important;
        z-index: 1; 
        pointer-events: none;
    }
    .content { 
        position: relative; 
        z-index: 2; 
        text-align: center;
    }
    .header-title { 
        font-family: 'Orbitron', monospace !important; 
        text-transform: uppercase; 
        letter-spacing: 6px; 
        font-size: 3.2rem !important; 
        font-weight: 700 !important;
        margin: 0; 
        background: linear-gradient(45deg, #667eea, #764ba2, #f093fb, #667eea) !important;
        background-size: 400% 400% !important;
        -webkit-background-clip: text !important;
        background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        animation: gradientMove 5s ease infinite !important;
        text-shadow: 0 2px 10px rgba(102,126,234,0.5) !important;
    }
    .status { 
        color: #667eea !important; 
        font-weight: 600 !important; 
        letter-spacing: 3px !important; 
        font-size: 1rem !important; 
        text-transform: uppercase !important; 
        margin-top: 12px !important;
        font-family: 'Orbitron', monospace !important;
    }
    @keyframes gradientMove { 
        0%,100%{background-position:0% 50%} 
        50%{background-position:100% 50%} 
    }
    @keyframes blink { 
        0% { opacity: 1; } 
        50% { opacity: 0.3; } 
        100% { opacity: 1; } 
    }
    .active-dot { 
        display: inline-block; 
        width: 14px; 
        height: 14px; 
        background: #667eea !important; 
        border-radius: 50%; 
        margin-left: 12px; 
        animation: blink 2s infinite !important; 
        box-shadow: 0 0 12px #667eea !important;
    }
</style>
</head>
<body>
    <div class="main-header">
        <div id="bg-carousel"></div>
        <div class="overlay"></div>
        <div class="content">
            <h1>CALCULATOR TRANSPORT<span style="color:#FF0000;"></span></h1>
            <div class="status">Logistics Intelligence <span class="active-dot"></span></div>
        </div>
    </div>
    <script>
        const images = [
            "https://images.unsplash.com/photo-1436491865332-7a61a109cc05?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80",
            "https://images.unsplash.com/photo-1567808291548-fc3ee04dbcf0?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80", 
            "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80",
            "https://images.unsplash.com/photo-1581092160607-a458d3227616?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80",
            "https://images.unsplash.com/photo-1571164324422-6d668a8b4132?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80"
        ];
        let index = 0;
        const bgDiv = document.getElementById('bg-carousel');
        function changeBackground() {
            bgDiv.style.backgroundImage = `url(${images[index]})`;
            index = (index + 1) % images.length;
        }
        changeBackground();
        setInterval(changeBackground, 4000);
    </script>
</body>
</html>
"""

st.markdown(header_code, unsafe_allow_html=True)




# Initialisation Session State
if 'config' not in st.session_state:
    st.session_state.config = {
        "devise_base": "MAD",
        "taux_change": {"MAD": 1.0, "CHF": 9.6, "EUR": 10.8, "USD": 10.2},
        "villes_depart": ["Casablanca", "Tanger", "Agadir"],
        "villes_arrivee": ["Anvers", "Marseille", "Genève"],
        "routes": {
            "Casablanca-Anvers": {
                "FraisMaroc": {"Préacheminement": 5000.0, "Frais transitaire": 5000.0, "Somme administrations": 1800.0, "Passage portuaire départ": 1700.0, "Acconage": 2500.0},
                "FraisArrivee": {"Débarquement": 500.0, "Passage portuaire arrivée": 250.0, "Post-acheminement": 800.0},
                "FretMaritime": {"Fret": 80.0, "BAF": 0.05, "CAF": -0.01, "Rabais": 0.005, "Remise": 0.01, "Ristourne": 0.015},
                "FretRoutier": {"Fret": 160.0, "CAF": 0.03, "Rabais": 0.0, "Remise": 0.01, "Ristourne": 0.015, "Assurance": 0.01},
                "FraisPersonnalises": {},
                "devise": "CHF"
            }
        },
        "Taxes": {"DroitsDouane": 0.40, "TVA": 0.20}
    }
    st.session_state.shipment = {"nb_up": 1.0, "nb_palettes": 1.0, "nb_conteneurs": 0.0, "valeur_cip": 1000.0, "route": "Casablanca-Anvers"}
    st.session_state.history = []
    st.session_state.results = None


if 'active_tab' not in st.session_state:
    st.session_state.active_tab = 0



def convert_to_base(amount, source_devise, config):
    return amount * config["taux_change"][source_devise] / config["taux_change"][config["devise_base"]]


def calculate_all_costs(config, shipment):
    results = {}
    route_data = config["routes"][shipment["route"]]
    devise_route = route_data["devise"]
    
    # Frais fixes
    total_frais_depart = sum(route_data["FraisMaroc"].values())
    total_frais_arrivee = sum(route_data["FraisArrivee"].values())
    results["Frais Départ"] = convert_to_base(total_frais_depart, "MAD", config)
    results["Frais Arrivée"] = convert_to_base(total_frais_arrivee, devise_route, config)
    
    # Frets
    fret_data = route_data["FretMaritime"]
    fret_final = shipment["nb_up"] * fret_data["Fret"] * (1 + fret_data["BAF"] + fret_data["CAF"] - fret_data["Rabais"] - fret_data["Remise"] - fret_data["Ristourne"])
    results["Fret Maritime"] = convert_to_base(fret_final, devise_route, config)
    
    routier_data = route_data["FretRoutier"]
    routier_final = shipment["nb_up"] * routier_data["Fret"] * (1 + routier_data["CAF"] - routier_data["Rabais"] - routier_data["Remise"] - routier_data["Ristourne"]) + shipment["valeur_cip"] * routier_data["Assurance"]
    results["Fret Routier"] = convert_to_base(routier_final, devise_route, config)
    
    # Frais personnalisés
    total_personnalise = 0
    for nom, data in route_data["FraisPersonnalises"].items():
        unite = data["unite"]
        montant_base = data["montant"]
        
        if unite == "palette":
            montant = montant_base * shipment["nb_palettes"]
        elif unite == "conteneur":
            montant = montant_base * shipment["nb_conteneurs"]
        elif unite == "general":
            montant = montant_base
        else:  # UP
            montant = montant_base * shipment["nb_up"]
        
        if data.get("pourcentage_cip", 0) > 0:
            montant += shipment["valeur_cip"] * data["pourcentage_cip"]
        
        total_personnalise += montant
        results[f"Frais Perso: {nom}"] = convert_to_base(montant, data["devise"], config)
    
    results["Total Frais Personnalisés"] = convert_to_base(total_personnalise, devise_route, config)
    
    # Taxes
    total_transport = sum([v for k, v in results.items() if "Taxe" not in k and "TOTAL" not in k])
    cip_base = convert_to_base(shipment["valeur_cip"], devise_route, config)
    results["Droits Douane"] = cip_base * config["Taxes"]["DroitsDouane"]
    results["TVA"] = (cip_base + results["Droits Douane"]) * config["Taxes"]["TVA"]
    results["GRAND TOTAL"] = total_transport + results["Droits Douane"] + results["TVA"]
    
    return results


# Interface 7 onglets ✅ AUCUN KEY SUR METRIC
tabs = st.tabs([
    "📦 Calcul", "🗺️ Routes", "💰 Frais Perso", "💱 Devises", "⚙️ Taxes", "📊 Résultats", "📋 Légende"
])
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = tabs

# Active l'onglet selon session_state
if 'active_tab' in st.session_state:
    try:
        tabs[st.session_state.active_tab].display()
    except:
        pass  # Ignore si erreur




with tab1:
    st.markdown("### 🚀 **Calcul Express**")
    col1, col2 = st.columns(2)
    with col1:
        st.session_state.shipment["nb_up"] = st.number_input("**UP**", value=1.0, min_value=0.0, step=0.1, format="%.1f", key="input_up")
        st.session_state.shipment["nb_palettes"] = st.number_input("**Palettes**", value=1.0, min_value=0.0, step=1.0, format="%.0f", key="input_palettes")
        st.session_state.shipment["nb_conteneurs"] = st.number_input("**Conteneurs**", value=0.0, min_value=0.0, step=1.0, format="%.0f", key="input_conteneurs")
    with col2:
        st.session_state.shipment["valeur_cip"] = st.number_input("**Valeur CIP**", value=1000.0, min_value=0.0, step=100.0, format="%.0f", key="input_cip")
        st.session_state.shipment["route"] = st.selectbox("**Route**", list(st.session_state.config["routes"].keys()), key="select_route_calc")
    
    if st.button("🧮 **CALCULER TOUT**", use_container_width=True):
        st.session_state.results = calculate_all_costs(st.session_state.config, st.session_state.shipment)
        st.session_state.history.append({
            "date": date.today().strftime("%Y-%m-%d %H:%M"), 
            "route": st.session_state.shipment["route"], 
            "total": st.session_state.results["GRAND TOTAL"]
        })
        st.session_state.active_tab = 5  # 📊 Résultats = index 5 (0,1,2,3,4,5,6)
        st.rerun()


with tab2:
    st.markdown("### 🗺️ **Routes**")
    col1, col2 = st.columns(2)
    with col1:
        new_depart = st.text_input("**Ville départ**", key="input_ville_depart")
        if st.button("➕ Départ", key="btn_add_depart") and new_depart:
            if new_depart not in st.session_state.config["villes_depart"]:
                st.session_state.config["villes_depart"].append(new_depart)
                st.success(f"✅ {new_depart} ajoutée!")
                st.rerun()
    with col2:
        new_arrivee = st.text_input("**Ville arrivée**", key="input_ville_arrivee")
        if st.button("➕ Arrivée", key="btn_add_arrivee") and new_arrivee:
            if new_arrivee not in st.session_state.config["villes_arrivee"]:
                st.session_state.config["villes_arrivee"].append(new_arrivee)
                st.success(f"✅ {new_arrivee} ajoutée!")
                st.rerun()
    
    ville_d = st.selectbox("Départ", st.session_state.config["villes_depart"], key="select_ville_d")
    ville_a = st.selectbox("Arrivée", st.session_state.config["villes_arrivee"], key="select_ville_a")
    if st.button(f"✨ **Créer {ville_d}-{ville_a}**", key="btn_create_route"):
        route_key = f"{ville_d}-{ville_a}"
        if route_key not in st.session_state.config["routes"]:
            default = list(st.session_state.config["routes"].values())[0]
            st.session_state.config["routes"][route_key] = {
                "FraisMaroc": default["FraisMaroc"].copy(),
                "FraisArrivee": default["FraisArrivee"].copy(),
                "FretMaritime": default["FretMaritime"].copy(),
                "FretRoutier": default["FretRoutier"].copy(),
                "FraisPersonnalises": {},
                "devise": "CHF"
            }
            st.success(f"✅ **{route_key}** créée!")
            st.rerun()


with tab3:
    st.markdown("### 💰 **Frais Personnalisés** ⭐")
    route = st.selectbox("**Route**", list(st.session_state.config["routes"].keys()), key="select_route_frais")
    frais_data = st.session_state.config["routes"][route]["FraisPersonnalises"]
    
    col1, col2, col3, col4 = st.columns(4)
    with col1: nom = st.text_input("**Nom**", key=f"input_nom_{route}")
    with col2: montant = st.number_input("**Montant**", value=0.0, step=10.0, key=f"input_mont_{route}")
    with col3: 
        devise = st.selectbox("**Devise**", list(st.session_state.config["taux_change"].keys()), key=f"select_devise_{route}")
        unite = st.selectbox("**Unité**", ["UP", "palette", "conteneur", "general"], key=f"select_unite_{route}")
    with col4: pct_cip = st.number_input("**% CIP**", value=0.0, step=0.01, format="%.2f", key=f"input_pct_{route}")
    
    if st.button("➕ **AJOUTER**", use_container_width=True, key=f"btn_ajout_frais_{route}") and nom:
        frais_data[nom] = {
            "montant": float(montant), 
            "devise": devise, 
            "unite": unite,
            "pourcentage_cip": float(pct_cip)
        }
        st.success(f"✅ **{nom}** ({unite}) ajouté!")
        st.rerun()
    
    if frais_data:
        st.markdown("### 📋 **Frais de cette route**")
        df_frais = pd.DataFrame([{
            "Nom": k, "Montant": f"{v['montant']:.0f}", "Unité": v["unite"],
            "Devise": v["devise"], "%CIP": f"{v['pourcentage_cip']*100:.1f}%"
        } for k, v in frais_data.items()])
        st.dataframe(df_frais, use_container_width=True)
        
        suppr = st.multiselect("🗑️ Supprimer", list(frais_data.keys()), key=f"multiselect_suppr_{route}")
        if st.button("Supprimer", key=f"btn_suppr_{route}") and suppr:
            for f in suppr: del frais_data[f]
            st.rerun()


with tab4:
    st.markdown("### 💱 **Devises**")
    st.session_state.config["devise_base"] = st.selectbox("**Devise Base**", ["MAD", "CHF", "EUR", "USD"], key="select_devise_base")
    
    new_devise = st.text_input("**Nouvelle devise**", key="input_new_devise")
    if st.button("➕ Ajouter", key="btn_add_devise") and new_devise:
        st.session_state.config["taux_change"][new_devise] = 1.0
        st.rerun()
    
    taux_df = pd.DataFrame([{"Devise": k, "Taux": v} for k, v in st.session_state.config["taux_change"].items()])
    edited = st.data_editor(taux_df, num_rows="dynamic", use_container_width=True, key="editor_taux")
    for idx, row in edited.iterrows():
        st.session_state.config["taux_change"][row["Devise"]] = float(row["Taux"])



with tab5:
    st.markdown("### ⚙️ **Taxes**")
    col1, col2 = st.columns(2)
    with col1:
        dd = st.number_input("**Douane %**", value=st.session_state.config["Taxes"]["DroitsDouane"]*100, step=1.0, key="input_douane")
        st.session_state.config["Taxes"]["DroitsDouane"] = dd/100
    with col2:
        tva = st.number_input("**TVA %**", value=st.session_state.config["Taxes"]["TVA"]*100, step=1.0, key="input_tva")
        st.session_state.config["Taxes"]["TVA"] = tva/100


with tab6:
    if st.session_state.results:
        st.markdown("### 💎 **RÉSULTATS**")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.markdown(f'<div class="metric-card"><div class="metric-value">{st.session_state.shipment["nb_up"]:.1f}</div><div class="metric-label">📦 UP</div></div>', unsafe_allow_html=True)
        with col2:
            st.markdown(f'<div class="metric-card"><div class="metric-value">{st.session_state.shipment["nb_palettes"]:.0f}</div><div class="metric-label">📋 Palettes</div></div>', unsafe_allow_html=True)
        with col3:
            st.markdown(f'<div class="metric-card"><div class="metric-value">{st.session_state.shipment["nb_conteneurs"]:.0f}</div><div class="metric-label">📦 Conteneurs</div></div>', unsafe_allow_html=True)
        with col4:
            st.markdown(f'<div class="metric-card"><div class="metric-value">{st.session_state.results["GRAND TOTAL"]:,.0f}</div><div class="metric-label">💎 TOTAL {st.session_state.config["devise_base"]}</div></div>', unsafe_allow_html=True)
        
        # ========================================
        # 🔧 ÉDITEUR COMPLET DES RÉSULTATS ✅ CORRIGÉ
        # ========================================
        st.markdown("### 🔧 **Éditeur Complet - Modifier Tous les Frais**")
        
        # Récupérer la route actuelle
        route_actuelle = st.session_state.shipment["route"]
        route_data = st.session_state.config["routes"][route_actuelle]
        
        # Préparer les données pour l'éditeur principal (✅ SANS lambda function)
        data_editor = []
        for categorie, montant in st.session_state.results.items():
            if "Frais Perso:" in categorie:
                continue
            elif categorie in ["Total Frais Personnalisés", "Droits Douane", "TVA", "GRAND TOTAL"]:
                data_editor.append({"Catégorie": categorie, "Montant": float(montant), "Editable": "❌ Non"})
            else:
                data_editor.append({"Catégorie": categorie, "Montant": float(montant), "Editable": "✅ Oui"})
        
        df_main = pd.DataFrame(data_editor)
        
        col_main1, col_main2 = st.columns([3, 1])
        with col_main1:
            # ✅ CORRIGÉ : column_config simplifié SANS lambda
            edited_main = st.data_editor(
                df_main,
                column_config={
                    "Montant": st.column_config.NumberColumn(format="%.0f")
                },
                use_container_width=True,
                hide_index=False,
                key="editor_resultats_main"
            )
        
        with col_main2:
            st.markdown("### **Actions Principales**")
            if st.button("💾 **Sauvegarder Frais Fixes**", key="btn_save_frais_fixes"):
                for idx, row in edited_main.iterrows():
                    categorie = row["Catégorie"]
                    nouveau_montant = float(row["Montant"])
                    
                    # Ne modifier que les lignes éditables
                    if row["Editable"] == "✅ Oui":
                        if categorie == "Frais Départ":
                            total_actuel = sum(route_data["FraisMaroc"].values())
                            if total_actuel > 0:
                                ratio = nouveau_montant / total_actuel
                                for k, v in route_data["FraisMaroc"].items():
                                    route_data["FraisMaroc"][k] = v * ratio
                        
                        elif categorie == "Frais Arrivée":
                            total_actuel = sum(route_data["FraisArrivee"].values())
                            if total_actuel > 0:
                                ratio = nouveau_montant / total_actuel
                                for k, v in route_data["FraisArrivee"].items():
                                    route_data["FraisArrivee"][k] = v * ratio
                        
                        elif categorie == "Fret Maritime":
                            if st.session_state.shipment["nb_up"] > 0:
                                route_data["FretMaritime"]["Fret"] = nouveau_montant / st.session_state.shipment["nb_up"]
                        
                        elif categorie == "Fret Routier":
                            if st.session_state.shipment["nb_up"] > 0:
                                route_data["FretRoutier"]["Fret"] = (nouveau_montant / st.session_state.shipment["nb_up"]) * 0.95
                
                # Recalculer TOUS les résultats
                st.session_state.results = calculate_all_costs(st.session_state.config, st.session_state.shipment)
                st.success("✅ Frais fixes mis à jour & recalculés!")
                st.rerun()
        
        # Section Frais Personnalisés
        frais_perso = route_data["FraisPersonnalises"]
        if frais_perso:
            st.markdown("---")
            st.markdown("### ✨ **Frais Personnalisés**")
            
            frais_list = []
            for nom, data in frais_perso.items():
                frais_list.append({
                    "Nom": nom,
                    "Montant": float(data["montant"]),
                    "Devise": data["devise"],
                    "Unité": data["unite"],
                    "Pourcentage CIP": float(data.get("pourcentage_cip", 0)) * 100
                })
            
            df_frais = pd.DataFrame(frais_list)
            col_frais1, col_frais2 = st.columns([3, 1])
            
            with col_frais1:
                edited_frais = st.data_editor(
                    df_frais,
                    column_config={
                        "Montant": st.column_config.NumberColumn(format="%.2f"),
                        "Pourcentage CIP": st.column_config.NumberColumn(format="%.2f")
                    },
                    use_container_width=True,
                    key=f"editor_frais_resultats_{route_actuelle}"
                )
            
            with col_frais2:
                if st.button("💾 **Sauvegarder Perso**", key=f"btn_save_perso_res_{route_actuelle}"):
                    for idx, row in edited_frais.iterrows():
                        nom = row["Nom"]
                        frais_perso[nom] = {
                            "montant": float(row["Montant"]),
                            "devise": row["Devise"],
                            "unite": row["Unité"],
                            "pourcentage_cip": float(row["Pourcentage CIP"]) / 100
                        }
                    st.session_state.results = calculate_all_costs(st.session_state.config, st.session_state.shipment)
                    st.success("✅ Frais personnalisés sauvegardés!")
                    st.rerun()
                
                suppr_frais = st.multiselect("🗑️ Supprimer", [row["Nom"] for _, row in edited_frais.iterrows()], key=f"suppr_perso_res_{route_actuelle}")
                if st.button("🗑️ **Supprimer**", key=f"btn_del_perso_res_{route_actuelle}") and suppr_frais:
                    for nom in suppr_frais:
                        del frais_perso[nom]
                    st.session_state.results = calculate_all_costs(st.session_state.config, st.session_state.shipment)
                    st.success(f"✅ {len(suppr_frais)} supprimés!")
                    st.rerun()
        
        # Affichage final du tableau récapitulatif
        st.markdown("---")
        st.markdown("### 📊 **Récapitulatif Final**")
        df_final = pd.DataFrame([
            [k, f"{v:,.0f}", st.session_state.config['devise_base']] 
            for k, v in st.session_state.results.items()
        ], columns=["**Catégorie**", "**Montant**", "Devise"])
        st.dataframe(df_final, use_container_width=True)
        
        # Graphique et export
        fig = px.pie(values=list(st.session_state.results.values()), names=list(st.session_state.results.keys()), hole=0.4)
        st.plotly_chart(fig, use_container_width=True)
        
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            pd.DataFrame(st.session_state.results.items(), columns=["Catégorie", "Montant"]).to_excel(writer, 'Resultats')
            pd.DataFrame([st.session_state.shipment]).to_excel(writer, 'Envoi')
            pd.DataFrame(st.session_state.history).to_excel(writer, 'Historique')
        st.download_button("📥 **EXCEL COMPLET**", output.getvalue(), f"Transport_v4.2_{date.today().strftime('%Y%m%d')}.xlsx")
    st.markdown('</div>', unsafe_allow_html=True)


with tab7:
    st.markdown("### 📋 **LÉGENDE & AIDE**")
    st.markdown("""
    **🎯 Unités de frais personnalisés :**
    
    | **Unité** | **× Quantité** | **Exemple** |
    |-----------|----------------|-------------|
    | **UP** | Nb UP | 50 MAD × 10 UP = 500 MAD |
    | **palette** | Nb Palettes | 100 MAD × 5 = 500 MAD |
    | **conteneur** | Nb Conteneurs | 5000 MAD × 1 = 5000 MAD |
    | **general** | 1 (fixe) | 2000 MAD fixe |
    
    **💰 % CIP =** Pourcentage de la **Valeur CIP** saisie
    **Ex:** 10 000 MAD CIP × 1.5% = 150 MAD ajouté
    """)

    if st.button("🔄 **RESET COMPLET**"):
        st.session_state.config = {}
        st.session_state.shipment = {}
        st.session_state.results = None
        st.rerun()

# 🔥 FEEDBACK TELEGRAM - LONGUEUR IDENTIQUE
st.markdown("---")

st.markdown('<div class="input-section" style="padding: 2rem; margin: 1rem 0;">', unsafe_allow_html=True)

st.markdown("""
<h3 style="text-align: center; margin-bottom: 2rem; color: #667eea;">
    💬 **Votre Avis Nous Intéresse**
</h3>
""", unsafe_allow_html=True)

TOKEN = st.secrets.get("TELEGRAM_TOKEN", "TON_TOKEN_BOT_TELEGRAM") 
CHAT_ID = st.secrets.get("TELEGRAM_CHAT_ID", "")


with st.form("feedback_form", clear_on_submit=True):
    # ✅ BOX 100% LARGEUR - MÊME LONGUEUR
    name = st.text_input("👤 **Nom / Entreprise**", 
                        placeholder="Votre nom",
                        help="Optionnel",
                        label_visibility="collapsed")
    
    # ✅ BOX 100% LARGEUR - MÊME LONGUEUR  
    msg = st.text_area("✍️ **Votre commentaire ou suggestion**", 
                      placeholder="Votre commentaire ou suggestion",
                      height=100,
                      label_visibility="collapsed")
    
    # ✅ BOUTON 100% LARGEUR
    submitted = st.form_submit_button("🚀 **ENVOYER L'AVIS**", use_container_width=True)

if submitted and msg.strip():
    try:
        import requests
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        text = f"🚀 *CALCUL TRANSPORT*\n\n👤 *{name or 'Anonyme'}*\n💬 *{msg}*\n📅 {date.today().strftime('%d/%m/%Y %H:%M')}"
        response = requests.post(url, json={
            "chat_id": CHAT_ID, 
            "text": text, 
            "parse_mode": "Markdown"
        })
        
        if response.status_code == 200:
            st.success("✅ **Merci infiniment pour votre retour !** 🎉")
            
        else:
            st.error("❌ **Erreur envoi Telegram**")
    except:
        st.error("❌ **Erreur réseau**")
elif submitted:
    st.warning("⚠️ **Le commentaire ne peut pas être vide**")

st.markdown('</div>', unsafe_allow_html=True)
st.markdown("---")
st.caption("Calculateur Transport - Made with ❤️")
