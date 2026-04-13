import os
import sys

# Ensure the 'src' module can be imported correctly
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.data_loading import load_data 
from src.data_cleaning import clean_data
from src.eda import perform_eda
from src.segmentation import segment_customers
from src.analysis import advanced_analysis

def main():
    print("=== Starting Customer Churn Analysis Pipeline ===")
    
    data_path = os.path.join('data', 'Telco_Customer_Churn.csv')
    charts_output_dir = os.path.join('outputs', 'charts')
    reports_output_dir = os.path.join('outputs', 'reports')
    
    # Ensure standard output directories exist
    os.makedirs(charts_output_dir, exist_ok=True)
    os.makedirs(reports_output_dir, exist_ok=True)
    
    # Check if data file exists
    if not os.path.exists(data_path):
        print(f"Error: Dataset not found at {data_path}. Please check the path and try again.")
        return
        
    # Step 1: Data Understanding
    df = load_data(filepath=data_path)
    
    # Step 2: Data Cleaning
    df_cleaned = clean_data(df=df)
    
    # Step 3: Exploratory Data Analysis
    perform_eda(df=df_cleaned, output_dir=charts_output_dir)
    
    # Step 4: Customer Segmentation
    df_segmented = segment_customers(df=df_cleaned, output_dir=charts_output_dir)
    
    # Step 5: Advanced Analysis
    advanced_analysis(df=df_segmented, output_dir=charts_output_dir)
    
    print("\n=== Pipeline Execution Completed Successfully! ===")
    print(f"Please check the '{charts_output_dir}' directory for all generated visualisations.")

if __name__ == '__main__':
    main()
