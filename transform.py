import pandas as pd
from extract import extract_data

def transform_data():
    df = extract_data()

    # ✅ ADD HERE (with proper indentation)
    print("Total columns:", len(df.columns))

    print("\n🔄 Transforming real dataset...\n")

    df.columns = [
        "area_code", "state", "market", "market_size", "profit", "margin",
        "sales", "cogs", "total_expenses", "marketing", "inventory",
        "budget_profit", "budget_cogs", "budget_margin", "budget_sales",
        "product_id", "date", "product_type", "product", "product_types"
    ]

    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df = df.drop_duplicates()
    df = df.fillna(0)

    print("✅ Data Cleaned Successfully!\n")
    print(df.head())

    return df

if __name__ == "__main__":
    transform_data()