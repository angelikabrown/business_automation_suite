import pandas as pd



try:

    df = pd.read_csv('sample_data/testdata.csv')

    print(f"Imported {len(df)} records")
    print("\nColumns")
    print(df.columns.to_list())

    print("\nPreview")
    print(df.head())
    

except FileNotFoundError:
    print("File not found. Please check the file path.")

