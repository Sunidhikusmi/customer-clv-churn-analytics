import pandas as pd

df = pd.read_csv("data/processed/cleaned_data.csv")
df['invoicedate'] = pd.to_datetime(df['invoicedate'])

snapshot_date = df['invoicedate'].max()

last_purchase = df.groupby('customerid')['invoicedate'].max().reset_index()

last_purchase['days_inactive'] = (snapshot_date - last_purchase['invoicedate']).dt.days
last_purchase['churned'] = last_purchase['days_inactive'] > 90

last_purchase.to_csv("data/final/customer_churn.csv", index=False)

print("Churn file created")
