import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Titre de votre Mini-SaaS
st.title("🚀 Mon Premier Mini-SaaS de Tâches")
st.write("Gestion simplifiée des missions administratives.")

# Fichier pour sauvegarder les données localement (pour le test)
DB_FILE = "taches_data.csv"

# Charger les données existantes
if os.path.exists(DB_FILE):
    df_existing = pd.read_csv(DB_FILE)
else:
    df_existing = pd.DataFrame(columns=["Nom", "Email", "Tache", "Date_Debut", "Date_Fin"])

# Formulaire de saisie
with st.form("form_tache", clear_on_submit=True):
    st.subheader("Ajouter une nouvelle tâche")
    nom = st.text_input("Nom complet")
    email = st.text_input("Adresse Email")
    tache = st.text_area("Description de la tâche")
    date_debut = st.date_input("Date de début", datetime.today())
    date_fin = st.date_input("Date de fin", datetime.today())
    
    # Bouton de validation
    submitted = st.form_submit_button("Enregistrer la tâche")
    
    if submitted:
        if nom and email and tache:
            # Créer une ligne avec les nouvelles données
            nouvelle_ligne = pd.DataFrame({
                "Nom": [nom],
                "Email": [email],
                "Tache": [tache],
                "Date_Debut": [str(date_debut)],
                "Date_Fin": [str(date_fin)]
            })
            
            # Ajouter à la liste et sauvegarder
            df_existing = pd.concat([df_existing, nouvelle_ligne], ignore_index=True)
            df_existing.to_csv(DB_FILE, index=False)
            st.success("Tâche enregistrée avec succès !")
        else:
            st.error("Veuillez remplir au moins le nom, l'email et la tâche.")

# Affichage des tâches enregistrées
st.divider()
st.subheader("📋 Liste des tâches enregistrées")
if not df_existing.empty:
    st.dataframe(df_existing, use_container_width=True)
else:
    st.info("Aucune tâche enregistrée pour le moment.")