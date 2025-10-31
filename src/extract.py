import os
import pandas as pd

RAW_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw')

def load_raw_csv(filename):
    path = os.path.join(RAW_DIR, filename)
    df = pd.read_csv(path)
    return df
