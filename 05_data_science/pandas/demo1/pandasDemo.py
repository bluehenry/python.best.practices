# There are several ways to create a DataFrame.
# One way way is to use a dictionary. For example:
dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }

import pandas as pd
brics = pd.DataFrame(dict)
print(brics)

# Pandas has assigned a key for each country as the numerical values 0 through 4.
# If you would like to have different index values,
# say, the two letter country code, you can do that easily as well.

# Set the index for brics
brics.index = ["BR", "RU", "IN", "CH", "SA"]

# Print out brics with new index values
print(brics)

# Another way to create a DataFrame is by importing a csv file using Pandas.
countries = pd.read_csv('countries.csv')

print(countries)

# There are several ways to index a Pandas DataFrame.
# One of the easiest ways to do this is by using square bracket notation.
# Print out the column as Pandas Series
print(countries['capital'])

# Print out the column as Pandas DataFrame
print(countries[['capital']])

# Square brackets can also be used to access observations (rows) from a DataFrame.
# Print out first 2 observations (rows)
print(countries[0:2])

# You can also use loc and iloc to perform just about any data selection operation. loc is label-based, which means that you have to specify rows and columns based on their row and column labels. iloc is integer index based, so you have to specify rows and columns by their integer index like you did in the previous exercise.

# Print out the second observation (column)
print(countries.iloc[2])