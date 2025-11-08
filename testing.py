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

# Step 1: Find all quotes on the page
quotes = soup.find_all('span', class_='text')

# print(quotes)

# Step 2: Print a random quote
import random
random_quote = random.choice(quotes)
print("Random Quote:", random_quote.text)