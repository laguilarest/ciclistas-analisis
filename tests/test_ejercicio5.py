import pytest
import pandas as pd
from src.ejercicio5 import filtrar_ciclistas_por_club, mejor_ciclista_en_club, calcular_posicion_y_porcentaje

def test_filtrar_ciclistas_por_club():
    # Crea un DataFrame de ejemplo
    data = {"club_clean": ["UCSC", "Otro", "UCSC"]}
    df = pd.DataFrame(data)
    
    # Llama a la función
    df_filtered = filtrar_ciclistas_por_club(df, "UCSC")
    
    # Verifica los resultados
    assert df_filtered.shape[0] == 2

def test_mejor_ciclista_en_club():
    # Crea un DataFrame de ejemplo
    data = {"time": ["00:30:00", "00:25:00"]}
    df = pd.DataFrame(data)
    
    # Llama a la función
    mejor_ciclista = mejor_ciclista_en_club(df)
    
    # Verifica los resultados
    assert mejor_ciclista["time"] == "00:25:00"

def test_calcular_posicion_y_porcentaje():
    # Crea un DataFrame de ejemplo
    data = {"dorsal": [1, 2, 3], "time": ["00:45:00", "00:30:00", "00:15:00"]}
    df = pd.DataFrame(data)
    
    # Llama a la función
    posicion, porcentaje = calcular_posicion_y_porcentaje(df, 2)
    
    # Verifica los resultados
    assert posicion == 2
    assert porcentaje == pytest.approx(66.67, rel=1e-2)  # Tolerancia relativa del 1%
