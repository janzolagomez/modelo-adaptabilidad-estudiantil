#!/usr/bin/env python
# coding: utf-8

# In[9]:


import streamlit as st
import pandas as pd
import joblib

# Cargar el modelo entrenado
modelo = joblib.load("mejor_modelo_adaptabilidad.pkl")

st.set_page_config(page_title="Predicción de Adaptabilidad Digital", layout="centered")
st.title("🎓 Predicción del Nivel de Adaptabilidad Digital de Estudiantes")

st.markdown("Completa los datos del estudiante para predecir su nivel de adaptación al entorno educativo digital.")

# Diccionarios de traducción español → inglés
mapeos = {
    "Gender": {"Masculino": "Male", "Femenino": "Female"},
    "Age": {
        "0-20 años": "0-20", "21-25 años": "21-25", "26-30 años": "26-30",
        "31-35 años": "31-35", "36-40 años": "36-40", "41 años o más": "41+"
    },
    "Education Level": {"Primaria/Secundaria": "School", "Técnico/Instituto": "College", "Universidad": "University"},
    "Institution Type": {"Pública": "Government", "Privada": "Private"},
    "IT Student": {"Sí, actualmente estudio tecnología": "Yes", "No estudio ni he estudiado tecnología": "No"},
    "Location": {"Urbana": "Urban", "Rural": "Rural"},
    "Load-shedding": {"Nunca": "Low", "A veces": "Medium", "Casi siempre": "High"},
    "Financial Condition": {"Bajo nivel de ingresos": "Poor", "Nivel medio de ingresos": "Mid", "Alto nivel de ingresos": "Rich"},
    "Internet Type": {"Datos móviles": "Mobile Data", "Wifi": "Wifi", "Sin acceso a internet": "No Internet"},
    "Network Type": {"2G": "2G", "3G": "3G", "4G": "4G", "Sin acceso a internet": "No Internet"},
    "Class Duration": {"0 horas": "0", "1 a 3 horas": "1-3", "3 a 6 horas": "3-6", "Más de 6 horas": ">6"},
    "Self Lms": {"Sí": "Yes", "No": "No"},
    "Device": {"Teléfono móvil": "Mobile", "Ordenador": "Computer", "Tableta": "Tablet"}
}

# Formulario
with st.form("formulario_prediccion"):
    genero = st.selectbox("Género", list(mapeos["Gender"].keys()))
    edad = st.selectbox("Edad", list(mapeos["Age"].keys()))
    nivel = st.selectbox("Nivel educativo alcanzado", list(mapeos["Education Level"].keys()))
    institucion = st.selectbox("Tipo de institución educativa", list(mapeos["Institution Type"].keys()))
    it = st.selectbox("¿Has estudiado o estás estudiando algo relacionado con tecnología?", list(mapeos["IT Student"].keys()))
    ubicacion = st.selectbox("Ubicación de residencia", list(mapeos["Location"].keys()))
    cortes = st.selectbox("Frecuencia de cortes eléctricos donde vives", list(mapeos["Load-shedding"].keys()))
    condicion = st.selectbox("Ingresos económicos del hogar", list(mapeos["Financial Condition"].keys()))
    internet = st.selectbox("Tipo de conexión a internet", list(mapeos["Internet Type"].keys()))
    red = st.selectbox("Tipo de red disponible", list(mapeos["Network Type"].keys()))
    duracion = st.selectbox("Duración diaria de clases virtuales", list(mapeos["Class Duration"].keys()))
    lms = st.selectbox("¿Utiliza un sistema propio para aprender en línea (LMS)?", list(mapeos["Self Lms"].keys()))
    dispositivo = st.selectbox("Dispositivo principal que usa para estudiar", list(mapeos["Device"].keys()))

    enviado = st.form_submit_button("Predecir")

# Predicción
if enviado:
    entrada = pd.DataFrame([{
        "Gender": mapeos["Gender"][genero],
        "Age": mapeos["Age"][edad],
        "Education Level": mapeos["Education Level"][nivel],
        "Institution Type": mapeos["Institution Type"][institucion],
        "IT Student": mapeos["IT Student"][it],
        "Location": mapeos["Location"][ubicacion],
        "Load-shedding": mapeos["Load-shedding"][cortes],
        "Financial Condition": mapeos["Financial Condition"][condicion],
        "Internet Type": mapeos["Internet Type"][internet],
        "Network Type": mapeos["Network Type"][red],
        "Class Duration": mapeos["Class Duration"][duracion],
        "Self Lms": mapeos["Self Lms"][lms],
        "Device": mapeos["Device"][dispositivo]
    }])

    prediccion = modelo.predict(entrada)[0]

    recomendaciones = {
        "Low": {
            "nivel": "Bajo",
            "mensaje": "Se recomienda acompañamiento personalizado y acceso a recursos digitales básicos."
        },
        "Moderate": {
            "nivel": "Moderado",
            "mensaje": "Tiene una base aceptable. Puede mejorar con práctica digital y apoyo formativo."
        },
        "High": {
            "nivel": "Alto",
            "mensaje": "Excelente nivel de adaptación. Puede apoyar a sus compañeros o asumir retos más avanzados."
        }
    }

    nivel = recomendaciones[prediccion]["nivel"]
    consejo = recomendaciones[prediccion]["mensaje"]

    st.success(f"📊 Nivel de adaptabilidad digital: **{nivel}**")
    st.info(f"💡 Recomendación: {consejo}")

