import pandas as pd

def cargar_datos(ruta):
    return pd.read_csv(ruta, sep=";")

def transformar_fecha(df):
    df["dt"] = pd.to_datetime(df["dt"], dayfirst=True)
    df["year"] = df["dt"].dt.year
    return df

if __name__ == "__main__":
    df = cargar_datos(r"C:\Users\Lenovo\Downloads\datos_mock.csv")  # Ruta válida
    df = transformar_fecha(df)
    print(df.head())

