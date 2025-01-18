import pytest
import pandas as pd
from src.ejercicio1 import importar_dataset

def test_importar_dataset_correcto():
    # Crea un archivo CSV temporal
    data = "dorsal;biker;club;time\n1;Juan Pérez;Club A;00:45:00\n2;Ana López;Club B;01:15:00"
    with open("test_dataset.csv", "w") as f:
        f.write(data)
    
    # Llama a la función
    df = importar_dataset("test_dataset.csv")
    
    # Verifica que el resultado sea un DataFrame
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 4)  # Debe tener 2 filas y 4 columnas
    assert list(df.columns) == ["dorsal", "biker", "club", "time"]

def test_importar_dataset_archivo_no_encontrado():
    # Verifica que retorna None si el archivo no existe
    df = importar_dataset("archivo_inexistente.csv")
    assert df is None
