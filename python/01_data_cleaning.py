import pandas as pd

print("Cleaning started")

df = pd.read_csv("data/raw/online_retail.csv", encoding="ISO-8859-1")

# standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "")

# remove cancelled invoices
df = df[~df['invoice'].astype(str).str.startswith('c')]

# remove missing customers
df = df.dropna(subset=['customerid'])

# remove invalid quantity & price
df = df[(df['quantity'] > 0) & (df['price'] > 0)]

# convert date
df['invoicedate'] = pd.to_datetime(df['invoicedate'], errors='coerce')

# create revenue
df['revenue'] = df['quantity'] * df['price']

print("After cleaning:", df.shape)

df.to_csv("data/processed/cleaned_data.csv", index=False)

print("Cleaning completed")
