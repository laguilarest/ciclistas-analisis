import pytest
import pandas as pd
from src.ejercicio3 import minutes_002040, agrupar_tiempos

def test_minutes_002040():
    # Prueba con diferentes tiempos
    assert minutes_002040("00:15:00") == "00:00"
    assert minutes_002040("00:25:00") == "00:20"
    assert minutes_002040("00:50:00") == "00:40"

def test_agrupar_tiempos():
    # Crea un DataFrame de ejemplo
    data = {"time": ["00:15:00", "00:25:00", "00:50:00"]}
    df = pd.DataFrame(data)
    
    # Llama a la función
    df_grouped = agrupar_tiempos(df)
    
    # Verifica los resultados
    assert df_grouped.shape[0] == 3  # Tres franjas de tiempo
