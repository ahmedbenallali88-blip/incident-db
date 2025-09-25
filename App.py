import streamlit as st
from modules.auth import login
from modules.forms import incident_form
from modules.dashboard import show_dashboard

st.set_page_config(page_title="Fiche Incident 2025", layout="wide")
st.title("📋 Fiche Incident Qualité")

username = st.text_input("Nom d'utilisateur")
password = st.text_input("Mot de passe", type="password")
role = login(username, password)

if role:
    st.success(f"Bienvenue {username} ({role})")
    incident_form(role)
    if role == "coordinateur":
        show_dashboard()
else:
    st.warning("Identifiants incorrects ou accès refusé")
