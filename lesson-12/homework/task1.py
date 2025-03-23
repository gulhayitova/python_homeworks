from bs4 import BeautifulSoup

# Load the HTML file safely
weather_file = 'weather.html'

with open(weather_file, 'r', encoding='ISO-8859-1') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Extract table rows
rows = soup.find_all('tr')[1:]  # Skip the header row

# Process data
weather_data = []
temperatures = []
sunny_days = []
for row in rows:
    columns = row.find_all('td')
    day = columns[0].text.strip()
    temperature = int(columns[1].text.strip().replace('°C', ''))
    condition = columns[2].text.strip()
    weather_data.append({"Day": day, "Temperature": temperature, "Condition": condition})
    temperatures.append(temperature)
    if condition == "Sunny":
        sunny_days.append(day)

# Print extracted data
print("Weather Forecast:")
for entry in weather_data:
    print(f"{entry['Day']}: {entry['Temperature']}°C, {entry['Condition']}")

# Find the day(s) with the highest temperature
if temperatures:
    max_temp = max(temperatures)
    hottest_days = [entry['Day'] for entry in weather_data if entry['Temperature'] == max_temp]
    print(f"\nDay(s) with the highest temperature ({max_temp}°C): {', '.join(hottest_days)}")

    # Print sunny days
    print(f"Day(s) with 'Sunny' condition: {', '.join(sunny_days)}")

    # Calculate and print average temperature
    avg_temp = sum(temperatures) / len(temperatures)
    print(f"\nAverage Temperature for the week: {avg_temp:.2f}°C")
else:
    print("No weather data found in the file.")