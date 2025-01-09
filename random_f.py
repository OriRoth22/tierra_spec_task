import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
from config import(
    DATASET_NAME
    )

def run(df_test ,df_train_path=DATASET_NAME):  
    # Read data without assuming header names
    df = pd.read_csv(df_train_path)
    test_df = df_test
    
    # Use column positions directly
    X = df.iloc[:, :7]  # First 7 columns as features
    y = df.iloc[:, 8]   # 8th column as target
    X_test_new = test_df.iloc[:, :7]  # First 7 columns for prediction
    
    # Scale the features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    X_test_new_scaled = scaler.transform(X_test_new)
    
    # Initialize Random Forest model
    rf_model = RandomForestRegressor(n_estimators=150, random_state=42)
    
    # Train the Random Forest model
    print("\nTraining Random Forest...")
    rf_model.fit(X, y)
    
    # Make predictions
    train_predictions = rf_model.predict(X)
    test_predictions = rf_model.predict(X_test_new)
    
    # Add predictions to DataFrames
    results_train = df.copy()
    results_train['Random_Forest_Train_Prediction'] = train_predictions

    results_test = test_df.copy()
    results_test['Random_Forest_Prediction'] = test_predictions

    # Save results to CSV
    #results_train.to_csv('train_results.csv', index=False)
    results_test.to_csv('results.csv', index=False)
    
    print("Results saved to 'results.csv'.")
    return results_test

# Run the function
if __name__ == "__main__":
    df = pd.read_csv('results.csv', DATASET_NAME)
    results_test = run(df)
