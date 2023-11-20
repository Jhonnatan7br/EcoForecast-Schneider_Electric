import argparse
import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.DataFrame()
def load_data():
    # Define the path to the data folder and the output file
    data_folder_path = 'C:/Users/Jhonnatan/Documents/GitHub/EcoForecast-Schneider_Electric/data'
    output_file_path = 'C:/Users/Jhonnatan/Documents/GitHub/EcoForecast-Schneider_Electric/test.csv'

    # Initialize an empty DataFrame for the final merged data
    merged_df = pd.DataFrame()

    # Loop through the files in the data folder
    for file_name in os.listdir(data_folder_path):
        if file_name.endswith('.csv'):
            # Construct the full file path
            file_path = os.path.join(data_folder_path, file_name)

            # Read the CSV file
            df = pd.read_csv(file_path)

            # Skip if the DataFrame is empty
            if df.empty:
                print(f"Warning: The file {file_name} is empty and will be skipped.")
                continue

            # Remove the '.csv' from the file name and use it as a prefix
            file_prefix = file_name.replace('.csv', '') + '_'

            # Add the file name as a prefix to all columns except for 'StartTime' and 'EndTime'
            df.rename(columns=lambda x: file_prefix + x if x not in ['StartTime', 'EndTime'] else x, inplace=True)

            # If merged_df is empty, initialize it with the first DataFrame
            if merged_df.empty:
                merged_df = df
            else:
                # Merge with the existing merged_df
                merged_df = pd.merge(merged_df, df, on=['StartTime', 'EndTime'], how='outer')

    # Fill NaN values with 0
    merged_df.fillna(0, inplace=True)

    # Save the unified DataFrame to the output file
    merged_df.to_csv(output_file_path, index=False)

    return merged_df

# Call the function
df = load_data()

def clean_data(merged_df, gen_codes, data_folder_path):
    # Create a DataFrame for green energy and load data
    green_energy_df = pd.DataFrame()
    load_df = pd.DataFrame()

    # Set 'StartTime' and 'EndTime' as DateTimeIndex for resampling
    merged_df['StartTime'] = pd.to_datetime(merged_df['StartTime'])
    merged_df['EndTime'] = pd.to_datetime(merged_df['EndTime'])

    # Go through the 'gen' and 'load' files and summarize the data
    for file_name in os.listdir(data_folder_path):
        file_prefix = file_name.replace('.csv', '')
        country_code = file_prefix.split('_')[-1].upper()

        if file_name.startswith('gen_') and any(gen_code in file_name for gen_code in gen_codes):
            # Sum 'quantity' for each hour and add to the green energy DataFrame
            gen_quantity_col = f'{file_prefix}_quantity'
            green_energy_df[f'green_energy_{country_code}'] = merged_df[gen_quantity_col].resample('H').sum()

        elif file_name.startswith('load_'):
            # Add 'Load' data to the load DataFrame
            load_col = f'{file_prefix}_Load'
            load_df[f'{country_code}_Load'] = merged_df[load_col].resample('H').sum()

    # Combine green energy and load data
    clean_df = pd.merge(green_energy_df, load_df, left_index=True, right_index=True, how='outer')

    # Reset index to turn 'StartTime' back into a column
    clean_df.reset_index(inplace=True)

    # Reformat 'StartTime' and 'EndTime' to the original string format if needed
    clean_df['StartTime'] = clean_df['StartTime'].dt.strftime('%Y-%m-%dT%H:%M:%SZ')
    clean_df['EndTime'] = clean_df['EndTime'].dt.strftime('%Y-%m-%dT%H:%M:%SZ')

    # Fill missing values with 0
    clean_df.fillna(0, inplace=True)

    return clean_df

# Define the gen codes to filter on
gen_codes = ["B01", "B09", "B11", "B10", "B12", "B13", "B15", "B16", "B18", "B19"]

# Assume df is the merged DataFrame returned by the load_data function
# Call the clean_data function
cleaned_df = clean_data(df, gen_codes, 'C:/Users/Jhonnatan/Documents/GitHub/EcoForecast-Schneider_Electric/data')

