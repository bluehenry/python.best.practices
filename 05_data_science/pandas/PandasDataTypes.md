# Pandas Data Types
[Overview of Pandas Data Types](https://pbpython.com/pandas_dtypes.html)

# Null
# String (nullable)
* Python: str
* Numpy: np.ojbect

# Integers(non-nullable)
* Python: int
* Numpy: np.int64
```python
number = row['number'] if not math.isnan(row['number']) else 'NULL'
```
# Floats (nullable)
* Python: float
* Numpy: np.float64

# Object
```python
str = row['str'] if row['str'] is not None else None
```
# datetime64
````python
if (row['datetime'] is not None) and (row['datetime'] is not pd.NaT):
    DateApplied = row['datetime']
    strDateApplied = '\'' + DateApplied.strftime('%Y-%m-%d, %H:%M:%S') + '\''
else:
    strDateApplied = 'NULL'
````

# bool/np.bool

# complex/np.complex64