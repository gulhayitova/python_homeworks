import requests
import json
import random

with open('api_key_for_movies.txt', 'r') as file: # personal api key stored in a file for privacy reasons
    api_key = file.read()
genre_word = input("Choose a genre: ") # genre name

url_genres = f"https://api.themoviedb.org/3/genre/movie/list?language=en&api_key={api_key}" # getting the genre id
genres = requests.get(url_genres)
genres = genres.json()
genres = genres['genres'] # getting a list of genres
genre_id = ''# creating genre id so it doesn't get an error
for genre in genres:
    if genre['name'] == genre_word:
        genre_id = genre['id']
        break

if genre_id: # if genre id is found
    url = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page={random.randint(1, 100)}&with_genres={genre_id}&api_key={api_key}"
    # a page is chosen randomly to randomize better
    movies = requests.get(url)
    nmovies = movies.json()
    print("\nMovie Title:", nmovies['results'][random.randint(0, 19)]['original_title']) # random movie from 20 movies in the page
    print("Release Date:", nmovies['results'][random.randint(0, 19)]['release_date'])
else: # if genre is not found
    print("Error. Invalid input.")