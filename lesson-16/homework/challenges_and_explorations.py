import pandas as pd

json_file = pd.read_json('iris.json')
summary = pd.DataFrame({
    'mean': json_file.mean(numeric_only=True),
    'median': json_file.median(numeric_only=True),
    'std': json_file.std(numeric_only=True)
})

excel_file = pd.read_excel('titanic.xlsx')
print("The sum of ages of the passengers:", excel_file['Age'].sum())
print("The smallest age among the passengers:", excel_file['Age'].min())
print("The biggest age among the passengers:", excel_file['Age'].max())

csv_file = pd.read_csv('movie.csv')
highest_likes = csv_file.sort_values('director_facebook_likes', ascending=False).head(1)
print("\nThe director with the highest facebook likes:", highest_likes['director_name'].values[0])
longest_movies = csv_file.sort_values('duration', ascending=False).head(5)
print('Directors of the longest movies:')
for director in longest_movies['director_name'].fillna("Unknown"):
    print(director)

parquet_file = pd.read_parquet('part-00000-aefaf364-d401-4e57-92a5-82fae6fdc855-c000.snappy.parquet')
parquet_file.fillna(parquet_file.mean(numeric_only=True), inplace=True)