import pandas as pd

def clean_mall_customers(input_path, output_path):
    df = pd.read_csv(input_path)
    df_clean = df.copy()

    duplicates_count = df_clean.duplicated().sum()
    df_clean.drop_duplicates(inplace=True)

    if 'Gender' in df_clean.columns and df_clean['Gender'].isnull().sum() > 0:
        df_clean['Gender'] = df_clean['Gender'].fillna(df_clean['Gender'].mode()[0])

    if 'Gender' in df_clean.columns:
        df_clean['Gender'] = df_clean['Gender'].str.strip().str.title()

    numeric_cols = df_clean.select_dtypes(include='number').columns
    for col in numeric_cols:
        df_clean[col] = df_clean[col].fillna(df_clean[col].median())

    df_clean.columns = df_clean.columns.str.lower().str.replace(" ", "_")
    df_clean.to_csv(output_path, index=False)

    print(f"Cleaned dataset saved to: {output_path}")
    print("Missing values after cleaning:\n", df_clean.isnull().sum())
    print(f"Duplicates removed: {duplicates_count}")
    print(f"Dataset shape: {df_clean.shape}")


if __name__ == "__main__":
    clean_mall_customers(
        input_path="Mall_Customers.csv",
        output_path="mall_customers_cleaned.csv"
    )
