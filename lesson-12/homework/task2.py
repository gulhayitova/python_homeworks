import requests
from bs4 import BeautifulSoup
import sqlite3
import csv


website = 'https://realpython.github.io/fake-jobs'

response = requests.get(website)
connection = sqlite3.connect("jobs.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS jobs(Title TEXT, Company TEXT, Location TEXT, Link TEXT, UNIQUE(Title, Company, Location));")

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    jobs = soup.find_all('div', class_='card-content')
    for job in jobs:
        title = job.find("h2", class_="title").text.strip()
        company = job.find("h3", class_="subtitle is-6 company").text.strip()
        location = job.find("p", class_="location").text.strip()
        # Job description is asked to be provided but there is no description in the website.
        job_link = job.find("a", class_="card-footer-item")["href"]

        cursor.execute(f"INSERT INTO jobs (Title, Company, Location, Link) VALUES (?, ?, ?, ?)", (title, company, location, job_link))

        # Check if job already exists
        cursor.execute("SELECT Link FROM jobs WHERE Title = ? AND Company = ? AND Location = ?", (title, company, location))
        existing_job = cursor.fetchone()

        if existing_job:
            # If job exists but the job link has changed, update it
            if existing_job[0] != job_link:
                cursor.execute('''
                    UPDATE jobs SET Link = ? WHERE Title = ? AND Company = ? AND Location = ?
                ''', (job_link, title, company, location))
        else:
            # Insert new job
            cursor.execute('''
                INSERT INTO jobs (title, company, location, job_link) 
                VALUES (?, ?, ?, ?)
            ''', (title, company, location, job_link))


    print("Jobs stored in the memory successfully!")


#function to filter jobs by company or location
def filter_jobs(filter_by, value):
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    
    query = f"SELECT * FROM jobs WHERE {filter_by} = ?"
    cursor.execute(query, (value,))
    rows = cursor.fetchall()
    conn.close()
    
    return rows

#function to export filtered jobs to CSV
def export_jobs_to_csv(filter_by, value, filename="filtered_jobs.csv"):
    jobs = filter_jobs(filter_by, value)
    
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([ "Title", "Company", "Location", "Job Link"])
        writer.writerows(jobs)
    
    print(f"Jobs exported to {filename} successfully!")




