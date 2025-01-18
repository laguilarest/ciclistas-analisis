"""
Módulo para agrupar tiempos de ciclistas y generar histogramas.

Funciones incluidas:
- minutes_002040: Agrupa tiempos en franjas de 20 minutos.
- agrupar_tiempos: Agrupa tiempos en un DataFrame por franjas.
- generar_histograma: Genera un histograma de ciclistas por franja de tiempo.
"""

import pandas as pd
import matplotlib.pyplot as plt


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


def eliminar_no_participantes(df):
    """
    Elimina del dataset los ciclistas con tiempo '00:00:00', indicando que no participaron.

    Parameters:
        df (pd.DataFrame): DataFrame con los datos de los ciclistas.

    Returns:
        pd.DataFrame: DataFrame filtrado, sin los ciclistas que no participaron.
    """
    return df[df['time'] != "00:00:00"]


def minutes_002040(time_str):
    """
    Agrupa un tiempo en formato hh:mm:ss en franjas de 20 minutos.

    Parameters:
        time_str (str): Tiempo en formato 'hh:mm:ss'.

    Returns:
        str: Tiempo agrupado en formato 'hh:mm', donde los minutos solo pueden ser 00, 20 o 40.
    """
    hours, minutes, _ = map(int, time_str.split(":"))
    if minutes < 20:
        minutes_grouped = "00"
    elif minutes < 40:
        minutes_grouped = "20"
    else:
        minutes_grouped = "40"
    return f"{hours:02}:{minutes_grouped}"


def agrupar_tiempos(df):
    """
    Agrupa los tiempos de los ciclistas en franjas de 20 min y crea un DataFrame con las franjas.

    Parameters:
        df (pd.DataFrame): DataFrame con la columna 'time'.

    Returns:
        pd.DataFrame: DataFrame con la columna 'time_grouped' y el conteo por franja.
    """
    # Crear una nueva columna agrupando los tiempos
    df['time_grouped'] = df['time'].apply(minutes_002040)

    # Agrupar por 'time_grouped' y contar los ciclistas
    df_grouped = df.groupby('time_grouped').size().reset_index(name='num_ciclistas')
    return df_grouped


def generar_histograma(df_grouped, output_path='img/histograma.png'):
    """
    Genera un histograma a partir de un DataFrame agrupado por franjas de tiempo.

    Parameters:
        df_grouped (pd.DataFrame): DataFrame con columnas 'time_grouped' y 'num_ciclistas'.
        output_path (str): Ruta donde se guardará el histograma generado.
    """
    # Crear el directorio de salida si no existe
    output_dir = os.path.dirname(output_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Generar el histograma
    plt.figure(figsize=(10, 6))
    plt.bar(df_grouped['time_grouped'], df_grouped['num_ciclistas'], color='blue', alpha=0.7)
    plt.xlabel('Franja de tiempo (hh:mm)')
    plt.ylabel('Número de ciclistas')
    plt.title('Distribución de Ciclistas por Franja de Tiempo')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(rotation=45)  # Rotar las etiquetas del eje x

    # Guardar el histograma
    plt.savefig(output_path)
    plt.show()


if __name__ == "__main__":
    # Ruta del dataset
    filepath = "data/dataset.csv"

    # Importar dataset
    print("\n--- Importar Dataset ---")
    df = importar_dataset(filepath)

    if df is not None:
        # Eliminar ciclistas con tiempo '00:00:00'
        print("\n--- Eliminar ciclistas con tiempo '00:00:00' ---")
        df = eliminar_no_participantes(df)
        print(f"Después de eliminar no participantes, quedan {len(df)} ciclistas.")

        # Agrupar los tiempos en franjas de 20 minutos
        print("\n--- Agrupar tiempos por franjas de 20 minutos ---")
        df_grouped = agrupar_tiempos(df)
        print(df_grouped)

        # Generar el histograma
        print("\n--- Generar Histograma ---")
        generar_histograma(df_grouped)
    else:
        print("No se pudo cargar el dataset.")
