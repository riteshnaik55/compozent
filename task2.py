#Compozent Internship Intermediate task
#Web Scrapping tool

import requests
from bs4 import BeautifulSoup

page = requests.get("https://en.wikipedia.org/wiki/India")
soup = BeautifulSoup(page.content, 'html.parser')
first_h1 = soup.select('h1')[0].text
first_p_text = soup.select('p')[1].text

with open("web_scraping_results.txt", "w", encoding="utf-8") as file:
    file.write("First H1 - " + first_h1 + "\n")
    file.write("First Paragraph - " + first_p_text + "\n")

print("Data saved to web_scraping_results.txt")
