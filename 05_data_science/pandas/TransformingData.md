# Mathematical Operators
```python
import numpy as np
import pandas as pd

df = pd.DataFrame(np.ones([5,4]), columns=['a', 'b', 'c', 'd'])

# Basic math operations on a DataFrame perform the computation for every cell
df *= 2

# You can also do calculations on specific rows or columns
df.loc[1] /= 2
df['b'] -= 1

```

* Operating on Two Series
    * Returns a new Series object
    * With all indices from both inputs
    * Results only filled where indices overlap; NaN everywhere else
    
* Operating on Two DataFrames
    * Returns a new DataFrame object
    * With all column and row labels from both inputs
    * Results only filled where indices overlap; NaN everywhere else
    
* Operating on Series and DataFrame
    * Labels are matched on columns
    * Returns a DataFrame
    * Results only filled where indices overlap; NaN everywhere else     
    
# Function Application       
## Numpy ufuncs
* Functions that work on entire DataFrames/Series
* Many mathematical operations, see [Numpy ufuncs](https://goo.gl/ESR8nX)

## Applying Functions
* DataFrame.applymap() applies a function to each cell
* Series.apply() does the same for values in a Series
* Applying Functions to Cells
    * Pass the function to df.applymap() – no parentheses!
    * Returns a new DataFrame with results
    * Equivalent function on a Series is called apply()
* Applying Functions to Rows/Columns
    * DataFrame.apply() and Series.apply() do different things!
    * DataFrame.apply() applies a function to entire rows/columns

```python
df.apply(f) # apply f to every column of df
df.apply(sum) # calculate sum of every column
df.apply(sum, axis=1) # calculate sum of every row
```

```python
df = pd.DataFrame({'sin': np.arange(0, 5*np.pi, 0.01), 
                   'cos': np.arange(0.5*np.pi, 5.5*np.pi, 0.01)})

# Numpy ufuncs like np.sin operate on every cell
# Here we compute the sin for every cell in the dataframe
df = np.sin(df)

% matplotlib inline
df.plot()


def iqr(col):
    q1 = col.quantile(.25)
    q3 = col.quantile(.75)
    return q3 - q1 

# df.apply() executes the given function on a whole row or column
df.apply(iqr)

def somefunc(x):
    return np.abs(x+.25)

# df.applymap() applies the given function for every cell in the DataFrame
df.applymap(somefunc).plot()
```

# Grouping and Aggregation
* Select one or more columns on the groupby object
* Before doing any actual calculations
```python
athletes.groupby(‘sport’)[‘gold’].sum()
# Group on multiple columns
athletes.groupby([‘sport’, ‘nationality’])[‘gold’].sum()
```
* Functions shown the following are optimized for GroupBy objects
    * count(), sum(), mean(), median(), std(), var(), min(), max(), first(), last()
* But you can call all methods on the underlying object (DF/Series)
* Or use GroupBy.apply() to call your own function

# Structural transformation
* stack() moves all data into 1 column with a multi level index
* Columns to rows
```python
# stack() moves data from rows into a single column
m = pd.read_csv('monthly_data.csv')
# Preparation: move the 'YYYY' column into the index
m.set_index('YYYY', inplace=True)
m.stack()

# stack() also allows quick calculations over all cells
m.stack().sum()
```
* Rows to Columns
* unstack() creates columns for the innermost index level and moves data from the rows into these columns
```python

# unstack() takes the inner index level and creates a column for every unique index
# It then moves the data into these columns
w.unstack()
```

# Reshaping Rows and Columns with pivot() and melt()
* pivot() moves data from rows into columns, so that we end up with a wider, shorter DataFrame
* pivot() takes 3 arguments: index, columns, and values
    * The first argument is the column that will be used for row indices
    * The second argument is the column that will be used to create column labels
* Each of these takes a column name from the original DataFrame
* Returns a DataFrame; rows and columns taken from index and columns, values taken from values
```python
p = pd.DataFrame({'id': [823905, 823905,
                         235897, 235897, 235897,
                         983422, 983422],
                  'item': ['prize', 'unit', 
                           'prize', 'unit', 'stock', 
                           'prize', 'stock'],
                  'value': [3.49, 'kg',
                            12.89, 'l', 50,
                            0.49, 4]})
p.pivot('id', 'item')                           
```

* melt() is the opposite of pivot()
* It moves the data from the rows into a single column
* The column names will show up in a new column called "variable"
* All other values not set as id_vars will end up in “value” column
* Returns a DataFrame; Use id_vars to list columns that contain group identifiers

# Combining Datasets
* Adding a new column -- needs an indexed datastructure (Series)
* Adding a row with .loc -- no Series necessary
* We can also use append, but in that case we need a Series with a name (will be used as row index)
* Merging two DataFrames, by default this does an inner join on the common column (stud_nr)
```python
# We can also specify other join types: left, right, outer
grades.merge(other, how='outer')
```