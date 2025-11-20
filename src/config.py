"""
Configuración del proyecto
==========================

Este módulo contiene todas las configuraciones de rutas, parámetros
y constantes utilizadas en el análisis.
"""

from pathlib import Path

# Rutas del proyecto
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"
PLOTS_DIR = PROJECT_ROOT / "plots"

# Crear directorios si no existen
DATA_DIR.mkdir(exist_ok=True)
PLOTS_DIR.mkdir(exist_ok=True)

# Diccionario de rutas comunes
PATHS = {
    "root": PROJECT_ROOT,
    "data": DATA_DIR,
    "notebooks": NOTEBOOKS_DIR,
    "plots": PLOTS_DIR,
}

# Configuración de figuras y visualizaciones
FIGURES_CONFIG = {
    "default_figsize": (20, 15),
    "map_figsize": (20, 10),
    "scatter_figsize": (8, 6),
    "dpi": 300,
    "style": "white",
}

# Configuración de pandas display
PANDAS_CONFIG = {
    "display.max_rows": 500,
    "display.max_columns": 500,
    "display.width": 1000,
}

# Parámetros del análisis espacial
SPATIAL_PARAMS = {
    "knn_neighbors": 45,  # Número de vecinos más cercanos
    "price_outlier_threshold": 4000,  # Threshold para outliers de precio
    "moran_permutations": 999,  # Número de permutaciones para test de Moran
    "significance_level": 0.05,  # Nivel de significancia
}

# Colores para visualizaciones
COLORS = {
    "airbnb_red": "#FF5A5F",
    "airbnb_dark": "#FC642D",
    "moran_quadrants": {
        "not_significant": "lightgrey",
        "high_high": "red",
        "low_low": "blue",
        "high_low": "salmon",
        "low_high": "cornflowerblue",
    },
}

# Encoding por defecto para CSVs
DEFAULT_ENCODING = "utf-8"  # Cambiado de latin1 a utf-8 para mejor compatibilidad

# Lista de alcaldías de CDMX
ALCALDIAS = [
    "Cuauhtémoc",
    "Cuajimalpa de Morelos",
    "Coyoacán",
    "Miguel Hidalgo",
    "Benito Juárez",
    "Iztacalco",
    "Tlalpan",
    "Azcapotzalco",
    "Iztapalapa",
    "La Magdalena Contreras",
    "Venustiano Carranza",
    "Álvaro Obregón",
    "Gustavo A. Madero",
    "Xochimilco",
    "Tláhuac",
    "Milpa Alta",
]