# Save the cleaned DataFrame to a CSV file
cleaned_df.to_csv('C:/Users/Jhonnatan/Documents/GitHub/EcoForecast-Schneider_Electric/cleaned_test.csv', index=False)

def preprocess_data_for_ml(cleaned_df):
    # Convert 'StartTime' and 'EndTime' to datetime if they are not already
    cleaned_df['StartTime'] = pd.to_datetime(cleaned_df['StartTime'])
    cleaned_df['EndTime'] = pd.to_datetime(cleaned_df['EndTime'])

    # Ensure that all intervals are one hour long
    # This step assumes that the data is already in 1-hour intervals, if not, resampling should be done before this step
    cleaned_df = cleaned_df.set_index('StartTime').resample('H').first()

    # Drop the 'EndTime' as it is redundant for fixed intervals
    cleaned_df = cleaned_df.drop(columns=['EndTime'])

    # Handle missing values if any - options are to fill with 0, mean or interpolate
    cleaned_df = cleaned_df.fillna(0)  # or cleaned_df.interpolate() or cleaned_df.fillna(cleaned_df.mean())

    # Prepare features (X) and target (y) if it's a supervised model
    # Assuming the target variable is named 'target_column' and all others are features
    X = cleaned_df.drop(columns=['target_column'])  # Replace with your actual target column name
    y = cleaned_df['target_column']  # Replace with your actual target column name

    # Scale the features - this is crucial for many algorithms, especially those sensitive to magnitude like SVMs or kNN
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # The function returns the scaled features and the target, ready for training a model
    return X_scaled, y

# Assume cleaned_df is the DataFrame returned by the clean_data function
# Call the preprocess_data_for_ml function
X, y = preprocess_data_for_ml(cleaned_df)

# Now X and y can be used to train a machine learning model

def preprocess_data_for_ml(cleaned_df, output_file_path):
    # Assuming 'cleaned_df' has all the necessary columns and we just need to restructure and save it

    # Check if the cleaned DataFrame has the expected number of rows
    if len(cleaned_df) != 2210:
        raise ValueError(f"The DataFrame has {len(cleaned_df)} rows, but 2210 rows are required.")

    # Assuming 'cleaned_df' already has the columns 'StartTime', 'EndTime', 'Load', 'Generated', 'UnitName'
    # And assuming 'AreaID' is an index or a column in the DataFrame that we need to use as header
    # We will set 'AreaID' as the header and drop it from the rows
    cleaned_df.columns = cleaned_df.loc['AreaID']
    cleaned_df = cleaned_df.drop('AreaID')

    # Assuming 'StartTime' and 'EndTime' are the first two rows after 'AreaID'
    # Set 'StartTime' and 'EndTime' back to the DataFrame from the index
    cleaned_df = cleaned_df.reset_index()

    # Save the DataFrame to the CSV file
    cleaned_df.to_csv(output_file_path, index=False)

# Load your cleaned data
# cleaned_df = pd.read_csv('path_to_your_cleaned_data.csv')

# Define the output file path
output_file_path = 'C:/Users/Jhonnatan/Documents/GitHub/EcoForecast-Schneider_Electric/test.csv'
# Assuming load_data, clean_data, and preprocess_data_for_ml are already defined functions
# from the previous discussions and you have them implemented in your script.

def save_data(df, output_file_path):
    # Save the preprocessed DataFrame to a CSV file
    df.to_csv(output_file_path, index=False)
    print(f"Data saved to {output_file_path}")

def main(input_file, output_file):
    # Load the data
    df = load_data(input_file)

    # Clean the data
    # You need to provide the necessary arguments for clean_data based on your implementation
    df_clean = clean_data(df)

    # Preprocess the data for machine learning
    # You need to provide the necessary arguments for preprocess_data_for_ml based on your implementation
    df_processed, _ = preprocess_data_for_ml(df_clean)

    # Save the preprocessed data
    save_data(df_processed, output_file)

if __name__ == "__main__":
    # Parse arguments from the command line
    args = parse_arguments()

    # Execute the main function with the provided arguments
    main(args.input_file, args.output_file)
