import streamlit as st

st.title("Mi primera aplicación")

nombre = st.text_input("Ingresa tu nombre")

if st.button("Saludar"):
    if nombre:
        st.write(f"Hola, {nombre}!")
        st.balloons()
        st.success("¡Saludo enviado con éxito!")
        st.info("¡Disfruta de la aplicación!")
        st.warning("Recuerda cerrar la aplicación cuando termines")
    else:
        st.error("Por favor, ingresa tu nombre antes de saludar.")
        st.error("Aún no has presionado el botón de saludo.")
        st.info("Presiona el botón para recibir un saludo.")
