import streamlit as st
from funciones import carga_datos

st.set_page_config(page_title="Renta de bicicletas", page_icon="🚲", layout="wide")

df = carga_datos()

st.title("Analisis de rentas y uso de bicicletas")
st.write("Bienvenido a la aplicación de análisis de rentas y uso de bicicletas.")

inicio, exploracion, analisis = st.tabs(["Inicio", "Exploración", "Análisis"])

with inicio:
    st.header("Inicio")
    st.write("Esta es la sección de inicio de la aplicación.")

with exploracion:
    st.header("Exploración")
    st.write("Esta es la sección de exploración de datos.")

with analisis:
    st.header("Análisis")
    st.write("Esta es la sección de análisis de datos.")