# Configuration parameters for the project

# STAC API endpoint
STAC_API_URL = "https://planetarycomputer.microsoft.com/api/stac/v1"

# Time range for data collection
TIME_RANGE = "2024-03-11/2024-04-01"

FILTER = False
DATASET_NAME = "dataset.csv"

# Cloud cover threshold (percentage)
CLOUD_COVER_THRESHOLD = 15

# NDVI threshold for filtering
NDVI_THRESHOLD = 0.2

# NDHI threshold for filtering
NDHI_THRESHOLD = 0.25

# Bands of interest
BANDS_OF_INTEREST = ["coastal", "blue", "green", "red", "nir08", "swir16", "swir22", "lwir11"]

# Band mapping for scaling
BAND_MAPPING = {
    'coastal': 'B1',
    'blue': 'B2',
    'green': 'B3',
    'red': 'B4',
    'nir08': 'B5',
    'swir16': 'B6',
    'swir22': 'B7',
    'lwir11': 'B10'
}

# Area of interest (polygon coordinates)
POLYGON_GEOJSON = {
    "type": "Polygon",
    "coordinates": [[
        [35.425319654, 32.566444657],
        [35.425263411, 32.566480554],
        [35.425629751, 32.566491813],
        [35.4267837, 32.566000681],
        [35.427050295, 32.565594612],
        [35.427458434, 32.565414986],
        [35.428331729, 32.565377635],
        [35.427650177, 32.563207762],
        [35.424608773, 32.563749924],
        [35.424609093, 32.563881124],
        [35.425375536, 32.566217865],
        [35.425319654, 32.566444657]
    ]]
}
