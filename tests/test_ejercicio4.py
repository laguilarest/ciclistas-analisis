import pytest
import pandas as pd
from src.ejercicio4 import clean_club, agrupar_clubes

def test_clean_club():
    # Prueba diferentes nombres de clubes
    assert clean_club("Club Ciclista A") == "A"
    assert clean_club("AGRUPACIÓN CICLISTA B") == "B"
    assert clean_club(None) == "INDEPENDIENTE"

def test_agrupar_clubes():
    # Crea un DataFrame de ejemplo
    data = {"club": ["Club A", "Club A", "Club B"]}
    df = pd.DataFrame(data)
    
    # Llama a la función
    df_clean, df_clubs = agrupar_clubes(df)
    
    # Verifica los resultados
    assert df_clubs.shape[0] == 2  # Dos clubes únicos
    assert df_clubs["num_ciclistas"].sum() == 3
