import pandas as pd

def clean_mall_customers(input_path, output_path):
    """
    Cleans the Mall Customers dataset.

    Steps Performed:
    1. Load dataset
    2. Handle missing values
        - Gender → fill with mode
        - Age → fill with median
        - Spending Score → fill with mean
    3. Standardize column names
    4. Save cleaned dataset
    """

    # Load dataset
    df = pd.read_csv(input_path)

    # Create a copy
    df_clean = df.copy()

    # Fill missing Gender with mode
    if df_clean['Gender'].isnull().sum() > 0:
        df_clean['Gender'] = df_clean['Gender'].fillna(df_clean['Gender'].mode()[0])

    # Fill missing Age with median
    if df_clean['Age'].isnull().sum() > 0:
        df_clean['Age'] = df_clean['Age'].fillna(df_clean['Age'].median())

    # Fill missing Spending Score with mean
    if 'Spending Score (1-100)' in df_clean.columns:
        if df_clean['Spending Score (1-100)'].isnull().sum() > 0:
            df_clean['Spending Score (1-100)'] = df_clean['Spending Score (1-100)'].fillna(
                df_clean['Spending Score (1-100)'].mean()
            )

    # Standardize column names
    df_clean.columns = df_clean.columns.str.lower().str.replace(" ", "_")

    # Save cleaned dataset
    df_clean.to_csv(output_path, index=False)

    print(f"Cleaned dataset saved to: {output_path}")


if __name__ == "__main__":
    # Example usage
    clean_mall_customers(
        input_path="Mall_Customers.csv",
        output_path="mall_customers_cleaned.csv"
    )
