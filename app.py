import streamlit as st
from funciones import carga_datos

st.set_page_config(page_title="Renta de bicicletas", page_icon="🚲", layout="wide")

df = carga_datos()

st.title("Analisis de rentas y uso de bicicletas")
st.write("Bienvenido a la aplicación de análisis de rentas y uso de bicicletas.")

inicio, exploracion, analisis = st.tabs(["Inicio", "Exploración", "Análisis"])

with inicio:
    st.header("Conociendo el conjunto de datos")
    st.write("El dataset contiene información sobre las rentas de bicicletas, fechas, estaciones del año, clima y otros detalles relevantes.")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Registros", f"{len(df):,}")
    c2.metric("Total de rentas", f"{df['count'].sum():,}")
    c3.metric("Promedio de rentas por mes", f"{df['count'].sum() / df['MES_NUM'].nunique():,.2f}")
    c4.metric("Promedio por día", f"{df['count'].sum() / df['DIA_NUM'].nunique():,.2f}")

    st.subheader("Resumen del conjunto de datos")
    columnas = ["datetime", "ESTACION_NUM", "CLIMA_NUM", "temp", "humidity","count"]
    st.dataframe(df[columnas].head(10), use_container_width=True)

with exploracion:
    st.header("Exploración")
    st.write("Esta es la sección de exploración de datos.")

with analisis:
    st.header("Análisis")
    st.write("Esta es la sección de análisis de datos.")