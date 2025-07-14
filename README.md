# 🏠 Apartment Rental Scraper and Form Automation

This project is a Python script that scrapes apartment rental listings (addresses, prices, and links) from Zillow (or similar rental websites) using **BeautifulSoup** and **Selenium**, and then automatically fills out a form for each listing.

---

## 🚀 Features

✅ Scrapes:
- 📍 Address (cleaned, without complex names)
- 💰 Price (cleaned, only the dollar amount)
- 🔗 Link to the listing

✅ Cleans data (removes empty entries and duplicates)

✅ Automates form submissions using Selenium

---

## 💻 Technologies Used

- **Python**
- **BeautifulSoup** for parsing HTML
- **Selenium** for browser automation
- **Requests** for fetching website content

---

## ⚙️ Setup Instructions

1️⃣ **Clone this repository**

```bash
git clone https://github.com/YOUR_USERNAME/rental.git
cd rental

pip install selenium beautifulsoup4 requests

python main.py

This project is open source — feel free to fork it and adapt it!

