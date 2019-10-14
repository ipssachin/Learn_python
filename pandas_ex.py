#pandas excersise
from __future__ import print_function

import pandas as pd
print(pd.__version__)
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter


print(pd.Series(['San Francisco', 'San Jose', 'Sacramento']))

city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
population = pd.Series([852469, 1015785, 485199])

print(pd.DataFrame({ 'City name': city_names, 'Population': population }))

california_housing_dataframe = pd.read_csv("https://dl.google.com/mlcc/mledu-datasets/california_housing_train.csv", sep=",")
# california_housing_dataframe = pd.read_csv("california_housing_train.csv", sep=",")
#
print(california_housing_dataframe.describe())

print(california_housing_dataframe.head())
#
#
# print(california_housing_dataframe.hist('housing_median_age'))
california_housing_dataframe.hist('housing_median_age')
