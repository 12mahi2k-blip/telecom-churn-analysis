# 📊 Customer Churn Analysis Project

## 📖 Overview
This project provides a comprehensive and professional pipeline for analyzing customer churn using the Telco Customer Churn dataset. It demonstrates essential data science practices including data extraction, cleaning, exploratory data analysis, and customer segmentation to extract actionable insights.

## 🎯 Objectives
- Understand the underlying patterns and reasons why customers churn.
- Clean and preprocess raw telco dataset for robust analysis.
- Visualize demographics, payment structures, and account features to spot trends.
- Perform targeted customer segmentation based on tenure.

## 🛠 Steps Included
1. **Data Loading:** Initial dataset ingestion and understanding of shape, datatypes, and missing fields.
2. **Data Cleaning:** Standardize parameters, eliminate duplicated records, and fill/drop NA values.
3. **Exploratory Data Analysis (EDA):** Broad feature analysis via summary statistics, histograms, and boxplots to visualize distribution boundaries.
4. **Customer Segmentation:** Creating logical customer segments (`0-12 months`, `13-36 months`, `37+ months`) and profiling survival rates.
5. **Advanced Analysis:** Drilling down into churn drivers associated with gender, contract type, and chosen payment method.

## 💡 Key Insights
- Customers with **Month-to-Month contracts** usually depict a higher churn rate compared to one or two-year subscribers.
- New customers (especially in the `0-12 Months` group) are more volatile and typically at a high risk of churning.
- Payment methods like explicitly **Electronic check** usually correlate with higher churn ratios indicating potential user friction points.

## 🚀 How to Run

### 1. Setup the Environment
Ensure your environment meets the prerequisites by installing required libraries:
```bash
pip install -r requirements.txt
```

### 2. Verify Data Location
Make sure your given `Telco_Customer_Churn.csv` file is properly placed inside the `data/` directory.

### 3. Run the Automated Pipeline
You can trigger the entire modular pipeline by executing the main script from the root folder:
```bash
python main.py
```
*Note: Running `main.py` will automatically produce standard charts and save them in the `outputs/charts/` area.*

### 4. Interactive Analysis
For a deeply interactive and beginner-friendly walkthrough of the step-by-step logic, open the Jupyter Notebook:
```bash
jupyter notebook notebook/churn_analysis.ipynb
```
