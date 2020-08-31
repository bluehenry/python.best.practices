import pandas as pd

# Read data from CSV
df = pd.read_csv('data.csv')

# Print the first row
print(df.head(1))


# Print the last row
print(df.tail(1))