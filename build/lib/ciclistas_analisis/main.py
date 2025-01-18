import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.ejercicio1 import importar_dataset, mostrar_eda
from src.ejercicio2 import name_surname, eliminar_no_participantes, recuperar_dorsal
from src.ejercicio3 import agrupar_tiempos, generar_histograma
from src.ejercicio4 import agrupar_clubes
from src.ejercicio5 import filtrar_ciclistas_por_club, mejor_ciclista_en_club, calcular_posicion_y_porcentaje

def main():
    # Ejercicio 1: Importar Dataset
    filepath = "data/dataset.csv"
    print("\n--- Ejercicio 1: Importar Dataset ---")
    df = importar_dataset(filepath)

    # Mostrar análisis exploratorio
    print("\n--- Ejercicio 1: Mostrar Análisis Exploratorio (EDA) ---")
    mostrar_eda(df)

    # Ejercicio 2: Anonimizar y limpiar datos
    print("\n--- Ejercicio 2: Anonimizar Nombres y Limpiar Dataset ---")
    df = name_surname(df)
    print("Nombres anonimizados. Los 5 primeros ciclistas son:")
    print(df.head())

    df = eliminar_no_participantes(df)
    print(f"Después de limpiar el dataset, tenemos {df.shape[0]} ciclistas.")
    print("Primeros 5 ciclistas tras la limpieza:")
    print(df.head())

    # Recuperar datos del ciclista con dorsal 1000
    print("\n--- Ejercicio 2: Recuperar Datos del Ciclista con Dorsal 1000 ---")
    ciclista_1000 = recuperar_dorsal(df, 1000)
    if not ciclista_1000.empty:
        print("Datos del ciclista con dorsal 1000:")
        print(ciclista_1000)
    else:
        print("No se encontró ningún ciclista con dorsal 1000.")

    # Ejercicio 3: Agrupar Tiempos y Generar Histograma
    print("\n--- Ejercicio 3: Agrupar Tiempos y Generar Histograma ---")
    df_grouped = agrupar_tiempos(df)
    print("Datos agrupados por franjas de tiempo:")
    print(df_grouped)

    generar_histograma(df_grouped, output_path='img/histograma.png')

    # Ejercicio 4: Agrupar y Ordenar Clubs
    print("\n--- Ejercicio 4: Agrupar y Ordenar Clubs Ciclistas ---")
    df_clean, df_clubs = agrupar_clubes(df)

    print("Primeros 15 valores con la columna 'club_clean':")
    print(df_clean[['club', 'club_clean']].head(15))

    print("Datos agrupados por clubs ciclistas:")
    print(df_clubs.head(15))

    # Ejercicio 5: Mejor Ciclista de la UCSC
    print("\n--- Ejercicio 5: Mejor Ciclista de la UCSC ---")
    ciclistas_ucsc = filtrar_ciclistas_por_club(df_clean, 'UCSC')
    print(f"Total de ciclistas en UCSC: {len(ciclistas_ucsc)}")
    print("Ciclistas de la UCSC:")
    print(ciclistas_ucsc)

    ciclista_mejor_tiempo = mejor_ciclista_en_club(ciclistas_ucsc)
    print("Ciclista de la UCSC con el mejor tiempo:")
    print(ciclista_mejor_tiempo)

    posicion, porcentaje = calcular_posicion_y_porcentaje(df_clean, ciclista_mejor_tiempo['dorsal'])
    print(f"Posición del ciclista de la UCSC con el mejor tiempo: {posicion}")
    print(f"Porcentaje sobre el total: {porcentaje:.2f}%")

if __name__ == "__main__":
    main()