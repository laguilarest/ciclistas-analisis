from setuptools import setup, find_packages

setup(
    name="ciclistas_analisis",  # Nombre del paquete
    version="1.0.0",  # Versión inicial
    description="Este proyecto contiene herramientas para analizar datos de ciclistas en la competición de Orbea Monegros.",  # Breve descripción
    author="Jose Vicente",  # Nombre
    author_email="laguilarest@uoc.edu",  # Correo
    url="https://github.com/laguilarest/ciclistas-analisis",  # URL del repositorio 
    packages=find_packages(where="src"),  # Busca paquetes en la carpeta src/
    package_dir={"": "src"},  # Indica que las carpetas de los paquetes están en src/
    install_requires=[
        "pandas>=1.0",  # Dependencias necesarias
        "matplotlib>=3.0",
        "faker>=13.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Licencia del paquete
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",  # Versión mínima de Python
)
