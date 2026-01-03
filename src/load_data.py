import pandas as pd

# Load dataset
df = pd.read_csv("data/employee_activity.csv")

# Show first 5 rows
print(df.head())

# Show dataset size
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
