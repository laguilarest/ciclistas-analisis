
import matplotlib.pyplot as plt

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
    Agrupa los tiempos de los ciclistas en franjas de 20 minutos y genera un DataFrame con las franjas.

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