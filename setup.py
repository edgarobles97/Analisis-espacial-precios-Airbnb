"""
Setup configuration for Analisis Espacial Precios Airbnb CDMX
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README for long description
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="airbnb-cdmx-spatial-analysis",
    version="2.0.0",
    author="Edgar Robles Díaz",
    author_email="",
    description="Análisis espacial de precios de Airbnb en la Ciudad de México",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/edgarobles97/Analisis-espacial-precios-Airbnb",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: GIS",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "pandas>=1.3.0,<2.0.0",
        "numpy>=1.21.0,<2.0.0",
        "geopandas>=0.10.0,<1.0.0",
        "shapely>=1.8.0,<2.0.0",
        "pyproj>=3.2.0,<4.0.0",
        "libpysal>=4.6.0,<5.0.0",
        "esda>=2.4.0,<3.0.0",
        "spreg>=1.2.0,<2.0.0",
        "matplotlib>=3.4.0,<4.0.0",
        "seaborn>=0.11.0,<1.0.0",
        "plotly>=5.3.0,<6.0.0",
        "scipy>=1.7.0,<2.0.0",
        "statsmodels>=0.13.0,<1.0.0",
        "scikit-learn>=1.0.0,<2.0.0",
    ],
    extras_require={
        "dev": [
            "jupyter>=1.0.0",
            "ipykernel>=6.0.0",
            "black>=21.0",
            "flake8>=4.0.0",
            "pytest>=6.0.0",
        ],
        "notebooks": [
            "jupyter>=1.0.0",
            "ipykernel>=6.0.0",
            "ipywidgets>=7.6.0",
            "descartes>=1.1.0,<2.0.0",
            "contextily>=1.2.0,<2.0.0",
            "geoplot>=0.5.0,<1.0.0",
            "mapclassify>=2.4.0,<3.0.0",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.md"],
    },
)
