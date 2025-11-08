import time
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://quotes.toscrape.com/")
    time.sleep(5)

# x = page.locator("span.text")
# print(x)
#
# quotes = x.all_inner_texts()
# print(quotes)

