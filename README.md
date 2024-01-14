# Py-Html-to-csv-converter

This repository contains a Python script for web scraping using Selenium an convert HTML code to csv. The script is designed to be adaptable for various scraping tasks on websites with dynamic content.

## Script Structure

- scraper.py: The main Python script containing the web scraping functionality.
- main.py: Program to call and pass the parameters.
  Call with:

```
python3 main.py
```

- requirements.txt: List of Python libraries required for the script.

## Getting Started

### Prerequisites

- [Python](https://www.python.org/) installed
- [Selenium](https://www.selenium.dev/) library installed (`pip install selenium`)
- Webdriver (e.g., [ChromeDriver](https://sites.google.com/chromium.org/driver/)) installed and its path set in the script

## Install

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

### Script setup

Open scraper.py in your preferred text editor and update the following:

- Web Driver: Set the path to your preferred web driver (e.g., ChromeDriver) in the script.
- CSS Selectors: Customize the CSS selectors in the script to match the structure of the target website. Adjust the selectors used for button clicks, content extraction, and link identification.
- Output Filename: Optionally, change the output filename in the navigate_and_go_back function if needed.

### Output

- The scraped data will be stored in a CSV file named output.csv. Open this file using a spreadsheet application like Excel or Google Sheets for further analysis.
- If you encounter any issues or have suggestions for improvement, please create a [Pull Request](https://github.com/wickenico/py-html-to-csv-converter/pulls). Your feedback is valuable!

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or create a pull request.
