# Datos del Proyecto

## 📁 Descripción

Esta carpeta contiene los datos utilizados en el análisis espacial de precios de Airbnb en la Ciudad de México.

**Nota**: Los archivos de datos grandes (>50MB) no están incluidos en el repositorio de Git para mantener el tamaño del repositorio manejable. Los archivos CSV, shapefiles y otros datos deben ser descargados por separado.

## 🔗 Fuentes de Datos

### 1. Inside Airbnb

**Fuente**: http://insideairbnb.com/get-the-data.html

**Archivos necesarios**:
- `listings.csv` - Datos detallados de listados
- Fecha de descarga: Junio 2020 (aproximadamente)
- Ciudad: Ciudad de México, México

**Ubicación esperada**: `data/airbnb/`

### 2. Shapefiles de la Ciudad de México

**Fuente**: Datos Abiertos CDMX (https://datos.cdmx.gob.mx/)

**Archivos necesarios**:
- `alcaldias/alcaldias.shp` - Polígonos de alcaldías
- `coloniascdmx/coloniascdmx.shp` - Polígonos de colonias
- `CP_09/CP_09CdMx_v2.shp` - Polígonos de códigos postales

**Ubicación esperada**: `data/shapefiles/`

### 3. Transporte Público

**Fuentes**:
- Datos Abiertos CDMX
- Sistema de Transporte Colectivo Metro

**Archivos necesarios**:
- `estaciones-metro.csv` - Coordenadas de estaciones del Metro
- `estaciones-metrobus.csv` - Coordenadas de estaciones del Metrobús
- `estaciones_ecobici.csv` - Coordenadas de estaciones de Ecobici

**Ubicación esperada**: `data/transporte/`

### 4. Puntos de Interés

**Fuente**: Trip Advisor

**Archivos necesarios**:
- `sitios_de_interes.csv` - Coordenadas de principales atracciones turísticas

**Ubicación esperada**: `data/poi/`

### 5. Códigos Postales

**Fuente**: SEPOMEX

**Archivos necesarios**:
- `Ciudad de México.xls` - Catálogo de códigos postales

**Ubicación esperada**: `data/codigos_postales/`

## 📂 Estructura Recomendada

```
data/
├── README.md                           # Este archivo
├── raw/                                # Datos crudos sin procesar
│   ├── airbnb/
│   │   └── listings.csv
│   ├── shapefiles/
│   │   ├── alcaldias/
│   │   ├── coloniascdmx/
│   │   └── CP_09/
│   ├── transporte/
│   │   ├── estaciones-metro.csv
│   │   ├── estaciones-metrobus.csv
│   │   └── estaciones_ecobici.csv
│   ├── poi/
│   │   └── sitios_de_interes.csv
│   └── codigos_postales/
│       └── Ciudad de México.xls
│
└── processed/                          # Datos procesados
    ├── inside_abnb_clean.csv
    ├── inside_abnb_clean_2.csv
    ├── inside_abnb_clean_4.csv
    └── metro_clean.csv
```

## 🔐 Privacidad y Licencias

- **Inside Airbnb**: Los datos son públicos y recopilados de listados públicos de Airbnb. Se recomienda revisar los términos de uso de Inside Airbnb.
- **Datos Abiertos CDMX**: Datos de acceso público bajo licencia abierta.
- **Trip Advisor**: Datos de ubicación pública de atracciones turísticas.

## 📥 Cómo Obtener los Datos

1. Visitar las fuentes mencionadas arriba
2. Descargar los archivos necesarios
3. Colocarlos en la estructura de carpetas recomendada
4. Ejecutar los notebooks en orden para procesar los datos

## ⚠️ Notas Importantes

- Los archivos procesados (`*_clean*.csv`) se generan al ejecutar los notebooks
- Los shapefiles deben estar completos (`.shp`, `.shx`, `.dbf`, `.prj`)
- Algunos archivos pueden requerir conversión de encoding (latin1 → utf-8)
- El tamaño total de datos crudos es aproximadamente 500MB - 1GB

## 📊 Diccionario de Datos

Para una descripción detallada de las variables y su significado, consultar:
- Los notebooks individuales
- El README principal del proyecto
- Documentación de Inside Airbnb: http://insideairbnb.com/data-dictionary.html

## 🆘 Ayuda

Si tienes problemas descargando o procesando los datos:
1. Verifica que las URLs de las fuentes estén activas
2. Asegúrate de tener suficiente espacio en disco
3. Revisa los notebooks para ver el formato esperado
4. Abre un issue en el repositorio
