import pandas as pd

def load_data(filepath: str) -> pd.DataFrame:
    print(f"Loading data from {filepath}...")
    
    df = pd.read_csv(filepath, sep=",", engine="python", encoding="latin1", on_bad_lines="skip")
    
    print("\n--- First 10 rows ---")
    print(df.head(10))
    
    print("\n--- Data Types ---")
    print(df.dtypes)
    
    print("\n--- Missing Values ---")
    print(df.isnull().sum())
    
    return df