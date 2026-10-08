from pathlib import Path
import pandas as pd

ESTACIONES = {
    1: "Primavera",
    2: "Verano",
    3: "Otoño",
    4: "Invierno"
}

CLIMAS = {
    1: "Despejado",
    2: "Nublado",
    3: "Lluvia o nieve ligera",
    4: "Clima severo"
}

MESES = {
    1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Septiembre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre"
}

DIAS = {
    0: "Lunes",
    1: "Martes",
    2: "Miércoles",
    3: "Jueves",
    4: "Viernes",
    5: "Sábado",
    6: "Domingo"
}

def carga_datos():
    ruta = Path(__file__).parent / "data" / "bicicleta.csv"
    df = pd.read_csv(ruta)

    df["datetime"] = pd.to_datetime(df["datetime"])
    df["AÑO"] = df["datetime"].dt.year
    df["MES_NUM"] = df["datetime"].dt.month
    df["MES"] = df["MES_NUM"].map(MESES)
    df["DIA_NUM"] = df["datetime"].dt.dayofweek
    df["DIA"] = df["DIA_NUM"].map(DIAS)
    df["ESTACION_NUM"] = df["season"].map(ESTACIONES)
    df["CLIMA_NUM"] = df["weather"].map(CLIMAS)

    return df

def filtrar_datos(df, estacion, clima, año, mes):
    resultado = df.copy()

    if estacion != "Todas":
        resultado = resultado[resultado["ESTACION_NUM"] == estacion]
    
    if clima != "Todos":
        resultado = resultado[resultado["CLIMA_NUM"] == clima]
    
    if año != "Todos":
        resultado = resultado[resultado["AÑO"] == año]
    
    if mes != "Todos":
        resultado = resultado[resultado["MES_NUM"] == mes]

    return resultado


def preparar_analisis(df, opcion):
    if opcion == "Rentas por mes":
        datos = df.groupby("MES_NUM")["count"].sum().reindex(range(1, 13))
        datos.index = [MESES[i] for i in datos.index]
        return datos.to_frame("Rentas"), "barras"


    if opcion == "Renta por hora":
        datos = df.groupby("Hora")["count"].sum()
        return datos.to_frame("Rentas"), "linea"

    if opcion == "Rentas por estación":
        orden = ["Primavera", "Verano", "Otoño", "Invierno"]
        datos = df.groupby("ESTACION_NUM")["count"].sum().reindex(orden)
        return datos.to_frame("Rentas"), "barras"

    if opcion == "Rentas por clima":
        orden = ["Despejado", "Nublado", "Lluvia o nieve ligera", "Clima severo"]
        datos = df.groupby("CLIMA_NUM")["count"].sum().reindex(orden).dropna()
        return datos.to_frame("Rentas"), "barras"

    if opcion == "Rentas por día":
        datos = df.groupby("DIA_NUM")["count"].sum().reindex(range(7))
        return datos.to_frame("Rentas"), "barras"