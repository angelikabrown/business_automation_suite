import pandas as pd


df = pd.read_csv('sample_data/testdata.csv')

if df.empty:
    print("The DataFrame is empty.")

print(df.head())

