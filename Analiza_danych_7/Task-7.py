import pandas as pd

# Load data from CSV file
df = pd.read_csv('Analiza_danych_7/cve_result2.csv')

# Convert date column to datetime format
df['published'] = pd.to_datetime(df['published'])

# Extract year from date column and add it to the dataframe
df['year'] = pd.DatetimeIndex(df['published']).year

# Group by year and basescore, and count the number of unique string vectors
result = df.groupby(['year', 'baseScore'])['vectorString'].nunique()

# Convert the result to a dataframe
result_df = result.to_frame().reset_index()

# Save the result to a CSV file
result_df.to_csv('Analiza_danych_7/Task-7_result.csv', index=False)

