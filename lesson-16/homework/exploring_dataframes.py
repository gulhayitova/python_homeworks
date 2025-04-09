import pandas as pd

# task 1
json_file = pd.read_json('iris.json')
columns = json_file.columns
new_columns = [column.lower() for column in columns]
json_file.columns = new_columns
selected = json_file[['sepallength', 'sepalwidth']]

# task 2
excel_file = pd.read_excel('titanic.xlsx')
above_30 = excel_file.query('Age>30')
data = excel_file.value_counts('Sex')
print(data)

# task 3
parquet_file = pd.read_parquet('part-00000-aefaf364-d401-4e57-92a5-82fae6fdc855-c000.snappy.parquet')
print(parquet_file[['Origin', 'Dest', 'Reporting_Airline']])
unique_dest = set(parquet_file['Dest'])
print("The number of unique desinations:", len(unique_dest))

# task 4
csv_file = pd.read_csv('movie.csv')
longer_than_120 = csv_file.query('duration>120')
sorted_csv = csv_file.sort_values('director_facebook_likes', ascending=False)