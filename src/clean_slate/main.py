import pandas as pd


#read the CSV file
try:
    #saved in dataframe
    df = pd.read_csv('sample_data/testdata.csv')

    print(f"Imported {len(df)} records")
    print("\nColumns")
    print(df.columns.to_list())

    print("\nPreview")
    print(df.head())
    

except FileNotFoundError:
    print("File not found. Please check the file path.")


#REMOVE DUPLICATES

#count original records
original_count = len(df)

df.drop_duplicates(inplace=True)

new_count = len(df)

#summary
print("\n Clean Slate")
print(f"Imported:        {original_count}")
print(f"Duplicates:      {original_count - new_count}")
print(f"Cleaned Records: {new_count}")

