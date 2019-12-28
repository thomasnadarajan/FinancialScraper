from pyfinmod.financials import Financials
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

import matplotlib.pyplot as plt
import datetime as dt


def add_years(d, years):
    """Return a date that's `years` years after the date (or datetime)
    object `d`. Return the same calendar date (month and day) in the
    destination year, if it exists, otherwise use the following day
    (thus changing February 29 to March 1).

    """
    try:
        return d.replace(year = d.year + years)
    except ValueError:
        return d + (dt.date(d.year + years, 1, 1) - dt.date(d.year, 1, 1))
parser = Financials("AAPL")
#col_series = parser.income_statement.columns
stored = parser.income_statement
#print(parser.income_statement)
#income_points = parser.income_statement.loc["Net Income"]
income_points = stored.loc["Net Income"]
#test_corrected = parser.income_statement
corrected_indices = income_points.index.map(dt.datetime.toordinal).to_numpy()
#print(corrected_indices.reshape(1,-1))
corrected_values = income_points.to_numpy()
#print(corrected_values.reshape(1, -1))
xTrain, xTest, yTrain, yTest = train_test_split(corrected_indices, corrected_values, test_size = 0.2)
#print(yTrain)
income_model = LinearRegression().fit(xTrain.reshape(-1, 1), yTrain)
#value_at_2021 = add_years(dt.datetime.now(), 1)

#a = xTest.to_numpy().reshape(1, -1)
print(income_model.coef_)
prediction = income_model.predict(xTest.reshape(-1,1))
print(prediction)
plt.scatter(xTest.tolist(), prediction.tolist())
plt.show()