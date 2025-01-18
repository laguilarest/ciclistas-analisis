"""
Módulo para anonimizar y filtrar datos de ciclistas en un dataset.

Funciones incluidas:
- name_surname: Anonimiza los nombres de los ciclistas.
- eliminar_no_participantes: Filtra ciclistas con tiempo '00:00:00'.
- recuperar_dorsal: Recupera los datos de un ciclista por su dorsal.
"""

import pandas as pd
from faker import Faker


def importar_dataset(filepath):
    """
    Importa el dataset desde la ruta proporcionada y lo carga en un DataFrame.

    Parameters:
        filepath (str): Nombre del archivo CSV del dataset.

    Returns:
        pd.DataFrame: DataFrame con los datos del archivo o None si ocurre un error.
    """
    try:
        df = pd.read_csv(filepath, delimiter=";", encoding="latin1")
        return df
    except Exception as e:
        print(f"Error al importar el dataset: {e}")
        return None


def name_surname(df):
    """
    Anonimiza los nombres de los ciclistas en el dataset utilizando Faker.

    Parameters:
        df (pd.DataFrame): DataFrame con los datos de los ciclistas.

    Returns:
        pd.DataFrame: DataFrame con los nombres anonimizados.
    """
    fake = Faker()
    Faker.seed(42)
    df_copy = df.copy()
    df_copy['biker'] = [fake.name() for _ in range(len(df_copy))]
    return df_copy


def eliminar_no_participantes(df):
    """
    Elimina del dataset los ciclistas con tiempo '00:00:00', indicando que no participaron.

    Parameters:
        df (pd.DataFrame): DataFrame con los datos de los ciclistas.

    Returns:
        pd.DataFrame: DataFrame filtrado, sin los ciclistas que no participaron.
    """
    return df[df['time'] != "00:00:00"]


def recuperar_dorsal(df, dorsal):
    """
    Recupera los datos del ciclista con un dorsal específico.

    Parameters:
        df (pd.DataFrame): DataFrame con los datos de los ciclistas.
        dorsal (int): Número del dorsal del ciclista a buscar.

    Returns:
        pd.DataFrame: DataFrame con los datos del ciclista (vacío si no se encuentra).
    """
    return df[df['dorsal'] == dorsal]


if __name__ == "__main__":
    # Ruta del dataset
    filepath = "data/dataset.csv"

    # Importar dataset
    print("\n--- Importar Dataset ---")
    df = importar_dataset(filepath)

    # Ejecución de las funciones del ejercicio 2
    print("\n--- Anonimizar nombres de los ciclistas ---")
    df = name_surname(df)
    print(df.head())

    print("\n--- Eliminar ciclistas que no participaron ---")
    df = eliminar_no_participantes(df)
    print(df.head())

    print("\n--- Recuperar ciclista con dorsal 1000 ---")
    ciclista_1000 = recuperar_dorsal(df, 1000)
    if not ciclista_1000.empty:
        print(ciclista_1000)
    else:
        print("No se encontró ningún ciclista con dorsal 1000.")
