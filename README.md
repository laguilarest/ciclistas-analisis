Ciclistas Análisis

Este proyecto contiene herramientas para analizar datos de ciclistas que participaron en la competición de Orbea Monegros. Incluye funcionalidades para importar, limpiar y analizar datos, además de generar visualizaciones útiles para explorar las características del dataset.

Características Principales
	Importar y Explorar Datos
		Carga y visualiza un dataset con detalles de los ciclistas.
		Realiza un análisis exploratorio inicial.
	Anonimización y Limpieza
		Anonimiza los nombres de los ciclistas utilizando la librería Faker.
		Elimina registros de ciclistas que no participaron (tiempo igual a 00:00:00).
	Agrupación de Datos
		Agrupa tiempos en franjas de 20 minutos y genera histogramas.
		Limpia y agrupa datos de clubes ciclistas.
	Análisis Personalizado
		Identifica el ciclista con el mejor tiempo dentro de un club específico.
		Calcula la posición de un ciclista y su porcentaje relativo en el dataset.

Requisitos Previos
	Asegúrate de tener instalado:
		Python 3.8 o superior

	Librerías necesarias incluidas en el archivo requirements.txt
		Para instalarlas, ejecuta:
		pip install -r requirements.txt

Estructura del Proyecto

ciclistas-analisis/
├── data/                    # Carpeta con el dataset
│   └── dataset.csv          # Archivo de datos de entrada
├── dist/                    # Paquete generado para distribución
│   └── ciclistas_analisis-1.0.0.tar.gz
├── img/                     # Carpeta para gráficos generados
│   └── histograma.png       # Histograma generado por el proyecto
├── src/                     # Código fuente del proyecto
│   ├── ejercicio1.py        # Importación y EDA
│   ├── ejercicio2.py        # Anonimización y limpieza
│   ├── ejercicio3.py        # Agrupación de tiempos y visualización
│   ├── ejercicio4.py        # Agrupación de clubes
│   ├── ejercicio5.py        # Análisis de ciclistas en clubes
│   ├── main.py              # Módulo principal
│   └── __init__.py          # Inicialización del paquete
├── tests/                   # Pruebas unitarias y funcionales
│   ├── test_ejercicio1.py   # Tests para ejercicio 1
│   ├── test_ejercicio2.py   # Tests para ejercicio 2
│   ├── test_ejercicio3.py   # Tests para ejercicio 3
│   ├── test_ejercicio4.py   # Tests para ejercicio 4
│   ├── test_ejercicio5.py   # Tests para ejercicio 5
│   └── __init__.py          # Inicialización de pruebas
├── requirements.txt         # Dependencias del proyecto
├── setup.py                 # Configuración del paquete
├── LICENSE.txt              # Licencia del proyecto
└── README.md                # Archivo de documentación


El proyecto debe estar en una carpeta llamada ciclistas-analisis. Si ya tiene la carpeta en su equipo, simplemente acceda a ella desde la terminal:

	cd "ruta/donde/esta/ciclistas-análisis"

Si prefiere descargar el proyecto desde GitHub, puede hacerlo con este comando:

	git clone https://github.com/laguilarest/ciclistas-analisis.git
	cd "ciclistas-analisis"

El proyecto utiliza varias librerías de Python que deben instalarse. Esto puede hacerse de dos maneras:

Usando requirements.txt

	Ejecute el siguiente comando desde la raíz del proyecto para instalar las dependencias necesarias:

		pip install -r requirements.txt
	
Usando setup.py

	Alternativamente, puedes instalar el proyecto como un paquete de Python utilizando setup.py. Esto también instala automáticamente las dependencias.

	Desde la raíz del proyecto, ejecuta:

		python setup.py install

	Esto instala el proyecto como un paquete llamado ciclistas_analisis

Para ejecutar todo el flujo del proyecto de principio a fin, usa el archivo principal main.py:

	python src/main.py

Este comando ejecuta todos los ejercicios en orden y genera salidas en la terminal, además de guardar el histograma en img/histograma.png.

Cada módulo del proyecto está diseñado para ejecutarse por separado. Para ejecutar un ejercicio específico, se puede probar desde la terminal del dispositivo.

Por ejemplo, para probar el ejercicio 1:

	python src/ejercicio1.py

Ejercicio 2:

	python src/ejercicio2.py

Ejercicio 3:

	python src/ejercicio3.py

Ejercicio 4:

	python src/ejercicio4.py

Ejercicio 5:

	python src/ejercicio5.py

EL siguiente paso será ejecutar los test de manera similar. Podremos ejecutarlos todos a la vez utilizando:

	pytest

En caso de querer ejecutarlo uno a uno se hará de esta manera con cada ejercicio:

	pytest tests/test_ejercicio1.py
	pytest tests/test_ejercicio2.py
	pytest tests/test_ejercicio3.py
	pytest tests/test_ejercicio4.py
	pytest tests/test_ejercicio5.py

Pylint es una herramienta para analizar y garantizar que el código cumple con el estándar PEP 8. Al ejecutar Pylint en el archivo main.py, podremoss identificar errores, advertencias y mejores prácticas para mejorar la calidad del código en caso de que los hubiera.

Si aún no lo tenemos instalado, se puede instalar con el siguiente comando en la terminal o PowerShell:

	pip install pylint

Ejecute el siguiente comando en la terminal desde la raíz del proyecto (ciclistas_analisis):

	pylint src/main.py

Tras esto se obtiene la valoración del código según PEP8.

Este proyecto está bajo la licencia MIT. Puedes ver más detalles en el archivo LICENSE.txt.

Contacto
Juan Lucas Aguilar Esteban
Correo: laguilarest@uoc.edu