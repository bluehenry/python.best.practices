# Prerequisites
## Jupyter
* Install JupyterLab
```bash
pip install jupyterlab
```
* Running JupyterLab
```bash
sudo jupyter lab build
```

# Exploring data
## Exploring a dataset

```python
import numpy as np
import pandas as pd

df = pd.read_csv('weather.csv')

# How many rows and columns are there
df.shape

# Data type per column, memory usage
df.info()

# Inspecting start and end of the data: head() and tail() 
df.head()
```

## Statistic Exploration
* These work both on Series and DataFrames
    * Maxinum, Minimum, mean, media
* Counting values
    * df.mode(), Series.value_counts()
* Distribution
    * df.std(), df.var(), df.skew(), df.kurtosis(), df.quantitle()
        
```python
# An overview of basic statistics
df.describe()

df.mean()
df.max()
df['PRESSURE'].min()
df['TEMP'].mode()
```
```text
count
mean (average) 平均数
median (middle number) 中位数
mode (the most common number in a data set) 众数
std （Standard Deviation) 标准差
min
25%
50%
75%
max
```

### Standard Deviation
* [标准差计算公式](https://mp.weixin.qq.com/s?src=11&timestamp=1584663135&ver=2227&signature=xa-8P-C1KYN*BCwSr7f0ka8gXu4HErvjx4pwrsAwIjrW8-eRUPr5m-KwsBckcTTdkrE9JDp4KzI0FbObjFmKjlZ6jXTkzAttYTF80m2YuOvtRI*nMlHjnu*O3cXa6HU0&new=1)
* [直观、形象、动态，一文了解无处不在的标准差](https://mp.weixin.qq.com/s?src=11&timestamp=1584663305&ver=2227&signature=5yPP8GWQlrINGJYDTV0CBr2O88OZuj2SaZ7VSU8F8KzAvGDqkN6V99lR2k*fIdyZp52*9CW4DujHc3OSyWATJDoWnZ2MX2eNwc-imZ32xpEihsfNL*y-6cpAXBspGlwn&new=1)
* 总结数字的方式有两种：量化其相似性或差异（difference）。
    * 量化数字的相似性即「集中趋势量数」（measures of central tendency），包括平均数、中位数和众数；
    * 量化数字的差异即「差异量数」（measures of variability），包括方差和标准差。
* 当数字越分散时，标准差越大。


### Visualization
```python
df['TEMP'].plot()
df['TEMP'].hist()
```

# Selecting, Filtering, and Sorting Data
## Indexing (Single Value)
* Retrieve a column by label
* This returns a Series
```python
df['col_name']  # if column index has type string
df[5]           # if column index has type int
```
* retrieve cell from column and row
```python
df['col_name']['row_name] 
```

* more samples
```python
# Get series
df['TEMP']

# Get slice
df['TEMP'][:4]

# Don't use this
df.TEMP

df.['TEMP'][1]


# The property T is an accessor to the method transpose().
df.T
dft = dft.T
dft.columns
dft[2]
dft[0]['TEMP']
dft[2][2]
dft['TIME':'PRESSURE']

t = pd.DataFrame([['John'], ['Bob'], ['Anne']], index=[4,3,4])
t
t[0][4]

```

## Indexing with lists and slices
### lists
* Using lists to retrieve multiple columns in any order
* This returns a DataFrame
 ```python
# out brackets mean that we are indexing into the DataFrame of our series
# inner brackets mean that we're using a Python list to select multiple things at once
# select columns with lists
df[['PRESSURE', 'TIME', 'TEMP']]
dft[3:]

# Select a number of rows from series
df['TIME'][[3,1,4]]
```
### Slices
* Slices return rows, not columns 
* ALso returns a DataFrame
* also works with labels
```python
# In Python a slice uses a colon to select a range of things
# select rows with slices
df[2:4]
df[2:4][['PRESSURE', 'TIME', 'TEMP']]
```

## [pandas.DataFrame.loc](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html)
* row-based indexing with labels
* Retrieve rows
* Select columns in the same operation
```python
capitals = pd.DataFrame(
    [
    ["Ngerulmud",391,1.87],
    ["Vatican City",826,100],
    ["Yaren",1100,10.91],
    ["Funafuti",4492,45.48],
    ["City of San Marino",4493]
    ], 
    index = ["Palau", "Vatican City", "Nauru", "Tuvalu", "San Marino"],
    columns=['Capital', 'Population', 'Percentage'])

capitals
# loc, single operation
capitals.loc['Nauru', 'Population']
# chained indexing, two operations
capitals['Population']['Nauru']


capitals.loc['Palau':'Nauru', ['Population', 'Percentage']]
```

## [pandas.DataFrame.iloc](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iloc.html)
* row-based indexing by integer by position
* Retrieve rows
* Select columns in the same operation
```python
capitals.iloc[5]
capitals.iloc[[4,1]]
capitals.iloc[[4,1], 1:]
capitals.iloc[:,2]
```

## Boolean Filtering
```python
capitals[[True, True, False, True, False]]
capitals['Percentage'] > 25
capitals[capitals['Percentage'] > 25]

# Retrieve all rows where column TEMP > 20
df[df['TEMP'] > 20] 
```
```python

index = ['Mary', 'John', 'Ann', 'Pete', 'Laura'],
columns = ['test_1', 'test_2']

# And you can use lists of booleans with loc and iloc too
# Select all columns with a mean over 6
grades.loc[:, grades.mean() > 5.5]

```

## Assigning Values with Index
* Indexing operators allow you to assign to them
* Update an entire column or row
* Also works with loc, iloc, etc.
* Avoid chianed indexing (use loc/iloc)
```python
grades.loc[['Laura', 'John'], 'test_2'] += 1
grades.loc['Pete'] = [7,8]

# Creating a new column is simple
grades['passed'] = grades.mean(axis=1) > 6

```

## Sorting
* Sort by index
* Sort by a column
* Sort by multiple columns
```python
# To change the original data: use inplace=True
# To sort in reverse, use ascending=False
capitals.sort_index(inplace=True, ascending=False)
capitals

# Or you can sort by multiple columns
grades.sort_values(by=['test_1', 'test_2'])

#Sort rows, not columns
capitals.sort_index(axis=1)

```