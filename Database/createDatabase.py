import os
import sqlite3
import pandas as pd

# path to the folder containing the csv file
DataPath = os.path.join('..','archive')

# Connect to the SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect('fake-news.db')
print("Database creation was successful")
cursor = conn.cursor()

for filename in os.listdir(DataPath):
    if filename.endswith('.csv'): # check if the file is a CSV file
        

        csvPath = os.path.join(DataPath, filename)
        df = pd.read_csv(csvPath)

        #Create a table name frome the filemane (without extension)
        tableName = filename.split('.')[0]

        #insert the data into the SQLite database as a table
        df.to_sql(tableName,conn,if_exists="replace",index=False)
        print(f"table {tableName} Created")

conn.close()
