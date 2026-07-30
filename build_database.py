import sqlite3
import pandas as pd

df = pd.read_csv("dataset.csv")

conn = sqlite3.connect("wpl_database.db")
df.to_sql("matches", conn, if_exists="replace", index=False)
conn.close()

print("wpl_database.db created with 'matches' table:", len(df), "rows")
