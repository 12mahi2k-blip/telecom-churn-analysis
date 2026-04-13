import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def segment_customers(df: pd.DataFrame, output_dir: str) -> pd.DataFrame:
    """
    Creates tenure groups and generates segmentation visualizations.
    - Creates tenure groups: 0-12, 13-36, 37+
    - Generates pie chart for group distribution
    - Generates bar chart for churn within each group
    """
    print("\nSegmenting customers...")
    os.makedirs(output_dir, exist_ok=True)
    
    # Function to create tenure groups
    def get_tenure_group(tenure):
        if tenure <= 12:
            return '0-12 Months'
        elif tenure <= 36:
            return '13-36 Months'
        else:
            return '37+ Months'
            
    # Apply segmentation
    df['tenure_group'] = df['tenure'].apply(get_tenure_group)
    
    # Group counts
    group_counts = df['tenure_group'].value_counts()
    
    # 1. Pie chart for tenure groups
    plt.figure(figsize=(7, 7))
    plt.pie(group_counts, labels=group_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("pastel"))
    plt.title('Customer Segmentation by Tenure')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'tenure_segmentation_pie.png'))
    plt.close()
    
    # 2. Bar chart for churn by tenure group
    plt.figure(figsize=(8, 5))
    # Order the x-axis logically
    order = ['0-12 Months', '13-36 Months', '37+ Months']
    sns.countplot(data=df, x='tenure_group', hue='churn', palette='Set1', order=order)
    plt.title('Churn by Tenure Group')
    plt.xlabel('Tenure Group')
    plt.ylabel('Count')
    plt.legend(title='Churn')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'churn_by_tenure_bar.png'))
    plt.close()
    
    print(f"Segmentation plots saved to '{output_dir}'.")
    return df
