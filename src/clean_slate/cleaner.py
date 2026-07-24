import pandas as pd

def clean_file(file_path):

    #read the CSV file
    try:
        #saved in dataframe
        df = pd.read_csv(file_path)

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

    #FORMATTING COLUMNS

    #strip whitespace from column names
    df.columns = df.columns.str.strip()

    #strip whitespace from columns
    df['Name'] = df['Name'].str.strip()
    df['Email'] = df['Email'].str.strip()
    df['Phone'] = df['Phone'].str.strip()
    df['City'] = df['City'].str.strip()

    #capitalize the first letter of each word in the 'name' column
    df['Name'] = df['Name'].str.title()
    df['City'] = df['City'].str.title()

    #standardize the email column to lowercase
    df['Email'] = df['Email'].str.lower()

    #standardize phone to all text format (remove dashes, spaces, parentheses)
    df['Phone'] = df['Phone'].str.replace(r'[\s\-\(\)]', '', regex=True)


    #Print results
    print("\nFormatted Preview")
    print(df.head())

