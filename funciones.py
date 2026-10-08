from pathlib import Path
import pandas as pd

ESTACIONES = {
    1: "Primavera",
    2: "Verano",
    3: "Otoño",
    4: "Invierno",
}

CLIMAS = {
    1: "Despejado",
    2: "Nublado / Bruma",
    3: "Lluvia o nieve ligera",
    4: "Clima severo",
}

MESES = {
    1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril",
    5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto",
    9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre",
}

DIAS = {
    0: "Lunes", 1: "Martes", 2: "Miércoles", 3: "Jueves",
    4: "Viernes", 5: "Sábado", 6: "Domingo",
}


def cargar_datos():
    
    ruta = Path(__file__).parent / "data" / "bicicleta.csv"
    df = pd.read_csv(ruta)

    df["datetime"] = pd.to_datetime(df["datetime"])
    df["Año"] = df["datetime"].dt.year
    df["Mes_num"] = df["datetime"].dt.month
    df["Mes"] = df["Mes_num"].map(MESES)
    df["Hora"] = df["datetime"].dt.hour
    df["Dia_num"] = df["datetime"].dt.dayofweek
    df["Día"] = df["Dia_num"].map(DIAS)
    df["Estación"] = df["season"].map(ESTACIONES)
    df["Clima"] = df["weather"].map(CLIMAS)

    return df


def filtrar_datos(df, estacion, clima, año, mes):
   
    resultado = df.copy()

    if estacion != "Todas":
        resultado = resultado[resultado["Estación"] == estacion]
    if clima != "Todos":
        resultado = resultado[resultado["Clima"] == clima]
    if año != "Todos":
        resultado = resultado[resultado["Año"] == int(año)]
    if mes != "Todos":
        resultado = resultado[resultado["Mes"] == mes]

    return resultado


def preparar_analisis(df, opcion):
    
    if opcion == "Rentas por mes":
        datos = df.groupby("Mes_num")["count"].sum().reindex(range(1, 13))
        datos.index = [MESES[i] for i in datos.index]
        return datos.to_frame("Rentas"), "barras"

    if opcion == "Rentas por hora":
        datos = df.groupby("Hora")["count"].sum()
        return datos.to_frame("Rentas"), "linea"

    if opcion == "Rentas por estación":
        orden = ["Primavera", "Verano", "Otoño", "Invierno"]
        datos = df.groupby("Estación")["count"].sum().reindex(orden)
        return datos.to_frame("Rentas"), "barras"

    if opcion == "Rentas según el clima":
        orden = ["Despejado", "Nublado / Bruma", "Lluvia o nieve ligera", "Clima severo"]
        datos = df.groupby("Clima")["count"].sum().reindex(orden).dropna()
        return datos.to_frame("Rentas"), "barras"

    # Rentas por día de la semana
    datos = df.groupby("Dia_num")["count"].sum().reindex(range(7))
    datos.index = [DIAS[i] for i in datos.index]
    return datos.to_frame("Rentas"), "barras"
