import pandas as pd
import numpy as np
from scipy.signal import argrelextrema
import matplotlib.pyplot as plt
import datetime

#Import our historical data
data = pd.read_csv('Data/EURUSD.csv', sep='\t')
data.columns = [['Date', 'open', 'high', 'low', 'close', 'vol']]
data = data.drop_duplicates(keep=False)
print(data.iloc(0))
print(data.iloc(0)[0].Date)
# data.Date = pd.to_datetime(data.Date,format='%d.%m.%Y %H:%M:%S.%f')
data.Date = pd.to_datetime(data.Date,format='%d.%m.%Y %H:%M:%S ')
data = data.set_index(data.Date)
data = data[['open', 'high', 'close', 'vol']]

price = data.close.iloc[:100]

# Find our relative extrema
max_idx = argrelextrema(price.values,np.greater,order=1)
min_idx = argrelextrema(price.values,np.less,order=1)

print(max_idx)
print(min_idx)
