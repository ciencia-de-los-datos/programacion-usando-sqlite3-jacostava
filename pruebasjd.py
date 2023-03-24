import sqlite3
import sys

import pandas as pd


conn = sqlite3.connect(":memory:")
cur = conn.cursor()

with open("create_tables.sql", encoding="utf-8") as file:
    cur.executescript(file.read())

df = pd.read_sql("select SUM(c12) from tbl1;", con=conn)
print(df)