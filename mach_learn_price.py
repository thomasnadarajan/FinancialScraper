import requests
import pandas
from pyfinmod.financials import Financials
import datetime as dt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
r = requests.get("https://financialmodelingprep.com/api/v3/historical-price-full/AAPL?serietype=line")
corrected = r.json()
array_temp_time = []
array_temp_price = []
for dicter in corrected['historical']:
    #corrected_date = dt.datetime(int(dicter['date'].split('-')[0]), int(dicter['date'].split('-')[1]), int(dicter['date'].split('-')[2]), 0, 0).toordinal()
    corrected_d = dt.date(int(dicter['date'].split('-')[0]), int(dicter['date'].split('-')[1]), int(dicter['date'].split('-')[2])).toordinal()
    array_temp_time.append(corrected_d)
    array_temp_price.append(float(dicter['close']))
parser = Financials("AAPL")
stored = parser.income_statement
income_points = stored.loc["Net Income"]
dates = [x.toordinal() for x in stored.columns.values.tolist()]
logged_indices = []
for x in dates:
    i = 0
    while i < len(array_temp_time):
        if array_temp_time[i] == x:
            logged_indices.append(i)
            break
        elif array_temp_time[i] > x:
            logged_indices.append(i-1)
            break
        i+=1
#print(logged_indices)
corrected = []
for x in logged_indices:
    i = 0
    while i < len(array_temp_price):
        if i == x:
            corrected.append(array_temp_price[i])
            break
        i+=1

#print(corrected)
#print(income_points.values.tolist())
#corrected_y = np.ndarray
corrected.reverse()
xTrain, xTest, yTrain, yTest = train_test_split(income_points.values, np.array(corrected), test_size=0.2)
print(xTest, yTest)
price_model = LinearRegression().fit(xTrain.reshape(-1, 1), yTrain.reshape(-1,1))