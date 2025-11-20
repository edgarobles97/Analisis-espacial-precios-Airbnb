# Análisis Espacial de Precios de Airbnb en la Ciudad de México

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

> **Tesina:** "The economics behind two-sided markets: key determinants of Airbnb pricing in Mexico City"
> **Autor:** Edgar Robles Díaz
> **Año:** 2020 | **Refactorizado:** 2025

## 📋 Tabla de Contenidos

- [Descripción](#descripción)
- [Hallazgos Principales](#hallazgos-principales)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Instalación](#instalación)
- [Uso](#uso)
- [Metodología](#metodología)
- [Datos](#datos)
- [Resultados](#resultados)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)
- [Contacto](#contacto)

## 📖 Descripción

Este proyecto analiza los determinantes de precios de listados de Airbnb en la Ciudad de México mediante técnicas de análisis espacial. El estudio incorpora efectos espaciales (spillover) para comprender la dinámica de precios en la ciudad.

### Contexto

El surgimiento de la economía compartida ha tenido efectos sustanciales en diversas industrias (comercio electrónico, transportes, comunicación). En particular, la industria hotelera y de alojamiento ha experimentado disrupciones significativas. Airbnb se ha posicionado como la plataforma líder en alojamiento P2P (Peer to Peer) en diversas ciudades del mundo.

### Objetivo

Identificar y cuantificar los determinantes de los precios de los listados de Airbnb en la Ciudad de México, incorporando efectos espaciales para conocer la dinámica de precios en la ciudad.

## 🎯 Hallazgos Principales

1. **Agrupación Espacial de Precios**: Existe una alta autocorrelación espacial en los precios. Listados con precios altos se encuentran en vecindades con el mismo nivel de precios y viceversa.

2. **Características Físicas**: El número de huéspedes alojados, número de cuartos y baños tienen efectos positivos y significativos en el precio.

3. **Efectos de Reputación**:
   - La antigüedad del listado influye positivamente en el precio
   - El rating tiene un efecto positivo
   - Los huéspedes pagan un premium por confianza y completitud de información

4. **Accesibilidad y Ubicación**: La distancia a puntos de interés y sistemas de transporte colectivo afecta los precios. Listados más cercanos a estos puntos tienen precios más altos.

5. **Efectos Espaciales**: La incorporación de efectos espaciales (spillover y estructura espacial de errores) resultó alta, positiva y significativa, lo cual resalta la importancia de incluir estos efectos en estudios de precios.

## 📁 Estructura del Proyecto

```
Analisis-espacial-precios-Airbnb/
├── README.md                    # Este archivo
├── requirements.txt             # Dependencias de Python
├── .gitignore                   # Archivos a ignorar por Git
├── LICENSE                      # Licencia del proyecto
│
├── src/                         # Código fuente modular
│   ├── __init__.py             # Inicialización del módulo
│   ├── config.py               # Configuración y constantes
│   └── utils.py                # Funciones reutilizables
│
├── notebooks/                   # Jupyter notebooks del análisis
│   ├── 01_procesamiento_limpieza.ipynb
│   ├── 02_exploracion_visual.ipynb
│   ├── 03_distancias_ubicacion.ipynb
│   ├── 04_autocorrelacion_espacial.ipynb
│   └── 05_regresion_espacial.ipynb
│
├── data/                        # Datos (no versionados por tamaño)
│   └── README.md               # Descripción de fuentes de datos
│
└── plots/                       # Visualizaciones generadas
    ├── boxplot.png
    ├── LISA.png
    ├── Moran.png
    └── ...
```

## 🚀 Instalación

### Prerrequisitos

- Python 3.8 o superior
- pip o conda para gestión de paquetes
- Git

### Paso 1: Clonar el repositorio

```bash
git clone https://github.com/edgarobles97/Analisis-espacial-precios-Airbnb.git
cd Analisis-espacial-precios-Airbnb
```

### Paso 2: Crear entorno virtual (recomendado)

**Usando venv:**
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

**Usando conda:**
```bash
conda create -n airbnb-analysis python=3.8
conda activate airbnb-analysis
```

### Paso 3: Instalar dependencias

```bash
pip install -r requirements.txt
```

### Paso 4: Instalar el módulo local

```bash
pip install -e .
```

## 💻 Uso

### Ejecutar notebooks

1. Iniciar Jupyter:
```bash
jupyter notebook
```

2. Navegar a la carpeta `notebooks/` y ejecutar los notebooks en orden:
   - `01_procesamiento_limpieza.ipynb`
   - `02_exploracion_visual.ipynb`
   - `03_distancias_ubicacion.ipynb`
   - `04_autocorrelacion_espacial.ipynb`
   - `05_regresion_espacial.ipynb`

### Usar módulo de utilidades

```python
from src.utils import haversine, multi_collinearity_heatmap
from src.config import PATHS, SPATIAL_PARAMS

# Cargar datos
df = load_airbnb_data(PATHS['data'] / 'airbnb.csv')

# Calcular distancias
df['distance'] = df.apply(haversine, axis=1)

# Visualizar multicolinealidad
multi_collinearity_heatmap(df[['precio', 'bedrooms', 'bathrooms']])
```

## 🔬 Metodología

### Pipeline de Análisis

1. **Procesamiento y Limpieza**
   - Carga de datos de Inside Airbnb
   - Limpieza de valores faltantes
   - Transformación de variables
   - Detección y tratamiento de outliers

2. **Exploración Visual**
   - Análisis descriptivo por alcaldía
   - Visualizaciones geográficas
   - Distribución de precios
   - Mapas de calor

3. **Incorporación de Variables de Ubicación**
   - Cálculo de distancias a puntos de interés (Trip Advisor)
   - Distancias a estaciones de metro
   - Distancias a estaciones de metrobús
   - Creación de índices de accesibilidad

4. **Autocorrelación Espacial**
   - Índice I de Moran Global
   - Índice I de Moran Local (LISA)
   - Identificación de clusters espaciales
   - Visualización de agrupaciones

5. **Regresión Espacial**
   - Modelo OLS base
   - Modelo Spatial Lag (SAR)
   - Modelo Spatial Error (SEM)
   - Comparación de modelos

### Técnicas Estadísticas

- **Autocorrelación Espacial**: Índice de Moran I
- **Análisis Local**: LISA (Local Indicators of Spatial Association)
- **Regresión Espacial**: Modelos SAR y SEM
- **Matriz de Pesos Espaciales**: K-nearest neighbors (k=45)

## 📊 Datos

### Fuentes

1. **Inside Airbnb** (Murray Cox)
   - Datos de listados de Airbnb en CDMX
   - Variables de precio, características, ubicación y reputación

2. **Trip Advisor**
   - Coordenadas de puntos de interés turístico
   - Principales atracciones de la CDMX

3. **Datos Abiertos CDMX**
   - Shapefiles de alcaldías y colonias
   - Ubicación de estaciones de metro y metrobús
   - Estaciones de Ecobici

### Variables Principales

**Dependiente:**
- `precio`: Precio por noche (MXN)
- `ln_price`: Logaritmo natural del precio

**Independientes:**
- Características físicas: `bedrooms`, `bathrooms`, `accommodates`, `beds`
- Tipo de alojamiento: `Private room`, `Shared room`
- Amenidades: `wifi`, `parking`, `kitchen`, etc.
- Reputación: `review_scores_rating`, `number_of_reviews`, `ad_duration`
- Ubicación: `alcaldía`, `código_postal`, `latitude`, `longitude`
- Accesibilidad: `pi_dist` (índice de proximidad), `metro_distance`

## 📈 Resultados

Los resultados completos se encuentran en los notebooks y en la carpeta `plots/`.

### Visualizaciones Clave

- **Distribución de Precios**: Mapas de calor por alcaldía y código postal
- **Índice de Moran**: Gráfico de dispersión mostrando autocorrelación
- **LISA Clusters**: Mapa de agrupaciones espaciales (High-High, Low-Low, etc.)
- **Densidad de Listados**: Kernel density con puntos de interés

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para contribuir:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 📧 Contacto

**Edgar Robles Díaz**
- GitHub: [@edgarobles97](https://github.com/edgarobles97)
- Email: [Tu email si quieres incluirlo]

## 🙏 Agradecimientos

- Inside Airbnb por proporcionar datos abiertos
- CIDE por el apoyo institucional
- Comunidad de PySAL por las herramientas de análisis espacial

## 📚 Referencias

- Anselin, L. (1996). The Moran scatterplot as an ESDA tool to assess local instability in spatial association.
- Cliff, A. D., & Ord, J. K. (1973). Spatial autocorrelation.
- Moran, P. A. (1948). The interpretation of statistical maps. Journal of the Royal Statistical Society.

---

**Nota**: Este proyecto fue originalmente desarrollado en 2020 como tesina de maestría y refactorizado en 2025 con mejores prácticas de ingeniería de software y ciencia de datos.
