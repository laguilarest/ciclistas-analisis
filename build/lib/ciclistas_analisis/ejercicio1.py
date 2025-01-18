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
    except Exception as e:
        print(f"Error inesperado: {e}")
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