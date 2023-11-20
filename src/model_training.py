import pandas as pd
import argparse
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score
from joblib import dump

# To run the script, you would use the command line:
# python train_model.py --input_file path/to/your/processed_data.csv --model_file path/to/your/model.pkl

def load_data(file_path):
    # Load processed data from CSV file
    df = pd.read_csv(file_path)
    return df

def split_data(df):
    # Split data into training and validation sets
    X = df.drop('target', axis=1)  # Replace 'target' with the actual target column name
    y = df['target']  # Replace 'target' with the actual target column name
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_val, y_train, y_val

def train_model(X_train, y_train):
    # Initialize your model
    model = RandomForestClassifier(random_state=42)
    # Train the model
    model.fit(X_train, y_train)
    return model

def save_model(model, model_path):
    # Save the trained model
    dump(model, model_path)

def parse_arguments():
    parser = argparse.ArgumentParser(description='Model training script for Energy Forecasting Hackathon')
    parser.add_argument(
        '--input_file', 
        type=str, 
        default='data/processed_data.csv', 
        help='Path to the processed data file to train the model'
    )
    parser.add_argument(
        '--model_file', 
        type=str, 
        default='models/model.pkl', 
        help='Path to save the trained model'
    )
    return parser.parse_args()

def main(input_file, model_file):
    df = load_data(input_file)
    X_train, X_val, y_train, y_val = split_data(df)
    model = train_model(X_train, y_train)
    save_model(model, model_file)

    # Make predictions on the validation set
    y_pred = model.predict(X_val)

    # Calculate F1 score
    f1 = f1_score(y_val, y_pred, average='weighted')  # Use 'binary' for binary classification, 'macro' for multi-class
    print(f"F1 Score: {f1}")

if __name__ == "__main__":
    args = parse_arguments()
    main(args.input_file, args.model_file)
