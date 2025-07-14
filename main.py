from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

import requests
from bs4 import BeautifulSoup
import re

# Step 1: Send an HTTP request to the webpage
url = 'https://appbrewery.github.io/Zillow-Clone/'
response = requests.get(url)

# Step 2: Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Find all links
links = soup.find_all('a', attrs={"data-test":"property-card-link"})
unique_links = set()

link_list = []
price_list = []

for link_tag in links:
    href = link_tag.get("href")
    if href.startswith("https"):
        full_link = href
    else:
        full_link = "https://www.zillow.com" + href
    unique_links.add(full_link)
    link_list.append(full_link)


# Step 4: Find all address
address_list = [
    addr_tag.get_text(strip=True).split("|")[1].strip()
    if "|" in addr_tag.get_text(strip=True)
    else addr_tag.get_text(strip=True).strip()
    for addr_tag in soup.find_all('address', attrs={"data-test": "property-card-addr"})
    if addr_tag.get_text(strip=True).strip() != ""
]

# Step 5: Find all prices
price_tag = soup.find_all('span', attrs={"data-test":"property-card-price"})
for tag in price_tag:
    raw_price = tag.get_text(strip=True)
    match = re.search(r"\$\d[\d,]*", raw_price)
    if match:
        clean_price = match.group()
        price_list.append(clean_price)

# Setup Chrome driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSc_DrfI6M_AOYInw3g8LUb7CvkVMzyHyGXSVOIW3tqAWpqA0Q/viewform")
sleep(3)

wait = WebDriverWait(driver, 10)

for address, price, link in zip(address_list, price_list, link_list):
    address_field = driver.find_element(By.CSS_SELECTOR, "input[aria-labelledby='i1 i4']")
    price_field = driver.find_element(By.CSS_SELECTOR, "input[aria-labelledby='i6 i9']")
    link_field = driver.find_element(By.CSS_SELECTOR, "input[aria-labelledby='i11 i14']")

    # Clear (optional, but recommended)
    address_field.clear()
    price_field.clear()
    link_field.clear()

    # Fill fields
    address_field.send_keys(address)
    price_field.send_keys(price)
    link_field.send_keys(link)

    submit_button = driver.find_element(By.CSS_SELECTOR, "div.uArJ5e.UQuaGc.Y5sE8d.VkkpIf.QvWxOd")
    submit_button.click()

    another_response_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Submit another response")))
    another_response_link.click()


print("✅ Done! Browser closed.")
driver.quit()

