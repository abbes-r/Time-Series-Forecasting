# Time-Series-Forecasting
This project demonstrates time series forecasting using weather data. The primary goal is to predict the temperature (T (degC)) for the next 48 hours using previous data, including historical temperature and other weather-related features. This project showcases techniques in data analysis, feature engineering, and forecasting models.

## Dataset
The weather dataset is provided by the Max Planck Institute for Biogeochemistry. It consists of hourly observations from 2009 to 2016, with the following key details:
- Number of features: 19
- Features include:
  - Temperature (T (degC))
  - Atmospheric pressure (p (mbar))
  - Dew point temperature (Tdew (degC))
  - Relative humidity (rh (%))
  - Wind components (Wx, Wy)
  - Seasonal features (e.g., day and year trigonometric encodings)
- Time range: January 1, 2009, to December 31, 2016

## Steps in the Notebook
### Data Loading and Preprocessing
- The dataset is loaded using pandas, and the Date Time column is set as the index.
- Date-time formatting is applied to ensure proper handling of temporal data.

### Exploratory Data Analysis (EDA)
- Basic statistics and visualizations are used to understand the distribution and trends of the data.
- Key insights include seasonal patterns and relationships between features.
  
### Feature Engineering
- Derived features such as sinusoidal encoding of day and year for capturing seasonality.
- Lagged variables and rolling statistics for temporal dependencies.

### Model Development
- Models (e.g., neural networks or other time series models) are built to predict future temperatures.
- A rolling window of one week is used as the input to predict the next 48 hours.

### Model Evaluation
- Metrics like Mean Absolute Error (MAE) and Root Mean Square Error (RMSE) are used to assess the performance.

## Prerequisites
- Ensure you have the necessary Python libraries installed via the requirements.txt file
_ You can make sure torch is correctly installed using pip:
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu


