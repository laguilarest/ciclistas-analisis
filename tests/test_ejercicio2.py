import pytest
import pandas as pd
from src.ejercicio2 import name_surname, eliminar_no_participantes

def test_name_surname():
    # Crea un DataFrame de ejemplo
    df = pd.DataFrame({"biker": ["John Doe", "Jane Doe"]})
    
    # Llama a la función
    df_anonimizado = name_surname(df)
    
    # Verifica que los nombres han sido cambiados
    assert not df_anonimizado["biker"].equals(df["biker"])

def test_eliminar_no_participantes():
    # Crea un DataFrame con tiempos
    data = {"time": ["00:00:00", "01:00:00", "00:30:00"]}
    df = pd.DataFrame(data)
    
    # Llama a la función
    df_filtrado = eliminar_no_participantes(df)
    
    # Verifica que solo queden las filas con tiempo distinto de "00:00:00"
    assert df_filtrado.shape[0] == 2
    assert "00:00:00" not in df_filtrado["time"].values
