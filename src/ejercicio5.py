"""
Módulo para realizar análisis y cálculos sobre ciclistas y sus clubes.

Funciones incluidas:
- filtrar_ciclistas_por_club: Filtra ciclistas que pertenecen a un club específico.
- mejor_ciclista_en_club: Encuentra el ciclista con el mejor tiempo en un club.
- calcular_posicion_y_porcentaje: Calcula la posición de un ciclista y su porcentaje relativo.
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


def clean_club(club):
    """
    Limpia el nombre del club ciclista siguiendo las reglas especificadas.

    Parameters:
        club (str): Nombre del club a limpiar.

    Returns:
        str: Nombre limpio del club.
    """
    if pd.isnull(club):
        return "INDEPENDIENTE"
    club = club.upper()
    replacements = ['PEÑA CICLISTA ', 'CLUB CICLISTA ', 'CLUB ']
    for rep in replacements:
        club = club.replace(rep, "")
    return club.strip()


def filtrar_ciclistas_por_club(df, club):
    """
    Filtra los ciclistas que pertenecen a un club específico.

    Parameters:
        df (pd.DataFrame): DataFrame con los datos de los ciclistas.
        club (str): Nombre limpio del club para filtrar.

    Returns:
        pd.DataFrame: DataFrame con los ciclistas que pertenecen al club.
    """
    return df[df['club_clean'] == club]


def mejor_ciclista_en_club(df_club):
    """
    Encuentra el ciclista con el mejor tiempo en un club.

    Parameters:
        df_club (pd.DataFrame): DataFrame con los ciclistas de un club.

    Returns:
        pd.Series: Fila del ciclista con el mejor tiempo.
    """
    return df_club.loc[df_club['time'].idxmin()]


def calcular_posicion_y_porcentaje(df, dorsal):
    """
    Calcula la posición de un ciclista en el DataFrame ordenado por tiempo
    y su porcentaje relativo respecto al total de ciclistas.

    Parameters:
        df (pd.DataFrame): DataFrame con los datos de los ciclistas.
        dorsal (int): Dorsal del ciclista.

    Returns:
        tuple: (posición del ciclista, porcentaje sobre el total).
    """
    df_ordenado = df.sort_values(by='time').reset_index(drop=True)
    posicion = df_ordenado[df_ordenado['dorsal'] == dorsal].index[0] + 1
    porcentaje = (posicion / len(df)) * 100
    return posicion, porcentaje


if __name__ == "__main__":
    # Ruta del dataset
    filepath = "data/dataset.csv"

    # Importar el dataset
    print("\n--- Importar Dataset ---")
    df = importar_dataset(filepath)

    if df is not None:
        # Eliminar ciclistas con tiempo '00:00:00'
        print("\n--- Eliminar ciclistas con tiempo '00:00:00' ---")
        df = eliminar_no_participantes(df)

        # Limpiar nombres de clubes
        print("\n--- Limpiar nombres de clubes ---")
        df['club_clean'] = df['club'].apply(clean_club)

        # Filtrar ciclistas de la UCSC
        print("\n--- Filtrar ciclistas de la UCSC ---")
        ciclistas_ucsc = filtrar_ciclistas_por_club(df, "UCSC")
        print(f"Total de ciclistas en UCSC: {len(ciclistas_ucsc)}")
        print(ciclistas_ucsc)


        # Encontrar el ciclista con el mejor tiempo en la UCSC
        print("\n--- Mejor ciclista en la UCSC ---")
        if not ciclistas_ucsc.empty:
            mejor_ciclista = mejor_ciclista_en_club(ciclistas_ucsc)
            print(mejor_ciclista)

            # Calcular posición y porcentaje del ciclista
            posicion, porcentaje = calcular_posicion_y_porcentaje(df, mejor_ciclista['dorsal'])
            print(f"Posición del ciclista: {posicion}")
            print(f"Porcentaje respecto al total: {porcentaje:.2f}%")
        else:
            print("No hay ciclistas en la UCSC.")
    else:
        print("No se pudo cargar el dataset.")
