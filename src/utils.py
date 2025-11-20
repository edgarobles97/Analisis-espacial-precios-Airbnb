"""
Utilidades para análisis espacial de Airbnb
==========================================

Este módulo contiene funciones reutilizables para el análisis espacial
de precios de Airbnb en la Ciudad de México.
"""

from math import radians, cos, sin, asin, sqrt
from typing import Dict, Tuple, Optional
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd
from shapely.geometry import Point

from .config import PANDAS_CONFIG, FIGURES_CONFIG, DEFAULT_ENCODING


def haversine(row: pd.Series) -> float:
    """
    Calcula la distancia haversine entre dos puntos de la Tierra.

    La fórmula de haversine calcula la distancia de círculo máximo entre
    dos puntos en una esfera dadas sus longitudes y latitudes.

    Parameters
    ----------
    row : pd.Series
        Serie de pandas con las columnas:
        - longitude: longitud del primer punto
        - latitude: latitud del primer punto
        - longitude_2: longitud del segundo punto
        - latitude_2: latitud del segundo punto

    Returns
    -------
    float
        Distancia en kilómetros entre los dos puntos

    Examples
    --------
    >>> df['distance'] = df.apply(haversine, axis=1)
    """
    lon1 = row["longitude"]
    lat1 = row["latitude"]
    lon2 = row["longitude_2"]
    lat2 = row["latitude_2"]

    # Convertir grados decimales a radianes
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # Fórmula haversine
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))

    # Radio de la Tierra en kilómetros
    km = 6367 * c
    return km


def multi_collinearity_heatmap(
    df: pd.DataFrame,
    figsize: Tuple[int, int] = (11, 9),
    save_path: Optional[str] = None
) -> None:
    """
    Genera un mapa de calor de correlación para detectar multicolinealidad.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame con las variables numéricas a analizar
    figsize : Tuple[int, int], optional
        Tamaño de la figura (ancho, alto), por defecto (11, 9)
    save_path : str, optional
        Ruta para guardar la figura. Si es None, no se guarda

    Returns
    -------
    None
        Muestra el heatmap pero no retorna nada

    Examples
    --------
    >>> multi_collinearity_heatmap(df[['precio', 'bedrooms', 'bathrooms']])
    """
    # Establecer estilo
    sns.set(style="white")

    # Matriz de correlación
    corr = df.corr()

    # Crear máscara para el triángulo superior
    mask = np.zeros_like(corr, dtype=bool)
    mask[np.triu_indices_from(mask)] = True

    # Configurar figura
    f, ax = plt.subplots(figsize=figsize)

    # Generar paleta de colores divergente
    cmap = sns.diverging_palette(220, 10, as_cmap=True)

    # Generar heatmap
    sns.heatmap(
        corr,
        mask=mask,
        cmap=cmap,
        center=0,
        square=True,
        linewidths=0.5,
        cbar_kws={"shrink": 0.5},
        vmax=corr[corr != 1.0].max().max(),
    )

    if save_path:
        plt.savefig(save_path, dpi=FIGURES_CONFIG["dpi"], bbox_inches="tight")

    plt.show()


def plot_moran_scatter(
    moran_obj,
    ln_price: pd.Series,
    lag_lnprice: pd.Series,
    local_moran_obj,
    save_path: Optional[str] = None
) -> None:
    """
    Genera el gráfico de dispersión de Índice I de Moran.

    Parameters
    ----------
    moran_obj : pysal.explore.esda.moran.Moran
        Objeto de Moran global
    ln_price : pd.Series
        Serie con logaritmo natural de precios
    lag_lnprice : pd.Series
        Serie con el lag espacial de precios
    local_moran_obj : pysal.explore.esda.moran.Moran_Local
        Objeto de Moran local
    save_path : str, optional
        Ruta para guardar la figura

    Returns
    -------
    None
    """
    # Filtrar valores significativos
    quadfilter = (local_moran_obj.p_sim <= 0.05) * local_moran_obj.q
    quadrantcolor = np.array(
        ["lightgrey", "red", "cornflowerblue", "blue", "salmon"]
    )[quadfilter]

    plt.figure(figsize=FIGURES_CONFIG["scatter_figsize"])

    sns.regplot(
        x=ln_price,
        y=lag_lnprice,
        line_kws=dict(color="r"),
        scatter_kws=dict(c=quadrantcolor, marker=".", s=5, color=None),
        ci=None,
    )

    # Líneas de referencia
    plt.vlines(
        ln_price.mean(), *plt.gca().get_ylim(), color="k", linestyle="--"
    )
    plt.hlines(
        lag_lnprice.mean(), *plt.gca().get_xlim(), color="k", linestyle="--"
    )

    # Anotaciones
    plt.text(
        s=f"$I = {moran_obj.I:.3f}$",
        x=11,
        y=6,
        fontsize=14,
    )
    plt.text(
        s=f"$p= {moran_obj.p_sim:.3f}$",
        x=11,
        y=5.8,
        fontsize=14,
    )

    plt.ylabel("Wln_price")
    plt.title("Gráfico de dispersión de Índice I de Moran", fontsize=20)

    sns.despine()

    if save_path:
        plt.savefig(save_path, dpi=FIGURES_CONFIG["dpi"], bbox_inches="tight")

    plt.show()


