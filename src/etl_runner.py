from extract import load_raw_csv
from transform import clean_sales_df
from load import load_df_to_db
import sys

def run_etl(file_name):
    df_raw = load_raw_csv(file_name)
    df_clean = clean_sales_df(df_raw)
    load_df_to_db(df_clean)
    print(f"Loaded {len(df_clean)} rows from {file_name} into MySQL successfully.")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python src/etl_runner.py <filename>")
    else:
        run_etl(sys.argv[1])
