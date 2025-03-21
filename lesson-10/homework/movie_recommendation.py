import requests
import json

api_key = 'e23981a5135fbd398db90e13fc03178c'
genre = input("Choose a genre: ")
url = f'https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&with_genres={genre}'
movies = requests.get(url)
nmovies = movies.json()
print(nmovies)