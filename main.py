# web_scraping.py
# -----------------------------
# Project: Web Scraping with BeautifulSoup
# Objective: Extract quotes, authors, and tags from a public website
# Output: Clean data saved as both CSV and Excel files
# -----------------------------

import requests
from bs4 import BeautifulSoup
import pandas as pd
import html

# -----------------------------
# Helper Function to Clean Text
# -----------------------------
def clean_text(text):
    """Remove unwanted characters and fix smart quotes."""
    text = html.unescape(text)  # Convert HTML entities to readable text
    replacements = {
        "“": '"', "”": '"',
        "‘": "'", "’": "'",
        "—": "-", "–": "-",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text.strip()

# -----------------------------
# Step 1: Define the Target URL
# -----------------------------
url = "https://quotes.toscrape.com"

# -----------------------------
# Step 2: Send a GET Request
# -----------------------------
response = requests.get(url)
response.raise_for_status()  # Stop if page not found (e.g., 404)

# -----------------------------
# Step 3: Parse HTML Content
# -----------------------------
soup = BeautifulSoup(response.text, "html.parser")

# -----------------------------
# Step 4: Extract Quotes, Authors, and Tags
# -----------------------------
quotes_data = []
quote_blocks = soup.find_all("div", class_="quote")

for quote in quote_blocks:
    text = clean_text(quote.find("span", class_="text").get_text(strip=True))
    author = clean_text(quote.find("small", class_="author").get_text(strip=True))
    tags = [clean_text(tag.get_text(strip=True)) for tag in quote.find_all("a", class_="tag")]

    quotes_data.append({
        "Quote": text,
        "Author": author,
        "Tags": ", ".join(tags)
    })

# -----------------------------
# Step 5: Convert to DataFrame
# -----------------------------
df = pd.DataFrame(quotes_data)

# -----------------------------
# Step 6: Save Clean Data
# -----------------------------
# Save to CSV (UTF-8 with BOM for Excel compatibility)
df.to_csv("scraped_data.csv", index=False, encoding="utf-8-sig")

# Save to Excel (perfectly formatted)
df.to_excel("scraped_data.xlsx", index=False)

# -----------------------------
# Step 7: Confirmation Message
# -----------------------------
print("✅ Web scraping completed successfully!")
print("📁 Files created:")
print("   → scraped_data.csv")
print("   → scraped_data.xlsx")
