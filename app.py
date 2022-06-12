import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from plotly.subplots import make_subplots
from scipy import stats
from scipy import signal
from numpy import linalg as LA
import sympy
import math
import matplotlib.pyplot as plt
import os
import pathlib


# Full size page
st.set_page_config(
    page_title = "Plantes - Papa",
    page_icon = "🍀")

# Couleur
vert = "#008744"
bleue = "#0057e7"
bleue_claire = "#99bbf5"
rouge = "#d62d20"
jaune = "#ffa700"
tiede = "#ffcc5c"
noire = "#111111"
gris = "#999999"
blanc = "#ffffff"


uploaded_file = st.file_uploader("Choisir un fichier")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file, header = 0, sep = ";")

    option = st.selectbox(
     'Choisir une plante?',
     data['Plante '].unique())

    st.markdown(f'### Plante sélectionnée : {option}')

    # st.image("https://www.yao-dao.com/Picture/3756")

    # st.write(data.loc[data["Plante "]== option])

    analyse = data.loc[data["Plante "]== option]

    # Paramètre HTML 
    # display( HTML( analyse.to_html().replace("\\n","<br>") ) )

    # analyse.style.set_properties(**{
    #     'text-align': 'center',
    #     'white-space': 'pre-wrap',
    # })

    # Analyse
    st.markdown("#### Fu Xing Jué")

    # Variables :
    petit_cercle = analyse.iloc[0,5]
    grand_cercle = analyse.iloc[0,6]

    st.markdown("""
    <style>
    .small-font {
        font-size:60px !important;
    }
    .big-font{
        font-size:100px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1: 
        st.write("Petit cercle")
        if petit_cercle == "Bois":
            st.markdown('<p class="small-font">🟢</p>', unsafe_allow_html=True)
        elif petit_cercle == "Feu":
            st.markdown('<p class="small-font">🔴</p>', unsafe_allow_html=True)
        elif petit_cercle == "Terre":
            st.markdown('<p class="small-font">🟠</p>', unsafe_allow_html=True)
        elif petit_cercle == "Métal":
            st.markdown('<p class="small-font">⚪️</p>', unsafe_allow_html=True)
        elif petit_cercle == "Eau":
            st.markdown('<p class="small-font">⚫️</p>', unsafe_allow_html=True)

    with col2: 
        st.write("Grand cercle")
        if grand_cercle == "Bois":
            st.markdown('<p class="big-font">🟢</p>', unsafe_allow_html=True)
        elif grand_cercle == "Feu":
            st.markdown('<p class="big-font">🔴</p>', unsafe_allow_html=True)
        elif grand_cercle == "Terre":
            st.markdown('<p class="big-font">🟠</p>', unsafe_allow_html=True)
        elif grand_cercle == "Métal":
            st.markdown('<p class="big-font">⚪️</p>', unsafe_allow_html=True)
        elif grand_cercle == "Eau":
            st.markdown('<p class="big-font">⚫️</p>', unsafe_allow_html=True)


    st.markdown("#### Nature & Saveur")
    Nat_Sav = pd.DataFrame({
            "Nature" : (analyse.iloc[0,1], analyse.iloc[0,2]),
            "Saveur" : (analyse.iloc[0,3], analyse.iloc[0,4]),
        }).T

    Nat_Sav.fillna(".",inplace=True)

    Nat_Sav_style = Nat_Sav.style.applymap(lambda x: 
        f'background-color : {rouge}' if (x == "chaud" or x == "amer") else 
        f'background-color : {bleue_claire}' if (x =="frais") else
        f'background-color : {bleue}' if (x =="froid") else
        f'background-color : {tiede}' if (x =="tiède" or x == "doux/sucré") else
        f'background-color : {noire}' if (x =="salé") else
        f'background-color : {gris}' if (x =="piquant/acre") else
        f'background-color : {vert}' if (x =="acide") 
        else "")\
            .applymap(lambda x:
                f"color : {blanc} " if (x == "salé") else "")

    st.table(Nat_Sav_style)

    st.markdown("#### Lieu d'action")
    lieu_action = pd.DataFrame({
            "Lieu d'action" : (analyse.iloc[0,7],analyse.iloc[0,8],analyse.iloc[0,9],analyse.iloc[0,10])
        }).T

    lieu_action.dropna(axis = 1, inplace=True)

    st.table(lieu_action)

    
    posologie = analyse.iloc[0,11]
    st.markdown(f"**Posologie |** {posologie}")

    st.markdown("#### Actions / Indications")
    
    action = pd.DataFrame({
        "Action_1" : (analyse.iloc[0,12],analyse.iloc[0,13]),
        "Action_2" : (analyse.iloc[0,14],analyse.iloc[0,15]),
        "Action_3" : (analyse.iloc[0,16],analyse.iloc[0,17]),
        "Action_4" : (analyse.iloc[0,18],analyse.iloc[0,19])
    }).T

    action.dropna(axis=0, inplace=True)

    st.table(action)

    st.markdown("#### Précautions d'emploi et contre-indication")
    precaution = pd.DataFrame({
        "Précaution d'emploi" : [analyse.iloc[0,20]],
        "Contre-indication" : [analyse.iloc[0,21]]
    })

    st.markdown(f"**Précaution d'emploi :** {precaution.iloc[0,0]}  \n**Contre-indication :** {precaution.iloc[0,1]}")
    # st.table(precaution)

    st.markdown("#### Indications clinique")
    clinique = str(analyse.iloc[0,22]).replace("\n", " \n")
    if clinique == 'nan' :
        clinique = '...'
    st.markdown(f"{clinique}")

    st.markdown("#### Intéraction herbs-drugs")
    herbs_drugs = str(analyse.iloc[0,23]).replace("\n", " \n")
    if herbs_drugs == 'nan' :
        herbs_drugs = '...'
    st.markdown(f"{herbs_drugs}")

