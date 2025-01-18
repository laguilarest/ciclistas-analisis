
import re
import pandas as pd

def clean_club(club):
    """
    Limpia el nombre del club ciclista siguiendo las reglas especificadas.

    Parameters:
        club (str): Nombre del club a limpiar.

    Returns:
        str: Nombre limpio del club.
    """
    if pd.isnull(club):  # Manejar valores nulos
        return "INDEPENDIENTE"

    # Convertir el nombre del club a mayúsculas
    club = club.upper()

    # Reemplazar valores por nada
    replace_values = [
        'PEÑA CICLISTA ', 'PENYA CICLISTA ', 'AGRUPACIÓN CICLISTA ', 'AGRUPACION CICLISTA ',
        'AGRUPACIÓ CICLISTA ', 'AGRUPACIO CICLISTA ', 'CLUB CICLISTA ', 'CLUB '
    ]
    for value in replace_values:
        club = club.replace(value, '')

    # Reemplazar valores al inicio con expresiones regulares
    replace_start = [
        'C.C. ', 'C.C ', 'CC ', 'C.D. ', 'C.D ', 'CD ', 'A.C. ', 'A.C ', 'AC ',
        'A.D. ', 'A.D ', 'AD ', 'A.E. ', 'A.E ', 'AE ', 'E.C. ', 'E.C ', 'EC ',
        'S.C. ', 'S.C ', 'SC ', 'S.D. ', 'S.D ', 'SD '
    ]
    for pattern in replace_start:
        club = re.sub(f'^{pattern}', '', club)

    # Reemplazar valores al final con expresiones regulares
    replace_end = [
        ' T.T.', ' T.T', ' TT', ' T.E.', ' T.E', ' TE', ' C.C.', ' C.C', ' CC',
        ' C.D.', ' C.D', ' CD', ' A.D.', ' A.D', ' AD', ' A.C.', ' A.C', ' AC'
    ]
    for pattern in replace_end:
        club = re.sub(f'{pattern}$', '', club)

    # Eliminar espacios en blanco al principio y al final
    club = club.strip()

    return club

def agrupar_clubes(df):
    """
    Limpia los nombres de los clubes y agrupa los datos por clubes ciclistas.

    Parameters:
        df (pd.DataFrame): DataFrame con los datos de los ciclistas.

    Returns:
        tuple: DataFrame con los nombres limpios y DataFrame agrupado por clubes con el conteo de ciclistas.
    """
    df_copy = df.copy()  # Trabaja con una copia para evitar modificar el original
    df_copy['club_clean'] = df_copy['club'].apply(clean_club)

    # Agrupar por 'club_clean' y contar los ciclistas
    df_clubs = df_copy.groupby('club_clean').size().reset_index(name='num_ciclistas')

    # Ordenar por número de ciclistas en orden descendente
    df_clubs = df_clubs.sort_values(by='num_ciclistas', ascending=False)
    return df_copy, df_clubs