import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')

def get_engine():
    uri = f"mysql+mysqlconnector://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
    return create_engine(uri)

def load_df_to_db(df, table_name='orders', if_exists='append'):
    engine = get_engine()
    df.to_sql(name=table_name, con=engine, if_exists=if_exists, index=False, chunksize=1000)
