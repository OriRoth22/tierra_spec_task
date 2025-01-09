from data_loader import DataLoader
from data_processor import DataProcessor
from utils import select_latest_item
import random_f
import mapping
from config import FILTER

def main():
    # Initialize components
    data_loader = DataLoader()
    data_processor = DataProcessor()

    # Search for Landsat items
    print("Searching for Landsat items...")
    items = data_loader.search_items()

    # Filter items if FILTER is enabled
    if FILTER:
        print("Filtering items based on NDVI and NDHI...")
        filtered_items = data_processor.filter_items(items, data_loader)
    else:
        filtered_items = items

    # Select the latest item
    selected_item = select_latest_item(filtered_items)
    if not selected_item:
        return None

    # Load and clip data for the selected item
    print("Loading and clipping data...")
    polygon_data = data_loader.load_data(selected_item)

    # Process and save data
    print("Processing and saving data...")
    scaled_df = data_processor.process_and_save_data(polygon_data)

    # Print processing results
    print("Processing complete!")
    print(f"Scaled data shape: {scaled_df.shape}")

    # Run random forest model
    print("Running random forest model...")
    results_test = random_f.run(scaled_df)
    
    return results_test

if __name__ == "__main__":
    # Execute the main process
    results_df = main()
    
    # Create yield map
    if results_df is not None:
        mapping.create_yield_map()
