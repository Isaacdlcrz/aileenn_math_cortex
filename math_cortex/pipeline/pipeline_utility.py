import pandas as pd
import numpy as np
import json
import scipy.stats as stats
from prophet import Prophet
from scipy.fft import dct, idct
from statistics import median
from flask import jsonify

def convolve_2_dfs(df1, df2, tag1, tag2):
    array1 = df1[tag1]
    array2 = df2[tag2]
    conv = np.convolve(array1, array2)
    return conv
    
def predictions(df1):
    """### Import Data"""
    data = df1 #pd.read_csv("../new_data.csv")[-100:]
    data["fecha"] = pd.to_datetime(data["fecha"])
    data = data.sort_values(by=['fecha']).reset_index(drop=True)

    """### Check for null values and outliers"""

    # Drop NA
    data.dropna(inplace=True)

    # Drop Outliers
    data = data[np.abs(stats.zscore(data.valores)) < 3]


    """## 2.- DCT & FFT Analysis
    ---

    ### Imports
    """

    N = len(data)
    t = np.linspace(0, 1, N, endpoint=False)

    x = data["valores"].values
    y = dct(x, norm='ortho')
    windows = []
    transformations = {}

    for i in range(2, 12):
        temp_window = np.zeros(N)
        temp_window[:N//i] = 1
        windows.append(temp_window)


    for idx, window in enumerate(windows):
        temp_transform = idct(y*window, norm='ortho')
        transformations[idx+2] = temp_transform

    differences = {}
    for key in transformations:
        transformation = transformations[key]
        temp_diff = 0
        for idx, val in enumerate(transformation):
            if idx == 0:
                continue
            current_diff = np.round(abs(val-transformation[idx-1]), 4)
            if current_diff != 0.0:
                temp_diff += current_diff

        if temp_diff != 0:
            differences[key] = temp_diff

    keys = list(transformations.keys())
    chosen_key = keys[0]
    secondary_key = keys[1]
    time_series = transformations[chosen_key]
    secondary_series = transformations[secondary_key]

    timestamps = data["fecha"].values
    transformed_data = pd.DataFrame({'fecha': timestamps, 'valores': time_series})

    """## 4.- Model
    ---
    """

    """Rename DF columns"""

    transformed_data.columns = ['ds', 'y']

    """### FB Prophet"""

    pm = Prophet()

    pm.fit(transformed_data)

    pfuture = pm.make_future_dataframe(periods=7)

    pforecast = pm.predict(pfuture)

    # Dataframe en JSON a ser regresado al front
    #   |    |   |
    #   V    V   V
    forecast_json = pforecast.to_json(orient="split")
    
    return json.loads(forecast_json)

    mae = np.mean(
        abs(transformed_data.y - pforecast.yhat[:len(transformed_data.y)]))

    """### Prediction Convolutions

    #### FB Prophet
    """
    # Arreglo a ser regresado al front
    #   |    |   |
    #   V    V   V
    prophet_future_conv = convolve_2_dfs(pforecast, climaData, "yhat", "prec")
    
    
