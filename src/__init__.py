"""
Análisis Espacial de Precios de Airbnb en CDMX
==============================================

Módulo de utilidades para el análisis espacial de precios de Airbnb
en la Ciudad de México.

Autor: Edgar Robles Díaz
Año: 2020 (Refactorizado: 2025)
"""

__version__ = "2.0.0"
__author__ = "Edgar Robles Díaz"

from .utils import (
    haversine,
    multi_collinearity_heatmap,
    plot_moran_scatter,
    load_airbnb_data,
    setup_geopandas,
)
from .config import PATHS, FIGURES_CONFIG

__all__ = [
    "haversine",
    "multi_collinearity_heatmap",
    "plot_moran_scatter",
    "load_airbnb_data",
    "setup_geopandas",
    "PATHS",
    "FIGURES_CONFIG",
]
