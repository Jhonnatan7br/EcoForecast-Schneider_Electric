import os
import json
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from joblib import dump

def train_and_save_model(train_data_path, model_save_path, predictions_save_path):
    # Load the dataset
    df = pd.read_csv(train_data_path)

    # Split the dataset
    X = df.drop('target', axis=1)  # Replace 'target' with the actual target column name
    y = df['target']  # Replace 'target' with the actual target column name
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize the model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    
    # Train the model
    model.fit(X_train, y_train)

    # Make predictions
    predictions = model.predict(X_test)

    # Evaluate the model
    mse = mean_squared_error(y_test, predictions)
    print(f"Mean Squared Error: {mse}")

    # Save the model
    os.makedirs(model_save_path, exist_ok=True)
    model_filename = os.path.join(model_save_path, 'model.joblib')
    dump(model, model_filename)

    # Save the predictions in .json format
    os.makedirs(predictions_save_path, exist_ok=True)
    predictions_dict = {"target": predictions.tolist()}
    with open(os.path.join(predictions_save_path, 'predictions.json'), 'w') as f:
        json.dump(predictions_dict, f)

    print(f"Predictions saved to {predictions_save_path}/predictions.json")

if __name__ == "__main__":
    # Paths
    train_data_path = '../data/train.csv'
    model_save_path = '../models'
    predictions_save_path = '../predictions'
    
    # Train the model and save predictions
    train_and_save_model(train_data_path, model_save_path, predictions_save_path)
