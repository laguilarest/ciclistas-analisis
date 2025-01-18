
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
    # Ordenar el DataFrame por tiempo
    df_ordenado = df.sort_values(by='time').reset_index(drop=True)

    # Encontrar la posición del ciclista
    posicion = df_ordenado[df_ordenado['dorsal'] == dorsal].index[0] + 1

    # Calcular el porcentaje
    porcentaje = (posicion / len(df)) * 100

    return posicion, porcentaje