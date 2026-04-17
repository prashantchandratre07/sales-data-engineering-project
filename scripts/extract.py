import pandas as pd

def extract_data():
    # Read CSV file
    df = pd.read_csv('data/sales.csv')
    print("Data Loaded Sucessfully!\n")
    print(df.head())
    return df

if __name__ == "__main__":
    extract_data()