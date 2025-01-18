"""
Módulo para cargar un dataset y realizar un análisis exploratorio básico.

Contiene las funciones:
- importar_dataset: carga un dataset desde un archivo CSV.
- mostrar_eda: realiza un análisis exploratorio del dataset.
"""

import pandas as pd

def importar_dataset(filepath):
    """
    Importa el dataset desde la ruta proporcionada y lo carga en un DataFrame.

    Parameters:
        filepath (str): Nombre del archivo CSV del dataset.

    Returns:
        pd.DataFrame: DataFrame con los datos del archivo o None si ocurre un error.
    """
    try:
        print(f"Intentando cargar el archivo: {filepath}")
        # Especificar el delimitador correcto y la codificación
        df = pd.read_csv(filepath, delimiter=";", encoding="latin1")
        print("Dataset importado correctamente.")
        return df
    except FileNotFoundError:
        print(f"Error: El archivo {filepath} no se encuentra en el directorio actual.")
    except pd.errors.EmptyDataError:
        print("Error: El archivo está vacío o tiene un formato incorrecto.")
    except UnicodeDecodeError:
        print("Error: Problema de codificación en el archivo.")
    except ValueError:
        print("Error: Problema de valores en el archivo.")

    return None


def mostrar_eda(df):
    """
    Realiza un análisis exploratorio básico del dataset:
    - Muestra los primeros 5 valores.
    - Cuenta el número de ciclistas.
    - Lista las columnas disponibles.

    Parameters:
        df (pd.DataFrame): DataFrame con los datos.
    """
    if df is not None:
        # Mostrar los primeros 5 valores
        print("\nPrimeros 5 valores del dataset:")
        print(df.head())  # Usar print() en lugar de display() para scripts

        # Número total de ciclistas
        num_ciclistas = df.shape[0]
        print(f"\nEl número total de ciclistas que participaron es: {num_ciclistas}")

        # Listar las columnas disponibles
        columnas = list(df.columns)
        print("\nColumnas disponibles en el dataset:")
        for col in columnas:
            print(f"- {col}")
    else:
        print("El dataset no está cargado.")


if __name__ == "__main__":
    # Ruta al archivo de datos
    filepath = "data/dataset.csv"

    # Ejecutar las funciones del ejercicio
    print("\n--- Ejecutando Ejercicio 1 ---")
    df = importar_dataset(filepath)
    mostrar_eda(df)
