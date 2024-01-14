# Py-Html-to-csv-converter

This project is a web scraper that uses Selenium to scrape data from a website and convert it to csv for excel import.

## Requirements

- Python 3.7+
- Selenium
- ChromeDriver

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/wickenico/py-html-to-csv-converter.git
   ```
2. Install the requirements:
   ```
   pip install -r requirements.txt
   ```
3. Download the [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) that matches your Chrome version and put it in your PATH.

## Usage

1. Import the `Scraper` class from `scraper.py`:
   ```python
   from scraper import Scraper
   ```
2. Create a new `Scraper` instance:
   ```python
   scraper = Scraper(driver)
   ```
3. Load a page:
   ```python
   scraper.load_page('https://example.com')
   ```
4. Click a button and get the content:
   ```python
   scraper.click_button('.button-selector', '.content-selector')
   ```
