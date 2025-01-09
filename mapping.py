import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import xarray as xr 

def create_yield_map():
    # Load the clipped data and predictions
    clipped_data = xr.open_dataset("polygon_data.nc")
    results_df = pd.read_csv('results.csv')
    
    # Extract the predicted values (Random_Forest_prediction column)
    predictions = results_df['Random_Forest_Prediction'].values
    
    # Assuming 'red' contains the raster values (reshape it into 2D if needed)
    red_values = clipped_data['red'].values
    num_rows = int(np.sqrt(len(red_values)))  # Assuming the data is square-shaped
    num_cols = num_rows  # Adjust this if your raster is not square
    
    # Reshape the red_values into a 2D array representing the raster shape
    raster_shape = (num_rows, num_cols)
    red_values_reshaped = red_values.reshape(raster_shape)
    
    # Initialize an array of NaNs (or zeros) to hold the yield map
    yield_map = np.full(raster_shape, np.nan)
    
    # Get the indices of the non-zero pixels
    non_zero_indices = np.where(red_values_reshaped.flatten() != 0)[0]
    
    # Check if the number of non-zero pixels matches the number of predictions
    if len(non_zero_indices) != len(predictions):
        raise ValueError("The number of predictions does not match the number of non-zero pixels.")
    
    # Place the predictions back into the yield map at the non-zero locations
    yield_map.ravel()[non_zero_indices] = predictions
    
    # Plot the yield map
    plt.figure(figsize=(10, 8))
    plt.imshow(yield_map, cmap='viridis', interpolation='none')  # You can adjust the colormap as needed
    plt.colorbar(label='Predicted Yield')  # Add colorbar for reference
    plt.title('Predicted Yield Map')
    plt.xlabel('X Pixel')
    plt.ylabel('Y Pixel')
    plt.savefig("output", dpi=300, bbox_inches='tight')
    plt.show()
    

    
if __name__ == "__main__":
    # Call the function
    create_yield_map()
