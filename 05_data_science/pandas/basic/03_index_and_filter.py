import pandas as pd
import os

# Load the data
df = pd.read_pickle('data_frame.pickle')

# Get distinct artist
artists = df['artist']
unique_artists = pd.unique(artists)
print(unique_artists)
print(len(unique_artists))

# Filter True/False
s = artists == 'Blake, Robert'
print(s.value_counts)

# Select certain record
# loc: Label, iloc: position
print(df.loc[df['artist']=='Blake, Robert'])
df.loc[1035, 'artist']
print(df.iloc[0, 0])
print(df.iloc[0, :])
print(df.iloc[0:2, 0:2])

# Calculate area
# Convert object to number, data could have string in number row, force NaNs
pd.to_numeric(df['width'], errors='coerce')
df.loc[:, 'width'] = pd.to_numeric(df['width'], errors='coerce')

pd.to_numeric(df['height'], errors='coerce')
df.loc[:, 'height'] = pd.to_numeric(df['height'], errors='coerce')

df['height'] * df['width']
df['units'].value_counts()

# Assign - create a new columns 'area'
area = df['height'] * df['width']
df = df.assign(area=area)

df['area'].max()
df['area'].idxmax()  # Return label
df.loc[df['area'].idxmax(), :]
