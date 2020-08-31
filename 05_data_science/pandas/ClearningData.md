# Detecing Missing Data
* isnull() returns True for every cell that is NaN
* any() returns True if a column is True at least once
* notnull() and all() work similar to isnull() and any()
```python
* Which columns have missing values
df.isnull().any()
df.isnull().all()
df[df.isnull().any(axis=1)] # Use axis=1 for rows
```

# Removing Missing Values
* You can use df.drop() to remove items
* But df.dropna() is more powerful in this case
```python
df.drop(columns='WEATHER_CODE', inplace=True)
df.dropna() # drops all rows with null values
df.dropna(axis=1) # drop columns
df.dropna(thresh=4) # keep only rows with 4 values or more
df.dropna(how=‘all’) # only drop if all values are NaN
df.dropna(how=‘any’) # drop if any values are NaN
df.dropna(inplace=True)
```

# Filling Missing Values
* Replace all NaN values with a specific value
```python
df.fillna(5)
```
* fillna() accepts a Series of values
* Per column: replace missing data with mean
```python
df.fillna(df.mean())
```

# Interpolation
* Fill missing values with previous value
```python
df.fillna(method=‘ffill’)
```

* Use ‘bfill’ to fill backwards
* fillna() also accepts options inplace and columns
* For advanced interpolations use df.interpolate()

# Handling Outliers (离群值)
```python
athletes = pd.read_csv('athletes.csv')
athletes.info()
matplotlib inline
heights = athletes['height']
heights.plot.box()

q1 = heights.quantile(.25)
q3 = heights.quantile(.75)
iqr = q3 - q1 
pmin = q1 - 1.5 * iqr
pmax = q3 + 1.5 * iqr
nwh = heights.where(heights.between(pmin, pmax))

compare = pd.DataFrame({'before':heights, 'after':nwh})
compare.plot.box()
compare.describe()
```

# Removing Duplicates
* duplicated() returns a Series of Booleans
* which is True whenever a row is a duplicate
```python
athletes['nationality'].value_counts()

df[df.duplicated()] # shows all duplicates

# removing all duplicates
df.drop_duplicates(inplace=True)

# unique() does the same but returns a numpy array
df.unique() # you usually don’t want this
```

# Converting Types
```python
athletes[athletes['gold'] == 'O']
athletes.loc[7521, ['gold', 'silver', 'bronze']] = 0
```

* We can use the astype() function
* And pass it the type we want to convert to
```python
df[‘some_column’].astype(int)
```

* Or pass a dict with a type per column
* Note: All values have to fit into the new data type
```python
df.astype({‘name’: str, ‘age’: int})
```

#  Fixing Indices
* Set the index to a simple range 0..n
```python
df.reset_index()
df.reset_index(drop=True) # Don’t keep the original index
# Set index from a column
df.set_index(‘id’, drop=True)
```

# Rename
```python
# rename columns
df.rename(columns={‘a’: ‘Ann’, ‘b’: ‘Bob’})
# Or rename some rows
df.rename(index={‘a’: ‘Ann’, ‘b’: ‘Bob’})
```