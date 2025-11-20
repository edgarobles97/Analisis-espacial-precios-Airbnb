# Changelog

Todos los cambios notables en este proyecto serán documentados en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/),
y este proyecto adhiere a [Semantic Versioning](https://semver.org/lang/es/).

## [2.0.0] - 2025-01-20

### 🎉 Refactorización Mayor

Esta versión representa una modernización completa del código original de 2020 con mejores prácticas de ingeniería de software y ciencia de datos.

### Added ✨

- **Módulo `src/`**: Código modularizado y reutilizable
  - `src/utils.py`: Funciones reutilizables (haversine, visualizaciones, etc.)
  - `src/config.py`: Configuración centralizada de rutas y parámetros
  - `src/__init__.py`: Inicialización del paquete

- **Gestión de Dependencias**:
  - `requirements.txt`: Lista completa de dependencias con versiones
  - `setup.py`: Configuración para instalación del paquete

- **Documentación Mejorada**:
  - README.md expandido con:
    - Badges de estado
    - Tabla de contenidos
    - Instrucciones de instalación detalladas
    - Descripción de metodología
    - Diccionario de datos
    - Referencias académicas
  - `data/README.md`: Guía completa de fuentes de datos
  - `CHANGELOG.md`: Historial de cambios

- **Archivos de Configuración**:
  - `.gitignore`: Configuración apropiada para proyectos de ciencia de datos
  - `LICENSE`: Licencia MIT

- **Funciones con Documentación**:
  - Docstrings completos en formato NumPy
  - Type hints para mejor legibilidad
  - Ejemplos de uso en docstrings

### Changed 🔄

- **Estructura de Carpetas**:
  - `Notebook/` → `notebooks/` (lowercase para convenciones Unix)
  - `Plots/` → `plots/` (lowercase)
  - Nueva carpeta `src/` para código modular
  - Nueva carpeta `data/` con README

- **Mejoras de Código**:
  - Código repetitivo extraído a funciones reutilizables
  - Configuración centralizada en vez de hardcoded
  - Mejor manejo de errores (fallback UTF-8 → latin1)
  - Funciones documentadas con type hints

- **Librerías Actualizadas**:
  - Migración de `pysal` (deprecated) a módulos modernos (`libpysal`, `esda`, `spreg`)
  - Versiones especificadas para reproducibilidad

### Deprecated ⚠️

- Uso de rutas absolutas hardcodeadas (serán removidas en notebooks)
- Encoding `latin1` por defecto (preferir UTF-8)

### Removed 🗑️

- No se removieron archivos originales, solo se reorganizaron

### Fixed 🐛

- N/A (refactorización no incluye fixes de bugs del análisis original)

### Security 🔒

- Agregado `.gitignore` para evitar commits accidentales de:
  - Archivos grandes de datos
  - Credenciales (`.env`)
  - Archivos temporales del sistema

## [1.0.0] - 2020-06-01

### Added

- Versión original de la tesina
- 6 notebooks de análisis:
  1. Procesamiento y limpieza
  2. Exploración visual
  3. Distancias a metro y puntos de interés
  4. Autocorrelación espacial
  5. Regresión espacial
  6. Visualizaciones con Plotly
- Análisis espacial completo de precios de Airbnb en CDMX
- Implementación de Índice de Moran (global y local)
- Modelos de regresión espacial (SAR, SEM)
- Visualizaciones geográficas
- README básico con resultados principales

---

## Tipos de Cambios

- `Added` para nuevas funcionalidades
- `Changed` para cambios en funcionalidades existentes
- `Deprecated` para funcionalidades que serán removidas
- `Removed` para funcionalidades removidas
- `Fixed` para corrección de bugs
- `Security` para vulnerabilidades de seguridad
