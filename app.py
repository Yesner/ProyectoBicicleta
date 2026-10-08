import streamlit as st
from funciones import cargar_datos, filtrar_datos, preparar_analisis

st.set_page_config(page_title="Renta de bicicletas", page_icon="🚲", layout="wide")

df = cargar_datos()

st.title("Analisis de rentas y uso de bicicletas")
st.write("Bienvenido a la aplicación de análisis de rentas y uso de bicicletas.")

inicio, exploracion, analisis = st.tabs(["Inicio", "Exploración", "Análisis"])

with inicio:
    st.header("Conociendo el conjunto de datos")
    st.write("El dataset contiene información sobre las rentas de bicicletas, fechas, estaciones del año, clima y otros detalles relevantes.")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Registros", f"{len(df):,}")
    c2.metric("Total de rentas", f"{df['count'].sum():,}")
    c3.metric("Promedio de rentas por mes", f"{df['count'].sum() / df['Mes_num'].nunique():,.2f}")
    c4.metric("Promedio por día", f"{df['count'].sum() / df['Dia_num'].nunique():,.2f}")

    st.subheader("Resumen del conjunto de datos")
    columnas = ["datetime", "Estación", "Clima", "temp", "humidity","count"]
    st.dataframe(df[columnas].head(10), use_container_width=True)

with exploracion:
    st.header("Exploración de los datos")
    st.write("Selecciona algunos filtros y observa cómo cambian los datos.")

    estacion = st.selectbox("Selecciona la estación", ["Todas"] + list(df["Estación"].unique()))
    clima = st.selectbox("Selecciona el clima", ["Todos"] + list(df["Clima"].unique()))
    año = st.selectbox("Selecciona el año", ["Todos"] + list(df["Año"].unique()))
    mes = st.selectbox("Mes", ["Todos"] + ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"])

    filtrado = filtrar_datos(df, estacion, clima, año, mes)
    st.info(f"Se han filtrado {len(filtrado):,} registros.")

    columnas = ["datetime", "Estación", "Clima", "temp", "humidity","count"]
    st.dataframe(filtrado[columnas], use_container_width=True, height=350)

    if st.checkbox("Mostrar resumen estadistico"):
        st.dataframe(filtrado[["temp", "humidity", "windspeed", "count"]].describe().round(2), use_container_width=True)

    if st.checkbox("Mostrar datos faltantes"):
        st.dataframe(filtrado.isnull().sum().to_frame(name="Faltantes"), use_container_width=True)



with analisis:
    st.header("Análisis descriptivo")
    st.write("Aquí solo visualizamos cómo se distribuyen las rentas de bicicletas en diferentes categorías.")

    opcion = st.selectbox("¿Qué desea analizar?", ["Rentas por mes", "Rentas por hora", "Rentas por estación", "Rentas según el clima"])

    datos_grafico, tipo = preparar_analisis(df, opcion)

    st.subheader(opcion)
    if tipo == "linea":
        st.line_chart(datos_grafico)
    else:
        st.bar_chart(datos_grafico)

    st.dataframe(datos_grafico, use_container_width=True)