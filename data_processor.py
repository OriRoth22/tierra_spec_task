import numpy as np
import pandas as pd
from config import NDVI_THRESHOLD, NDHI_THRESHOLD, BAND_MAPPING

class DataProcessor:
    @staticmethod
    def calculate_ndvi(nir, red):
        """Calculate Normalized Difference Vegetation Index."""
        return (nir - red) / (nir + red + 1e-10)

    @staticmethod
    def calculate_ndhi(green, red):
        """Calculate Normalized Difference Height Index."""
        return (red - green) / (green + red + 1e-10)

    def filter_items(self, items, data_loader):
        """Filter items based on NDVI and NDHI thresholds."""
        filtered_items = []
        
        for item in items:
            print(f"Processing item: {item.id} from {item.datetime}")
            
            # Load and process NDVI
            ndvi_data = data_loader.load_data(item)
            ndvi = self.calculate_ndvi(
                ndvi_data["nir08"], 
                ndvi_data["red"]
            )
            mean_ndvi = ndvi.mean().item()
            
            if mean_ndvi <= NDVI_THRESHOLD:
                # Process NDHI
                ndhi = self.calculate_ndhi(
                    ndvi_data["green"], 
                    ndvi_data["red"]
                )
                mean_ndhi = ndhi.mean().item()
                
                if mean_ndhi < NDHI_THRESHOLD:
                    filtered_items.append(item)
                    
        return filtered_items

    @staticmethod
    def scale_reflectance(value):
        """Scale surface reflectance bands."""
        return (value * 0.0000275) - 0.2

    @staticmethod
    def scale_temperature(value):
        """Scale surface temperature band."""
        return (value * 0.00341802) + 149

    def process_and_save_data(self, clipped_data):
        """Process and save the data to CSV files."""
        # Convert to DataFrame
        band_arrays = []
        all_bands = list(clipped_data.data_vars)
        
        for band in all_bands:
            band_data = clipped_data[band].values.flatten()
            band_arrays.append(band_data)

        df = pd.DataFrame(
            {band: band_arrays[i] for i, band in enumerate(all_bands)}
        )
        df = df.apply(pd.to_numeric, errors='coerce')
        df = df.loc[(df!=0).any(axis=1)]
        
        # Save raw data
        #df.to_csv('bands.csv', index=False)
        
        # Process scaled data
        scaled_columns = {}
        reflectance_bands = ['coastal', 'blue', 'green', 'red', 'nir08', 'swir16', 'swir22']
        
        for band in reflectance_bands:
            if band in df.columns:
                scaled_col = f'{band}_scaled'
                df[scaled_col] = self.scale_reflectance(df[band])
                scaled_columns[scaled_col] = BAND_MAPPING[band]

        if 'lwir11' in df.columns:
            scaled_col = 'lwir11_scaled'
            df[scaled_col] = self.scale_temperature(df['lwir11'])
            scaled_columns[scaled_col] = BAND_MAPPING['lwir11']

        scaled_df = df[list(scaled_columns.keys())]
        scaled_df.columns = [scaled_columns[col] for col in scaled_df.columns]
        
        # Save scaled data
        #scaled_df.to_csv('scaled_bands.csv', index=False)
        
        return  scaled_df
