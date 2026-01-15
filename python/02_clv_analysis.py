import pandas as pd

df = pd.read_csv("data/processed/cleaned_data.csv")

# CLV calculation
clv = df.groupby('customerid').agg(
    total_revenue=('revenue', 'sum'),
    total_orders=('invoice', 'nunique'),
    avg_order_value=('revenue', 'mean')
).reset_index()

clv.to_csv("data/final/customer_clv.csv", index=False)

print("CLV file created")
