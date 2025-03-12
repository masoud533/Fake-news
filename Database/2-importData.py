import os
import sqlite3
import pandas as pd

conn = sqlite3.connect('news.db')
cursor = conn.cursor()

TrueData = os.path.join('..', 'archive', "True.csv")
df_real = pd.read_csv(TrueData)
df_real["label"] = "real"

print('Read real Data Successful')
print(df_real.info())
print(50 * "=")

FakeData = os.path.join('..', 'archive', "Fake.csv")
df_Fake = pd.read_csv(FakeData)
df_Fake["label"] = "fake"

print('Read Fake Data Successful')
print(df_Fake.info())
print(50 * "=")

df_all = pd.concat([df_real, df_Fake])

print('Concat Data Successful')
print(df_all.info())
print(50 * "=")

df_all.to_sql('news', conn, if_exists="append", index=False)

conn.commit()
conn.close()

print("Data Was Successfully Imported Into The Database.")