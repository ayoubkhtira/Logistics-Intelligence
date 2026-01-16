import streamlit as st
from dataclasses import dataclass
import pandas as pd
import plotly.express as px
from datetime import date
import io
import openpyxl
import numpy as np
import base64


# Configuration sans sidebar
st.set_page_config(
    page_title="Calculateur Transport", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Fonction pour encoder l'image en base64
@st.cache_data
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# CSS Styling professionnel avec background image
def set_background_image(image_path):
    # Encoder l'image
    image_base64 = get_base64_of_bin_file(image_path)
    
    css = f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700&family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Background avec image */
    .stApp {{
        background: linear-gradient(rgba(15, 15, 35, 0.85), rgba(26, 26, 46, 0.85)), 
                    url("data:image/jpg;base64,{image_base64}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        background-repeat: no-repeat;
        min-height: 100vh;
    }}
    
    /* Cacher la sidebar */
    section[data-testid="stSidebar"] {{
        display: none;
    }}
    
    header[data-testid="stHeader"] {{
        display: none;
    }}
    
    /* Styles pour le contenu */
    * {{ font-family: 'Inter', sans-serif; }}
    h1, h2, h3 {{ 
        color: #f8fafc !important; 
        font-family: 'Orbitron', monospace !important; 
        text-shadow: 0 2px 10px rgba(102,126,234,0.5); 
    }}
    
    .main-header {{ 
        padding: 3rem; 
        background: linear-gradient(135deg, rgba(10,10,16,0.85), rgba(26,26,46,0.85)) !important; 
        backdrop-filter: blur(25px); 
        border-radius: 24px; 
        border-left: 8px solid #667eea; 
        box-shadow: 0 30px 60px rgba(0,0,0,0.8); 
        margin-bottom: 2rem; 
    }}
    
    .header-title {{ 
        font-size: 3.2rem; 
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
    }}
    
    /* === ONGLETS PREMIUM - Style Box 3D === */
    .stTabs {{
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
    }}
    
    .stTabs [data-baseweb="tab-list"] {{
        gap: 4px !important;
        padding: 8px !important;
        border-radius: 20px !important;
        background: rgba(255,255,255,0.02) !important;
    }}
    
    .stTabs [data-baseweb="tab"] {{
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
    }}
    
    .stTabs [data-baseweb="tab"]:hover {{
        background: linear-gradient(145deg, rgba(102,126,234,0.2), rgba(118,75,162,0.2)) !important;
        border-color: rgba(102,126,234,0.5) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 15px 30px rgba(102,126,234,0.3) !important;
        color: #e2e8f0 !important;
    }}
    
    .stTabs [aria-selected="true"] {{
        background: linear-gradient(145deg, rgba(102,126,234,0.3), rgba(118,75,162,0.3)) !important;
        border-color: #667eea !important;
        color: #ffffff !important;
        transform: translateY(-4px) !important;
        box-shadow: 
            0 20px 40px rgba(102,126,234,0.5),
            0 0 30px rgba(102,126,234,0.3),
            inset 0 1px 0 rgba(255,255,255,0.3) !important;
    }}
    
    .stTabs [data-baseweb="tab-highlight"] {{
        background: transparent !important;
        background-color: rgba(255,255,255,0) !important;
        border: none !important;
        box-shadow: none !important;
    }}
                
    .stTabs [aria-selected="true"]::before {{
        content: '' !important;
        position: absolute !important;
        top: 0 !important;
        left: -100% !important;
        width: 100% !important;
        height: 100% !important;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent) !important;
        transition: left 0.6s !important;
    }}
    
    .stTabs [aria-selected="true"]:hover::before {{
        left: 100% !important;
    }}
    
    /* BOUTONS */
    .stButton > button {{ 
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
    }}
    
    .stButton > button:hover {{
        background: linear-gradient(135deg, rgba(102,126,234,0.25), rgba(118,75,162,0.25)) !important;
        box-shadow: 0 15px 35px rgba(102,126,234,0.4) !important;
        transform: translateY(-2px) !important;
    }}
    
    /* CARTES METRIC */
    .metric-card {{ 
        background: linear-gradient(145deg, rgba(102,126,234,0.2), rgba(118,75,162,0.2)) !important; 
        backdrop-filter: blur(20px); 
        color: white !important; 
        padding: 2.5rem !important; 
        border-radius: 24px !important; 
        text-align: center !important; 
        border: 2px solid rgba(255,255,255,0.2) !important; 
        box-shadow: 0 25px 50px rgba(102,126,234,0.4) !important; 
    }}
    
    .metric-value {{ font-size: 2.5rem !important; font-weight: 700 !important; color: #667eea !important; }}
    .metric-label {{ font-size: 1rem !important; opacity: 0.9 !important; margin-top: 0.5rem !important; }}
    
    /* SECTIONS INPUT */
    .input-section {{ 
        background: rgba(255,255,255,0.05); 
        padding: 2rem; 
        border-radius: 20px; 
        border: 1px solid rgba(102,126,234,0.3); 
        margin: 1rem 0; 
    }}
    
    /* EDIT ROW */
    .edit-row {{ 
        background: linear-gradient(135deg, rgba(102,126,234,0.1), rgba(118,75,162,0.1)) !important; 
        border-left: 4px solid #667eea !important; 
    }}
    
    /* ANIMATIONS */
    @keyframes gradientMove {{ 
        0%,100%{{background-position:0% 50%}} 
        50%{{background-position:100% 50%}} 
    }}
    
    /* RESPONSIVE */
    @media (max-width: 768px) {{
        .stTabs [data-baseweb="tab"] {{
            height: 50px !important;
            padding: 0 16px !important;
            font-size: 12px !important;
        }}
        .header-title {{ font-size: 2.2rem !important; }}
    }}
    </style>
    """
    return css

# Appliquer le CSS avec l'image de fond
try:
    st.markdown(set_background_image("images/img1.jpg"), unsafe_allow_html=True)
except FileNotFoundError:
    # Fallback si l'image n'est pas trouvée
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 50%, #16213e 100%) !important;
    }
    </style>
    """, unsafe_allow_html=True)
    st.warning("Image de fond non trouvée. Utilisation du fond par défaut.")

# Header simplifié sans carrousel
header_code = """
<div class="main-header">
    <div class="content">
        <h1 class="header-title">CALCULATOR TRANSPORT</h1>
        <div class="status">Logistics Intelligence</div>
    </div>
</div>
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

# Interface 7 onglets sans emojis
tabs = st.tabs([
    "Calcul", "Routes", "Frais Perso", "Devises", "Taxes", "Resultats", "Legende"
])
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = tabs

# Active l'onglet selon session_state
if 'active_tab' in st.session_state:
    try:
        tabs[st.session_state.active_tab].display()
    except:
        pass  # Ignore si erreur

with tab1:
    st.markdown("### **Calcul Express**")
    col1, col2 = st.columns(2)
    with col1:
        st.session_state.shipment["nb_up"] = st.number_input("**UP**", value=1.0, min_value=0.0, step=0.1, format="%.1f", key="input_up")
        st.session_state.shipment["nb_palettes"] = st.number_input("**Palettes**", value=1.0, min_value=0.0, step=1.0, format="%.0f", key="input_palettes")
        st.session_state.shipment["nb_conteneurs"] = st.number_input("**Conteneurs**", value=0.0, min_value=0.0, step=1.0, format="%.0f", key="input_conteneurs")
    with col2:
        st.session_state.shipment["valeur_cip"] = st.number_input("**Valeur CIP**", value=1000.0, min_value=0.0, step=100.0, format="%.0f", key="input_cip")
        st.session_state.shipment["route"] = st.selectbox("**Route**", list(st.session_state.config["routes"].keys()), key="select_route_calc")
    
    if st.button("**CALCULER TOUT**", use_container_width=True):
        st.session_state.results = calculate_all_costs(st.session_state.config, st.session_state.shipment)
        st.session_state.history.append({
            "date": date.today().strftime("%Y-%m-%d %H:%M"), 
            "route": st.session_state.shipment["route"], 
            "total": st.session_state.results["GRAND TOTAL"]
        })
        st.session_state.active_tab = 5  # Resultats = index 5 (0,1,2,3,4,5,6)
        st.rerun()

with tab2:
    st.markdown("### **Routes**")
    col1, col2 = st.columns(2)
    with col1:
        new_depart = st.text_input("**Ville depart**", key="input_ville_depart")
        if st.button("Ajouter Depart", key="btn_add_depart") and new_depart:
            if new_depart not in st.session_state.config["villes_depart"]:
                st.session_state.config["villes_depart"].append(new_depart)
                st.success(f"{new_depart} ajoutee!")
                st.rerun()
    with col2:
        new_arrivee = st.text_input("**Ville arrivee**", key="input_ville_arrivee")
        if st.button("Ajouter Arrivee", key="btn_add_arrivee") and new_arrivee:
            if new_arrivee not in st.session_state.config["villes_arrivee"]:
                st.session_state.config["villes_arrivee"].append(new_arrivee)
                st.success(f"{new_arrivee} ajoutee!")
                st.rerun()
    
    ville_d = st.selectbox("Depart", st.session_state.config["villes_depart"], key="select_ville_d")
    ville_a = st.selectbox("Arrivee", st.session_state.config["villes_arrivee"], key="select_ville_a")
    if st.button(f"**Creer {ville_d}-{ville_a}**", key="btn_create_route"):
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
            st.success(f"**{route_key}** creee!")
            st.rerun()

with tab3:
    st.markdown("### **Frais Personnalises**")
    route = st.selectbox("**Route**", list(st.session_state.config["routes"].keys()), key="select_route_frais")
    frais_data = st.session_state.config["routes"][route]["FraisPersonnalises"]
    
    col1, col2, col3, col4 = st.columns(4)
    with col1: nom = st.text_input("**Nom**", key=f"input_nom_{route}")
    with col2: montant = st.number_input("**Montant**", value=0.0, step=10.0, key=f"input_mont_{route}")
    with col3: 
        devise = st.selectbox("**Devise**", list(st.session_state.config["taux_change"].keys()), key=f"select_devise_{route}")
        unite = st.selectbox("**Unite**", ["UP", "palette", "conteneur", "general"], key=f"select_unite_{route}")
    with col4: pct_cip = st.number_input("**% CIP**", value=0.0, step=0.01, format="%.2f", key=f"input_pct_{route}")
    
    if st.button("**AJOUTER**", use_container_width=True, key=f"btn_ajout_frais_{route}") and nom:
        frais_data[nom] = {
            "montant": float(montant), 
            "devise": devise, 
            "unite": unite,
            "pourcentage_cip": float(pct_cip)
        }
        st.success(f"**{nom}** ({unite}) ajoute!")
        st.rerun()
    
    if frais_data:
        st.markdown("### **Frais de cette route**")
        df_frais = pd.DataFrame([{
            "Nom": k, "Montant": f"{v['montant']:.0f}", "Unite": v["unite"],
            "Devise": v["devise"], "%CIP": f"{v['pourcentage_cip']*100:.1f}%"
        } for k, v in frais_data.items()])
        st.dataframe(df_frais, use_container_width=True)
        
        suppr = st.multiselect("Supprimer", list(frais_data.keys()), key=f"multiselect_suppr_{route}")
        if st.button("Supprimer", key=f"btn_suppr_{route}") and suppr:
            for f in suppr: del frais_data[f]
            st.rerun()

with tab4:
    st.markdown("### **Devises**")
    st.session_state.config["devise_base"] = st.selectbox("**Devise Base**", ["MAD", "CHF", "EUR", "USD"], key="select_devise_base")
    
    new_devise = st.text_input("**Nouvelle devise**", key="input_new_devise")
    if st.button("Ajouter", key="btn_add_devise") and new_devise:
        st.session_state.config["taux_change"][new_devise] = 1.0
        st.rerun()
    
    taux_df = pd.DataFrame([{"Devise": k, "Taux": v} for k, v in st.session_state.config["taux_change"].items()])
    edited = st.data_editor(taux_df, num_rows="dynamic", use_container_width=True, key="editor_taux")
    for idx, row in edited.iterrows():
        st.session_state.config["taux_change"][row["Devise"]] = float(row["Taux"])

with tab5:
    st.markdown("### **Taxes**")
    col1, col2 = st.columns(2)
    with col1:
        dd = st.number_input("**Douane %**", value=st.session_state.config["Taxes"]["DroitsDouane"]*100, step=1.0, key="input_douane")
        st.session_state.config["Taxes"]["DroitsDouane"] = dd/100
    with col2:
        tva = st.number_input("**TVA %**", value=st.session_state.config["Taxes"]["TVA"]*100, step=1.0, key="input_tva")
        st.session_state.config["Taxes"]["TVA"] = tva/100

with tab6:
    if st.session_state.results:
        st.markdown("### **RESULTATS**")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.markdown(f'<div class="metric-card"><div class="metric-value">{st.session_state.shipment["nb_up"]:.1f}</div><div class="metric-label">UP</div></div>', unsafe_allow_html=True)
        with col2:
            st.markdown(f'<div class="metric-card"><div class="metric-value">{st.session_state.shipment["nb_palettes"]:.0f}</div><div class="metric-label">Palettes</div></div>', unsafe_allow_html=True)
        with col3:
            st.markdown(f'<div class="metric-card"><div class="metric-value">{st.session_state.shipment["nb_conteneurs"]:.0f}</div><div class="metric-label">Conteneurs</div></div>', unsafe_allow_html=True)
        with col4:
            st.markdown(f'<div class="metric-card"><div class="metric-value">{st.session_state.results["GRAND TOTAL"]:,.0f}</div><div class="metric-label">TOTAL {st.session_state.config["devise_base"]}</div></div>', unsafe_allow_html=True)
        
        # Editeur complet des resultats
        st.markdown("### **Modifier les Frais**")
        
        route_actuelle = st.session_state.shipment["route"]
        route_data = st.session_state.config["routes"][route_actuelle]
        devise_route = route_data["devise"]
        
        def convert_to_base(amount, source_devise, config):
            return amount * config["taux_change"][source_devise] / config["taux_change"][config["devise_base"]]
        
        def convert_from_base(amount, target_devise, config):
            return amount * config["taux_change"][config["devise_base"]] / config["taux_change"][target_devise]
        
        # Preparer les donnees pour l'editeur principal
        data_editor = []
        for categorie, montant in st.session_state.results.items():
            if "Frais Perso:" in categorie:
                continue
            elif categorie in ["Total Frais Personnalisés", "Droits Douane", "TVA", "GRAND TOTAL"]:
                data_editor.append({"Categorie": categorie, "Montant": float(montant), "Editable": "Non"})
            else:
                data_editor.append({"Categorie": categorie, "Montant": float(montant), "Editable": "Oui"})
        
        df_main = pd.DataFrame(data_editor)
        
        col_main1, col_main2 = st.columns([3, 1])
        with col_main1:
            edited_main = st.data_editor(
                df_main,
                column_config={
                    "Montant": st.column_config.NumberColumn(
                        label="Montant",
                        format="%.0f",
                        step=100.0
                    )
                },
                use_container_width=True,
                hide_index=True,
                key="editor_resultats_main"
            )
        
        with col_main2:
            st.markdown("")
            
            if st.button("**Sauvegarder les frais**", key="btn_save_frais_fixes", use_container_width=True):
                for idx, row in edited_main.iterrows():
                    categorie = row["Categorie"]
                    nouveau_montant = float(row["Montant"])
                    
                    if row["Editable"] == "Oui":
                        if categorie == "Frais Départ":
                            nouveau_montant_MAD = convert_from_base(nouveau_montant, "MAD", st.session_state.config)
                            total_actuel_MAD = sum(route_data["FraisMaroc"].values())
                            if total_actuel_MAD > 0:
                                ratio = nouveau_montant_MAD / total_actuel_MAD
                                for k in route_data["FraisMaroc"].keys():
                                    route_data["FraisMaroc"][k] = route_data["FraisMaroc"][k] * ratio
                        
                        elif categorie == "Frais Arrivée":
                            nouveau_montant_devise = convert_from_base(nouveau_montant, devise_route, st.session_state.config)
                            total_actuel_devise = sum(route_data["FraisArrivee"].values())
                            if total_actuel_devise > 0:
                                ratio = nouveau_montant_devise / total_actuel_devise
                                for k in route_data["FraisArrivee"].keys():
                                    route_data["FraisArrivee"][k] = route_data["FraisArrivee"][k] * ratio
                        
                        elif categorie == "Fret Maritime":
                            if st.session_state.shipment["nb_up"] > 0:
                                nouveau_montant_devise = convert_from_base(nouveau_montant, devise_route, st.session_state.config)
                                fret_data = route_data["FretMaritime"]
                                total_coeff = (1 + fret_data["BAF"] + fret_data["CAF"] - 
                                             fret_data["Rabais"] - fret_data["Remise"] - fret_data["Ristourne"])
                                if total_coeff > 0:
                                    nouveau_fret = nouveau_montant_devise / (st.session_state.shipment["nb_up"] * total_coeff)
                                    route_data["FretMaritime"]["Fret"] = max(0, nouveau_fret)
                                else:
                                    route_data["FretMaritime"]["Fret"] = 0
                        
                        elif categorie == "Fret Routier":
                            if nouveau_montant == 0:
                                route_data["FretRoutier"]["Fret"] = 0
                                route_data["FretRoutier"]["CAF"] = 0
                                route_data["FretRoutier"]["Rabais"] = 0
                                route_data["FretRoutier"]["Remise"] = 0
                                route_data["FretRoutier"]["Ristourne"] = 0
                                route_data["FretRoutier"]["Assurance"] = 0
                            else:
                                if st.session_state.shipment["nb_up"] > 0:
                                    nouveau_montant_devise = convert_from_base(nouveau_montant, devise_route, st.session_state.config)
                                    fret_data = route_data["FretRoutier"]
                                    
                                    total_coeff = (1 + fret_data["CAF"] - fret_data["Rabais"] - 
                                                 fret_data["Remise"] - fret_data["Ristourne"])
                                    
                                    if total_coeff > 0:
                                        assurance_montant = st.session_state.shipment["valeur_cip"] * fret_data.get("Assurance", 0)
                                        assurance_devise = convert_to_base(assurance_montant, devise_route, st.session_state.config)
                                        
                                        montant_fret_sans_assurance = nouveau_montant_devise - assurance_devise
                                        
                                        if montant_fret_sans_assurance > 0:
                                            nouveau_fret_base = montant_fret_sans_assurance / (st.session_state.shipment["nb_up"] * total_coeff)
                                            route_data["FretRoutier"]["Fret"] = max(0, nouveau_fret_base)
                                        else:
                                            route_data["FretRoutier"]["Fret"] = 0
                                    else:
                                        route_data["FretRoutier"]["Fret"] = 0
                
                st.session_state.results = calculate_all_costs(st.session_state.config, st.session_state.shipment)
                st.success("Frais mis a jour et recalcules!")
                st.rerun()
        
        # Section Frais Personnalises
        frais_perso = route_data["FraisPersonnalises"]
        if frais_perso:
            st.markdown("---")
            st.markdown("### **Frais Personnalises**")
            
            frais_list = []
            for nom, data in frais_perso.items():
                key_perso = f"Frais Perso: {nom}"
                montant_result = st.session_state.results.get(key_perso, 0)
                
                frais_list.append({
                    "Nom": nom,
                    "Montant Base": float(data["montant"]),
                    "Montant Calcule": float(montant_result),
                    "Devise": data["devise"],
                    "Unite": data["unite"],
                    "% CIP": float(data.get("pourcentage_cip", 0)) * 100
                })
            
            df_frais = pd.DataFrame(frais_list)
            col_frais1, col_frais2 = st.columns([3, 1])
            
            with col_frais1:
                edited_frais = st.data_editor(
                    df_frais,
                    column_config={
                        "Montant Base": st.column_config.NumberColumn(format="%.2f"),
                        "Montant Calcule": st.column_config.NumberColumn(format="%.2f"),
                        "% CIP": st.column_config.NumberColumn(format="%.2f")
                    },
                    use_container_width=True,
                    key=f"editor_frais_resultats_{route_actuelle}"
                )
            
            with col_frais2:
                if st.button("**Sauvegarder Perso**", key=f"btn_save_perso_res_{route_actuelle}", use_container_width=True):
                    for idx, row in edited_frais.iterrows():
                        nom = row["Nom"]
                        frais_perso[nom]["montant"] = float(row["Montant Base"])
                        frais_perso[nom]["pourcentage_cip"] = float(row["% CIP"]) / 100
                    
                    st.session_state.results = calculate_all_costs(st.session_state.config, st.session_state.shipment)
                    st.success("Frais personnalises sauvegardes et recalcules!")
                    st.rerun()
                
                noms_frais = [row["Nom"] for _, row in edited_frais.iterrows()]
                suppr_frais = st.multiselect("Supprimer", noms_frais, key=f"suppr_perso_res_{route_actuelle}")
                if st.button("**Supprimer**", key=f"btn_del_perso_res_{route_actuelle}", use_container_width=True) and suppr_frais:
                    for nom in suppr_frais:
                        del frais_perso[nom]
                    st.session_state.results = calculate_all_costs(st.session_state.config, st.session_state.shipment)
                    st.success(f"{len(suppr_frais)} frais supprimes et recalcules!")
                    st.rerun()
        
        # Affichage final du tableau recapitulatif
        st.markdown("---")
        st.markdown("### **Recapitulatif Final**")
        
        categories = []
        montants = []
        
        for categorie, montant in st.session_state.results.items():
            if "Frais Perso:" in categorie:
                categories.append(categorie.replace("Frais Perso: ", ""))
            else:
                categories.append(categorie)
            montants.append(float(montant))
        
        df_final = pd.DataFrame({
            "**Categorie**": categories,
            "**Montant**": [f"{m:,.0f}" for m in montants],
            "Devise": st.session_state.config['devise_base']
        })
        
        st.dataframe(df_final, use_container_width=True, hide_index=True)
        
        # Graphique
        fig = px.pie(
            values=montants, 
            names=categories, 
            hole=0.4,
            title="Repartition des couts"
        )
        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig, use_container_width=True)
        
        # Export Excel
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df_detailed = pd.DataFrame({
                "Categorie": categories,
                "Montant": montants,
                "Devise": st.session_state.config['devise_base']
            })
            df_detailed.to_excel(writer, sheet_name='Resultats', index=False)
            
            df_shipment = pd.DataFrame([st.session_state.shipment])
            df_shipment.to_excel(writer, sheet_name='Envoi', index=False)
            
            if st.session_state.history:
                df_history = pd.DataFrame(st.session_state.history)
                df_history.to_excel(writer, sheet_name='Historique', index=False)
            
            df_route = pd.DataFrame({
                "Parametre": list(route_data.keys()),
                "Valeur": [str(v) for v in route_data.values()]
            })
            df_route.to_excel(writer, sheet_name='Configuration Route', index=False)
        
        st.download_button(
            "**EXCEL COMPLET**", 
            output.getvalue(), 
            f"Transport_{route_actuelle}_{date.today().strftime('%Y%m%d')}.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    
    else:
        st.info("**Aucun resultat a afficher. Veuillez effectuer un calcul dans l'onglet 'Calcul'.**")
        
        if st.button("**Aller au Calcul**", use_container_width=True):
            st.session_state.active_tab = 0
            st.rerun()

with tab7:
    st.markdown("### **LEGENDE & AIDE**")
    st.markdown("""
    **Unites de frais personnalises :**
    
    | **Unite** | **× Quantite** | **Exemple** |
    |-----------|----------------|-------------|
    | **UP** | Nb UP | 50 MAD × 10 UP = 500 MAD |
    | **palette** | Nb Palettes | 100 MAD × 5 = 500 MAD |
    | **conteneur** | Nb Conteneurs | 5000 MAD × 1 = 5000 MAD |
    | **general** | 1 (fixe) | 2000 MAD fixe |
    
    **% CIP =** Pourcentage de la **Valeur CIP** saisie
    **Ex:** 10 000 MAD CIP × 1.5% = 150 MAD ajoute
    """)

    if st.button("**RESET COMPLET**"):
        st.session_state.config = {}
        st.session_state.shipment = {}
        st.session_state.results = None
        st.rerun()

# FEEDBACK TELEGRAM
st.markdown("---")

st.markdown('<div class="input-section" style="padding: 2rem; margin: 1rem 0;">', unsafe_allow_html=True)

st.markdown("""
<h3 style="text-align: center; margin-bottom: 2rem; color: #667eea;">
    **Votre Avis Nous Interesse**
</h3>
""", unsafe_allow_html=True)

TOKEN = st.secrets.get("TELEGRAM_TOKEN", "TON_TOKEN_BOT_TELEGRAM") 
CHAT_ID = st.secrets.get("TELEGRAM_CHAT_ID", "")

with st.form("feedback_form", clear_on_submit=True):
    name = st.text_input("**Nom / Entreprise**", 
                        placeholder="Votre nom",
                        help="Optionnel",
                        label_visibility="collapsed")
    
    msg = st.text_area("**Votre commentaire ou suggestion**", 
                      placeholder="Votre commentaire ou suggestion",
                      height=100,
                      label_visibility="collapsed")
    
    submitted = st.form_submit_button("**ENVOYER L'AVIS**", use_container_width=True)

if submitted and msg.strip():
    try:
        import requests
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        text = f"*CALCUL TRANSPORT*\n\n*{name or 'Anonyme'}*\n*{msg}*\n{date.today().strftime('%d/%m/%Y %H:%M')}"
        response = requests.post(url, json={
            "chat_id": CHAT_ID, 
            "text": text, 
            "parse_mode": "Markdown"
        })
        
        if response.status_code == 200:
            st.success("**Merci infiniment pour votre retour !**")
            
        else:
            st.error("**Erreur envoi Telegram**")
    except:
        st.error("**Erreur reseau**")
elif submitted:
    st.warning("**Le commentaire ne peut pas etre vide**")

st.markdown('</div>', unsafe_allow_html=True)
st.markdown("---")
st.caption("Calculateur Transport")
