import pandas as pd

# passing through database connection
df = pd.read_sql_query("SELECT * FROM purchases", connection)