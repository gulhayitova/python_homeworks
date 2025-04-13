import pandas as pd

# 1
titanic = pd.read_excel('titanic.xlsx')
unique_pclass = titanic['Pclass'].drop_duplicates().to_list()
about_titanic = list()
columns = ['Pclass', 'MeanAge', 'TotalFare', 'NumberOfPassengers']

for pclass in sorted(unique_pclass):
    filtered = titanic[titanic['Pclass'] == pclass]
    about_titanic.append([pclass, filtered['Age'].mean(), filtered['Fare'].sum(), filtered.shape[0]])

about_titanic = pd.DataFrame(about_titanic, columns=columns)
print(about_titanic)

# 2
movies = pd.read_csv('movie.csv')
unique_color = movies['color'].dropna().drop_duplicates().to_list()
unique_director = movies['director_name'].dropna().drop_duplicates().to_list()

colors_info = list()
columns_c = ['Color', 'TotalNumCriticForReviews', 'MeanDuration']
for color in unique_color:
    groupedby_color = movies[movies['color'] == color]
    colors_info.append([color, groupedby_color['num_critic_for_reviews'].shape[0], groupedby_color['duration'].mean()])
colors_df = pd.DataFrame(colors_info, columns=columns_c)

directors_info = list()
columns_d = ['Director', 'TotalNumCriticForReviews', 'MeanDuration']
for director in unique_director:
    groupedby_director = movies[movies['director_name'] == director]
    directors_info.append([director, groupedby_director['num_critic_for_reviews'].shape[0], groupedby_director['duration'].mean()])
directors_df = pd.DataFrame(directors_info, columns=columns_d)

flights = pd.read_parquet('part-00000-aefaf364-d401-4e57-92a5-82fae6fdc855-c000.snappy.parquet')

total_flights = dict()
avg_arrdelay = dict()
max_depdelay = dict()

# Not instructed to save in a dataframe, so saving in dictionaries
for (year, month), group in flights.groupby(['Year', 'Month']):
    group = group.copy()
    group['ArrDelay'] = pd.to_numeric(group['ArrDelay'], errors='coerce')
    group['DepDelay'] = pd.to_numeric(group['DepDelay'], errors='coerce')

    total_flights[(int(year), int(month))] = group.shape[0]
    avg_arrdelay[(int(year), int(month))] = group['ArrDelay'].mean()
    max_depdelay[(int(year), int(month))] = group['DepDelay'].max()

for key in sorted(total_flights.keys()):
    y, m = key
    print(f"Year: {y}, Month: {m} - Flights: {total_flights[key]}, Avg Arrival Delay: {avg_arrdelay[key]}, Max Departure Delay: {max_depdelay[key]}")