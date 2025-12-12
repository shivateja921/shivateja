import pandas as pd

def clean_mall_customers(input_path, output_path):
  

   
    df = pd.read_csv(input_path)

    
    df_clean = df.copy()

   
    if df_clean['Gender'].isnull().sum() > 0:
        df_clean['Gender'] = df_clean['Gender'].fillna(df_clean['Gender'].mode()[0])

    
    if df_clean['Age'].isnull().sum() > 0:
        df_clean['Age'] = df_clean['Age'].fillna(df_clean['Age'].median())

  
    if 'Spending Score (1-100)' in df_clean.columns:
        if df_clean['Spending Score (1-100)'].isnull().sum() > 0:
            df_clean['Spending Score (1-100)'] = df_clean['Spending Score (1-100)'].fillna(
                df_clean['Spending Score (1-100)'].mean()
            )


    df_clean.columns = df_clean.columns.str.lower().str.replace(" ", "_")

  
    df_clean.to_csv(output_path, index=False)

    print(f"Cleaned dataset saved to: {output_path}")


if __name__ == "__main__":

    clean_mall_customers(
        input_path="Mall_Customers.csv",
        output_path="mall_customers_cleaned.csv"
    )