def load_airbnb_data(
    filepath: str,
    encoding: str = DEFAULT_ENCODING,
    **kwargs
) -> pd.DataFrame:
    """
    Carga datos de Airbnb con configuración estándar.

    Parameters
    ----------
    filepath : str
        Ruta al archivo CSV
    encoding : str, optional
        Encoding del archivo, por defecto usa DEFAULT_ENCODING
    **kwargs
        Argumentos adicionales para pd.read_csv

    Returns
    -------
    pd.DataFrame
        DataFrame con los datos cargados
    """
    try:
        df = pd.read_csv(filepath, encoding=encoding, low_memory=False, **kwargs)
        return df
    except UnicodeDecodeError:
        # Fallback a latin1 si UTF-8 falla
        print(f"Warning: UTF-8 falló, intentando con latin1...")
        df = pd.read_csv(filepath, encoding="latin1", low_memory=False, **kwargs)
        return df


def setup_geopandas(
    df: pd.DataFrame,
    lon_col: str = "longitude",
    lat_col: str = "latitude"
) -> gpd.GeoDataFrame:
    """
    Convierte un DataFrame a GeoDataFrame con geometría de puntos.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame con coordenadas
    lon_col : str, optional
        Nombre de la columna de longitud, por defecto "longitude"
    lat_col : str, optional
        Nombre de la columna de latitud, por defecto "latitude"

    Returns
    -------
    gpd.GeoDataFrame
        GeoDataFrame con columna geometry
    """
    df["geometry"] = list(zip(df[lon_col], df[lat_col]))
    df["geometry"] = df["geometry"].apply(Point)
    geo_df = gpd.GeoDataFrame(df, geometry="geometry")
    return geo_df


def configure_pandas_display() -> None:
    """
    Configura las opciones de display de pandas según PANDAS_CONFIG.

    Returns
    -------
    None
    """
    for key, value in PANDAS_CONFIG.items():
        pd.set_option(key, value)


def filter_outliers(
    df: pd.DataFrame,
    column: str,
    threshold: float
) -> pd.DataFrame:
    """
    Filtra outliers basado en un threshold.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame a filtrar
    column : str
        Nombre de la columna a filtrar
    threshold : float
        Valor threshold para filtrar

    Returns
    -------
    pd.DataFrame
        DataFrame filtrado
    """
    filtered_df = df[df[column] < threshold].copy()
    n_removed = len(df) - len(filtered_df)
    print(f"Outliers removidos: {n_removed} ({n_removed/len(df)*100:.2f}%)")
    return filtered_df


def create_distance_index(
    df: pd.DataFrame,
    points_of_interest: pd.DataFrame,
    id_col: str = "id"
) -> pd.Series:
    """
    Calcula índice de distancia inversa a puntos de interés.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame con listados de Airbnb
    points_of_interest : pd.DataFrame
        DataFrame con puntos de interés
    id_col : str, optional
        Nombre de la columna ID, por defecto "id"

    Returns
    -------
    pd.Series
        Serie con el índice de proximidad por listing
    """
    # Crear key para merge cartesiano
    df_copy = df.copy()
    poi_copy = points_of_interest.copy()

    df_copy["key"] = 1
    poi_copy["key"] = 1

    # Merge
    merged = df_copy.merge(poi_copy, on="key", how="outer")

    # Calcular distancias
    merged["distance"] = merged.apply(haversine, axis=1)
    merged["inv_distance"] = merged["distance"] ** -1

    # Agrupar y sumar distancias inversas
    distance_index = merged.groupby(id_col)["inv_distance"].sum()

    return distance_index


def get_nearest_station(
    df: pd.DataFrame,
    stations: pd.DataFrame,
    id_col: str = "id",
    distance_col: str = "distance"
) -> pd.DataFrame:
    """
    Encuentra la estación más cercana para cada listado.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame con listados
    stations : pd.DataFrame
        DataFrame con estaciones
    id_col : str, optional
        Nombre columna ID
    distance_col : str, optional
        Nombre para columna de distancia

    Returns
    -------
    pd.DataFrame
        DataFrame con estación más cercana por listing
    """
    df_copy = df.copy()
    stations_copy = stations.copy()

    df_copy["key"] = 1
    stations_copy["key"] = 1

    merged = df_copy.merge(stations_copy, on="key", how="outer")
    merged[distance_col] = merged.apply(haversine, axis=1)

    # Obtener mínimo por grupo
    nearest = merged.loc[merged.groupby(id_col)[distance_col].idxmin()]

    return nearest
