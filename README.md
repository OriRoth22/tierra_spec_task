# Landsat Yield Prediction

A Python-based project for analyzing Landsat satellite imagery to predict agricultural yield using machine learning models.

## Overview

This project processes Landsat Collection 2 Level 2 data to:
1. Filter scenes based on cloud cover and vegetation indices
2. Extract spectral bands for specific geographical regions
3. Apply machine learning models to predict agricultural yield

## Requirements

- pystac-client
- odc-stac
- rioxarray
- netCDF4
- rasterio
- planetary-computer
- pandas
- numpy
- scikit-learn
- matplotlib
- geopandas
- shapely

## Data Processing Pipeline

### 1. Scene Selection
- Filters Landsat scenes by:
  - Date range: March-April 2024
  - Cloud cover < 15%
  - NDVI threshold < 0.2
  - NDHI threshold < 0.25

### 2. Data Extraction
- Clips data to region of interest using GeoJSON polygon
- Extracts bands: coastal, blue, green, red, NIR, SWIR1, SWIR2, LWIR
- Scales reflectance and temperature values

### 3. Machine Learning Models
Implements multiple regression models:
- Linear Regression
- Random Forest
- Gradient Boosting
- Neural Networks

The Random Forest model achieved the best performance based on R² and RMSE metrics.

### 4. Yield Mapping
Generates spatial yield predictions visualized as a heatmap.

## Usage

1. Configure the polygon coordinates in `polygon_geojson`
2. Set the desired time range in `time_of_interest`
3. Run the script to process data and generate predictions
4. Results are saved in:
   - `bands.csv`: Raw band values
   - `scaled_bands.csv`: Scaled spectral data
   - `results.csv`: Model predictions

## Model Performance

The implemented models were evaluated using R² and RMSE metrics on the training dataset. Detailed performance metrics are available in the script output.
