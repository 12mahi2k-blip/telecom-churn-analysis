import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def perform_eda(df: pd.DataFrame, output_dir: str):
    """
    Performs Exploratory Data Analysis and saves plots to the output directory.
    - Summary Statistics
    - Histograms
    - Boxplots
    - Churn Distribution
    """
    print("\nPerforming EDA...")
    os.makedirs(output_dir, exist_ok=True)
    
    # 1. Summary Statistics
    print("\n--- Summary Statistics ---")
    print(df.describe())
    
    # Use seaborn styling
    sns.set_theme(style="whitegrid")
    
    # 2. Histogram of Monthly Charges
    plt.figure(figsize=(8, 5))
    sns.histplot(data=df, x='monthlycharges', bins=30, kde=True, color='skyblue')
    plt.title('Distribution of Monthly Charges')
    plt.xlabel('Monthly Charges')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'monthly_charges_hist.png'))
    plt.close()
    
    # 3. Boxplot of Tenure
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=df, x='tenure', color='lightgreen')
    plt.title('Boxplot of Customer Tenure')
    plt.xlabel('Tenure (Months)')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'tenure_boxplot.png'))
    plt.close()
    
    # 4. Churn Distribution
    plt.figure(figsize=(6, 5))
    sns.countplot(data=df, x='churn', palette='Set2')
    plt.title('Customer Churn Distribution')
    plt.xlabel('Churn Status')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'churn_distribution.png'))
    plt.close()
    
    print(f"EDA plots saved to '{output_dir}'.")
