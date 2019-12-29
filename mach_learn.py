from pyfinmod.financials import Financials
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

import matplotlib.pyplot as plt
import datetime as dt
import numpy
import mpld3
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
parser = Financials("AMZN")
stored = parser.income_statement
income_points = stored.loc["Net Income"]
corrected_indices = income_points.index.map(dt.datetime.toordinal).to_numpy()
corrected_values = income_points.to_numpy()
xTrain, xTest, yTrain, yTest = train_test_split(corrected_indices, corrected_values, test_size = 0.2)
income_model = LinearRegression().fit(xTrain.reshape(-1, 1), yTrain)
prediction = income_model.predict(xTest.reshape(-1,1))
plottable_x = numpy.vectorize(dt.datetime.fromordinal)(xTest)
plt.scatter(plottable_x.tolist(), prediction.tolist())
#mpld3.show()
print(mpld3.fig_to_html(plt.gcf()))
#plt.show()
