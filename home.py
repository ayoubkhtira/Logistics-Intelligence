# home.py - Page d'accueil Logistics Intelligence (noms réels + style homogène)
import streamlit as st
import streamlit.components.v1 as components

# Configuration
st.set_page_config(
    page_title="Logistics Intelligence", 
    page_icon="🚚", 
    layout="wide",
    initial_sidebar_state="collapsed"  # Masquer sidebar par défaut
)

# CSS Styling HOMOGÈNE avec noms officiels
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
    height: 240px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    transition: all 0.3s ease !important;
    position: relative;
    overflow: hidden;
}
.tool-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
    transition: left 0.6s;
}
.tool-card:hover::before {
    left: 100%;
}
.tool-card:hover {
    transform: translateY(-10px) scale(1.02) !important;
    box-shadow: 0 35px 70px rgba(102,126,234,0.5) !important;
    border-color: #667eea !important;
}

.soon-card {
    background: linear-gradient(145deg, rgba(34,197,94,0.25), rgba(16,185,129,0.25)) !important;
    backdrop-filter: blur(20px); 
    color: #e2e8f0 !important; 
    padding: 2.5rem 1.5rem !important; 
    border-radius: 24px !important; 
    text-align: center !important; 
    border: 2px solid rgba(34,197,94,0.5) !important; 
    box-shadow: 0 25px 50px rgba(34,197,94,0.4) !important; 
    margin: 1rem 0.5rem !important;
    height: 240px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    animation: pulse 2s infinite;
    position: relative;
    overflow: hidden;
}
.soon-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
    transition: left 0.8s;
}
.soon-card:hover::before {
    left: 100%;
}

@keyframes pulse {
    0%, 100% { box-shadow: 0 25px 50px rgba(34,197,94,0.4); }
    50% { box-shadow: 0 25px 50px rgba(34,197,94,0.7); }
}

.tool-icon { 
    font-size: 4rem !important; 
    margin-bottom: 1.2rem;
    display: block;
    filter: drop-shadow(0 4px 8px rgba(0,0,0,0.3));
}
.tool-title { 
    font-size: 1.3rem !important; 
    font-weight: 700 !important;
    font-family: 'Orbitron', monospace !important;
    margin-bottom: 0.8rem;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    line-height: 1.2;
}
.tool-desc { 
    font-size
