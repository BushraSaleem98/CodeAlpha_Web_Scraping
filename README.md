# Web Scraping Project

## Project Overview
This project demonstrates a simple Python web scraping script that collects motivational quotes from a website and stores them in a clean, structured Excel file. It extracts the Quote, Author, and Tags for each entry and ensures proper text formatting and encoding for smooth Excel compatibility.

## Description
The script (`main.py`) uses the BeautifulSoup and Requests libraries to scrape data efficiently, and pandas to save it in a readable, tabular format inside `scraped_data.xlsx`. All unwanted characters like “â€œ” or “â€” are automatically removed during processing.

## Files Included
| File Name | Description |
|------------|-------------|
| [main.py](https://github.com/BushraSaleem98/CodeAlpha_Web_Scraping/blob/main/main.py) | Python script for scraping and saving the data |
| scraped_data.xlsx | Excel file containing cleaned quote data in columns: Quote, Author, and Tags |
| README.md | Documentation for the project |

## Requirements
Before running the project, install the required Python libraries:
`pip install requests beautifulsoup4 pandas openpyxl`

## How to Run
1. Clone the repository:  
   `git clone https://github.com/BushraSaleem98/CodeAlpha_Web_Scraping.git`  
2. Navigate into the project folder:  
   `cd CodeAlpha_Web_Scraping`  
3. Run the Python script:  
   `python main.py`  
4. View the output in `scraped_data.xlsx`, which will be generated in the same directory.

## Output Example
| Quote | Author | Tags |
|--------|---------|------|
| The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking. | Albert Einstein | change, deep-thoughts, thinking, world |
| It is our choices, Harry, that show what we truly are, far more than our abilities. | J.K. Rowling | abilities, choices |

## Author
**Bushra Saleem**  
[GitHub Repository](https://github.com/BushraSaleem98/CodeAlpha_Web_Scraping)

## Project Highlights
- Clean Excel formatting  
- UTF-8 encoding for readable text  
- Automated quote extraction  
- Beginner-friendly Python implementation  

A small but powerful step into the world of web scraping and data automation.
