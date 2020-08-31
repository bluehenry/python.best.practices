# importing pandas as pd
import pandas as pd

# Create the DataFrames from dict
dict = {
    'Date': ['10/2/2011', '11/2/2011', '12/2/2011', '13/2/11'],
    'Event': ['Music', 'Poetry', 'Theatre', 'Comedy'],
    'Cost': [10000, 5000, 15000, 2000]
    }
dataframe = pd.DataFrame(dict)

# Print the dataframe
print(dataframe)


# The Index of this DataFrame was given to us on creation as 0, 1, 2, 3,
print(dataframe.loc[1])
