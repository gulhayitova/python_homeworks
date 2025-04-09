import sqlite3
import pandas as pd

# task 1
with sqlite3.connect('chinook.db') as sql_file:
    data = pd.read_sql("SELECT * FROM customers LIMIT 10", sql_file)
    print(data)

# task 2
json_file = pd.read_json('iris.json')
print(json_file.shape)
print(json_file.columns)

# task 3
excel_file = pd.read_excel('titanic.xlsx')
print(excel_file.head())

# task 4
file_name = 'part-00000-aefaf364-d401-4e57-92a5-82fae6fdc855-c000.snappy.parquet'
parquet_data = pd.read_parquet(file_name)
print(parquet_data.info())

# task 5
with open('employee.csv') as file:
    csv_data = pd.read_csv(file)
    print(csv_data.sample(10))