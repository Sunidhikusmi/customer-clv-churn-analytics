import sqlite3
import pandas as pd

conn = sqlite3.connect("data/clv_churn.db")

df = pd.read_csv("data/processed/cleaned_data.csv")
df.to_sql("sales", conn, if_exists="replace", index=False)

clv = pd.read_csv("data/final/customer_clv.csv")
clv.to_sql("clv", conn, if_exists="replace", index=False)

churn = pd.read_csv("data/final/customer_churn.csv")
churn.to_sql("churn", conn, if_exists="replace", index=False)

conn.close()
print("Data loaded into SQLite")
