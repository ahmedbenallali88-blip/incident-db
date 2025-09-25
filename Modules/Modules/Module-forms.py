import streamlit as st
import sqlite3
from datetime import datetime

def incident_form(role):
    st.subheader("📝 Nouveau Incident")
    date = st.date_input("Date", value=datetime.today())
    heure = st.time_input("Heure", value=datetime.now().time())
    composant = st.text_input("Numéro de composant")
    article = st.text_input("Description article")
    couleur = st.selectbox("Couleur", ["L", "R", "B"])
    ligne = st.text_input("Ligne")
    machine = st.text_input("Machine")
    animateur = st.text_input("Animateur qualité")
    defaut1 = st.text_input("Défaut qualité")
    defaut2 = st.text_input("Défaut qualité 2")

    if st.button("✅ Enregistrer"):
        conn = sqlite3.connect("database/incidents.db")
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO incidents (date, heure, composant, article, couleur, ligne, machine, animateur, defaut1, defaut2)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (date, heure.strftime("%H:%M:%S"), composant, article, couleur, ligne, machine, animateur, defaut1, defaut2))
        conn.commit()
        conn.close()
        st.success("Incident enregistré avec succès ✅")
