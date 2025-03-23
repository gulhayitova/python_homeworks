from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import json
from bs4 import BeautifulSoup

# Set up Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in background
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.demoblaze.com")

# Laptops section
time.sleep(2)
driver.find_element(By.LINK_TEXT, "Laptops").click()
time.sleep(2)

laptops = []  # List to store scraped data

# Loop through pages
while True:
    # Parse page source with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, "html.parser")
    items = soup.find_all("div", class_="card-block")

    for item in items:
        name = item.find("h4", class_="card-title").text.strip()
        price = item.find("h5").text.strip()
        description = item.find("p", class_="card-text").text.strip()
        laptops.append({"name": name, "price": price, "description": description})

    # Check if Next button exists and click it
    try:
        next_button = driver.find_element(By.ID, "next2")
        next_button.click()
        time.sleep(2)  # Wait to load
    except:
        break  # No more pages

# Save to JSON
with open("laptops.json", "w", encoding="utf-8") as f:
    json.dump(laptops, f, indent=4, ensure_ascii=False)

driver.quit()

print("Scraping complete! Data saved in laptops.json")



