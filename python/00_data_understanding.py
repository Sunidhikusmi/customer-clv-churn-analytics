import pandas as pd

df = pd.read_csv("data/raw/online_retail.csv", encoding="ISO-8859-1")

df.columns = df.columns.str.strip().str.lower().str.replace(" ", "")

print("Columns:", df.columns.tolist())
print("Rows, Columns:", df.shape)
print("Date range:", df['invoicedate'].min(), "to", df['invoicedate'].max())
