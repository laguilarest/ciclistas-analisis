
from faker import Faker

def name_surname(df):
    """
    Anonimiza los nombres de los ciclistas en el dataset utilizando Faker.

    Parameters:
        df (pd.DataFrame): DataFrame con los datos de los ciclistas.

    Returns:
        pd.DataFrame: DataFrame con los nombres anonimizados.
    """
    fake = Faker()
    Faker.seed(42)  # Para reproducibilidad
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