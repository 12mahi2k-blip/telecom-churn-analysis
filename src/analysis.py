import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def advanced_analysis(df: pd.DataFrame, output_dir: str):
    """
    Analyzes churn by demographic and account features via visualizations:
    - Churn by Gender
    - Churn by Contract Type
    - Churn by Payment Method
    """
    print("\nRunning Advanced Analysis...")
    os.makedirs(output_dir, exist_ok=True)
    
    # 1. Churn by Gender
    plt.figure(figsize=(7, 5))
    sns.countplot(data=df, x='gender', hue='churn', palette='Paired')
    plt.title('Churn by Gender')
    plt.xlabel('Gender')
    plt.ylabel('Count')
    plt.legend(title='Churn')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'churn_by_gender.png'))
    plt.close()
    
    # 2. Churn by Contract Type
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x='contract', hue='churn', palette='magma')
    plt.title('Churn by Contract Type')
    plt.xlabel('Contract')
    plt.ylabel('Count')
    plt.legend(title='Churn')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'churn_by_contract.png'))
    plt.close()
    
    # 3. Churn by Payment Method
    plt.figure(figsize=(10, 5))
    sns.countplot(data=df, x='paymentmethod', hue='churn', palette='viridis')
    plt.title('Churn by Payment Method')
    plt.xlabel('Payment Method')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.legend(title='Churn')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'churn_by_payment_method.png'))
    plt.close()
    
    print(f"Advanced analysis plots saved to '{output_dir}'.")
