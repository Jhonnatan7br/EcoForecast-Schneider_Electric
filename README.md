# EcoForecast Schneider_Electric
 
# SE-Europe-Data_Challenge
NUWE - Schneider Electric European Data Science Challenge in November 2023.

Create a model capable of predicting the country (from a list of nine) that will have the most surplus of green energy in the next hour. It is needed to consider both the energy generation from renewable sources (wind, solar, geothermic, etc.), and the load (energy consumption). The surplus of green energy is considered to be the difference between the generated green energy and the consumed energy.

The countries to focus on are: Spain, UK, Germany, Denmark, Sweden, Hungary, Italy, Poland, and the Netherlands.

The solution must not only align with Schneider Electric's ethos but also go beyond its current offerings, presenting an unprecedented approach.

# Repository Structure
The repository is organized into several directories, each with a specific purpose in the data processing and machine learning pipeline:

![image](https://github.com/Jhonnatan7br/EcoForecast-Schneider_Electric/assets/104907786/c2314c74-8720-4b1b-84c0-a1edca4eb35f)


- data: Contains raw and processed data files. The raw data spans from 2022 to 2023 and is used as the input for the data processing scripts.
- models: Stores the trained machine learning models. These models are trained using the processed data from the data directory and are used to make predictions.
- predictions: Holds the output from the machine learning models. The predictions are stored in JSON format for easy interpretation and further analysis.
- scripts: Includes shell scripts that execute the entire data processing and machine learning pipeline.
- src: Contains Python scripts for each step of the pipeline:
  - data_ingestion.py: Responsible for fetching and ingesting raw data.
  - data_processing.py: Processes the ingested data and prepares it for model training.
  - model_training.py: Trains the machine learning model with the processed data.
  - model_prediction.py: Generates predictions using the trained model and the test dataset.
  - utils.py: Provides utility functions that may be used across the other scripts.

Additionally, there are several files at the root level of the repository:

.gitattributes: Git configuration file that defines attributes per path.
README.md: The markdown document that provides information about the repository, including how to run the pipeline and interpret the results.
requirements.txt: Lists of tokens to call the required API to ingest the data.

# Data Processing and Prediction Pipeline
The process to obtain insights and predictions involves several steps executed sequentially:

- Data Ingestion: The raw data for the specified period is fetched and stored in the data directory. This step is managed by the data_ingestion.py script.
- Data Processing: The ingested data is then processed by the data_processing.py script to prepare it for model training. This includes cleaning, normalization, feature extraction, and any other necessary preprocessing steps.
- Model Training: The model_training.py script takes the processed data and trains a machine learning model, which is then saved in the models directory. This step includes splitting the data into training and validation sets, selecting a model, training, and evaluating its performance.
- Prediction Generation: The trained model is used to make predictions on new data. The model_prediction.py script loads the test data from the data directory and the trained model from the models directory, performs predictions, and saves the results in the predictions directory as a JSON file.

Shell Script Execution: The run_pipeline.sh shell script in the scripts directory orchestrates the entire process by calling the Python scripts in the correct order with the appropriate arguments.

To run the entire pipeline, navigate to the scripts directory and execute run_pipeline.sh, specifying any custom arguments if necessary. The output will include the trained model and a JSON file with predictions corresponding to the test dataset. The predictions file will contain an array of target values and corresponding predicted values, making it straightforward to compare and analyze the model's performance.

# Types of energy on the ingested

It was selected only renewables sources of energy with the following codes ["B01", "B09", "B11", "B10", "B12", "B13", "B15", "B16", "B18", "B19"]

ENTSO-E documentation B17 is no longer considered green. for this reason are not included, Reference: Gather Worlds
URL: https://eepublicdownloads.blob.core.windows.net/public-cdn-container/clean-documents/Publications/Statistics/Factsheet/entsoe_sfs2022_web.pdf

- B01 Biomass 
- B02 Fossil Brown coal/Lignite
- B03 Fossil Coal-derived gas
- B04 Fossil Gas
- B05 Fossil Hard coal
- B06 Fossil Oil
- B07 Fossil Oil shale
- B08 Fossil Peat
- B09 Geothermal
- B10 Hydro Pumped Storage
- B11 Hydro Run-of-river and poundage
- B12 Hydro Water Reservoir
- B13 Marine
- B14 Nuclear
- B15 Other renewable
- B16 Solar
- B17 Waste
- B18 Wind Offshore
- B19 Wind Onshore
- B20 Other

#Interpolate any missing data
df.interpolate(method='linear', limit_direction='both', inplace=True)

# Schneider Electric value environmental oriented repository

Creating a predictive model that can forecast which of the nine specified countries will have the greatest surplus of green energy in the next hour holds significant value for optimizing energy distribution and reinforcing sustainability efforts. By accurately predicting surpluses, energy providers can make informed decisions about energy storage, load shifting, and inter-country energy transfers, leading to more efficient use of renewable resources. This aligns with Schneider Electric's commitment to sustainability and innovation, enhancing their portfolio with advanced analytics that support the transition to a more resilient and green energy grid. Such a model can also facilitate smarter grid management and reduce reliance on non-renewable energy sources, thus contributing to the overall reduction of carbon emissions and promoting environmental stewardship.

# Tokens:
- b5b8c21b-a637-4e17-a8fe-0d39a16aa849
- fb81432a-3853-4c30-a105-117c86a433ca
- 2334f370-0c85-405e-bb90-c022445bd273
- 1d9cd4bd-f8aa-476c-8cc1-3442dc91506d
