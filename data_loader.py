import pystac_client
import planetary_computer
import odc.stac
from shapely.geometry import shape
import geopandas as gpd
import xarray as xr
import rioxarray

from config import (
    STAC_API_URL, 
    TIME_RANGE, 
    CLOUD_COVER_THRESHOLD, 
    POLYGON_GEOJSON, 
    BANDS_OF_INTEREST
)

class DataLoader:
    def __init__(self):
        self.catalog = pystac_client.Client.open(
            STAC_API_URL,
            modifier=planetary_computer.sign_inplace,
        )
        self.polygon_gdf = gpd.GeoDataFrame(
            geometry=[shape(POLYGON_GEOJSON)], 
            crs="EPSG:4326"
        )

    def search_items(self):
        """Search for Landsat items based on criteria."""
        search = self.catalog.search(
            collections=["landsat-c2-l2"],
            intersects=POLYGON_GEOJSON,
            datetime=TIME_RANGE,
            query={"eo:cloud_cover": {"lt": CLOUD_COVER_THRESHOLD}}
        )
        return search.item_collection()

    def load_data(self, selected_item):
        """Load data for a selected item."""
        bbox = self.polygon_gdf.total_bounds
        data = odc.stac.stac_load(
            [selected_item],
            bands=BANDS_OF_INTEREST,
            bbox=bbox,
            patch_url=planetary_computer.sign,
        ).isel(time=0)
        
        data.rio.set_crs("EPSG:4326", inplace=True)
        clipped_data = data.rio.clip(
            [self.polygon_gdf.geometry[0]], 
            self.polygon_gdf.crs, 
            all_touched=True
        )
        df = clipped_data.to_dataframe().reset_index()

        # Save the cleaned DataFrame to a CSV file
        #df.to_csv('clipped_data.csv', index=False)
        # Saving as NetCDF
        
        # Convert the DataFrame to an xarray Dataset
        ds = xr.Dataset.from_dataframe(df)
        
        # Save as NetCDF
        ds.to_netcdf('polygon_data.nc')
        return clipped_data
