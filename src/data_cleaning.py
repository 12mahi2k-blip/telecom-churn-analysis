import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans DataFrame: drops duplicates, handles missing values, standardizes column names.
    """
    print("\nCleaning data...")
    
    # Standardize column names (lowercase, replace spaces with underscores)
    df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
    
    # Remove duplicates
    initial_shape = df.shape
    df = df.drop_duplicates()
    print(f"Removed {initial_shape[0] - df.shape[0]} duplicate rows.")
    
    # Handle missing values (e.g., 'totalcharges' can be blank for brand new customers)
    if 'totalcharges' in df.columns:
        df['totalcharges'] = pd.to_numeric(df['totalcharges'], errors='coerce')
        # Fill missing numeric totalcharges with 0
        df['totalcharges'] = df['totalcharges'].fillna(0)
    
    # Drop any other rows with complete missing necessary values if required
    df = df.dropna()
    print("Data cleaning complete.")
    
    return df
