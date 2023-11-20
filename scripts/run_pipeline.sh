#!/bin/bash

# You can run this script from the command line using:
# ./run_pipeline.sh <start_date> <end_date> <raw_data_file> <processed_data_file> <model_file> <test_data_file> <predictions_file>
# For example:
# ./run_pipeline.sh 2020-01-01 2020-01-31 data/raw_data.csv data/processed_data.csv models/model.pkl data/test_data.csv predictions/predictions.json

#!/bin/bash

# Set the base directory to the parent directory of this script
BASE_DIR="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; cd .. ; pwd -P )"

# Define paths for data, models, and predictions relative to the base directory
DATA_DIR="${BASE_DIR}/data"
MODELS_DIR="${BASE_DIR}/models"
PREDICTIONS_DIR="${BASE_DIR}/predictions"
SRC_DIR="${BASE_DIR}/src"

# Command line arguments or default values for file names
start_date=${1:-"2022-01-01"}
end_date=${2:-"2023-01-01"}
raw_data_file="${DATA_DIR}/${3:-raw_data.csv}"
processed_data_file="${DATA_DIR}/${4:-processed_data.csv}"
model_file="${MODELS_DIR}/${5:-model.pkl}"
test_data_file="${DATA_DIR}/test.csv"  # Assuming test.csv is the correct file name
predictions_file="${PREDICTIONS_DIR}/example_predictions.json"

# Navigate to the script directory
cd "${SRC_DIR}"

# Run data_ingestion.py
echo "Starting data ingestion..."
python data_ingestion.py --start_time "${start_date}" --end_time "${end_date}" --output_path "${DATA_DIR}"

# Run data_processing.py
echo "Starting data processing..."
python data_processing.py --input_file "${raw_data_file}" --output_file "${processed_data_file}"

# Run model_training.py
echo "Starting model training..."
python model_training.py --input_file "${processed_data_file}" --model_file "${model_file}"

# Run model_prediction.py
echo "Starting prediction..."
python model_prediction.py --input_file "${test_data_file}" --model_file "${model_file}" --output_file "${predictions_file}"

# Return to the base directory
cd "${BASE_DIR}"

echo "Pipeline completed."
