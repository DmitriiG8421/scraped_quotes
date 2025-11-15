import requests
from bs4 import BeautifulSoup

# Step 1: Send a request to Google's homepage
url = "https://quotes.toscrape.com/"
response = requests.get(url)

# Step 2: Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Extract and print the title
title = soup.title.text
print("The title of the page is:", title)

# Step 1: Find all authors on the page
author = soup.find_all('small', class_='author')

for i in set(author):
 print(i.text)

