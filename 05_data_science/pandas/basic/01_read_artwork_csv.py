import os
import pandas as pd

CSV_PATH = os.path.join('.', 'collection-master', 'artwork_data.csv')

# Read just 5 rows
df = pd.read_csv(CSV_PATH, nrows=5)

# Specify an INdex
df = pd.read_csv(CSV_PATH, nrows=5, index_col='id')

# Limit columns
df = pd.read_csv(CSV_PATH, nrows=5, index_col='id', usecols=['id', 'artist'])

# All columns that we need
COLS_TO_USE = ['id', 'artist',
               'title', 'medium', 'year',
               'acquisitionYear', 'height',
               'width', 'units']

# Proper data loading
df = pd.read_csv(CSV_PATH,
                 usecols=COLS_TO_USE,
                 index_col='id',
                 low_memory=False)

# Save for later
df.to_pickle(os.path.join('.', 'data_frame.pickle'))
