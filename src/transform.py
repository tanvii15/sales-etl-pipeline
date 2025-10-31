import pandas as pd

def clean_sales_df(df):
    # Standardize column names
    df.columns = [c.strip().lower().replace(' ', '_') for c in df.columns]

    # Parse order date
    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce').dt.date

    # Convert numeric columns
    df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce').fillna(0).astype(int)
    df['unit_price'] = pd.to_numeric(df['unit_price'], errors='coerce').fillna(0.0)

    # Compute total price if missing
    if 'total_price' not in df.columns or df['total_price'].isnull().any():
        df['total_price'] = df['quantity'] * df['unit_price']

    # Drop duplicates
    df = df.drop_duplicates(subset=['order_id'])

    # Fill missing values
    df['region'] = df['region'].fillna('Unknown')
    df['product_name'] = df['product_name'].fillna('Unknown Product')

    return df
