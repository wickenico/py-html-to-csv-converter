from selenium import webdriver
from scraper import Scraper

# Initialize the driver
driver = webdriver.Chrome()  # or webdriver.Firefox(), etc.

scraper = Scraper(driver)
scraper.load_page("https://www.ebay-deine-stadt.de/ortenau/search-seller?")
scraper.navigate_and_go_back(
    ".seller-wrapper a.arrow-link", "span.button.load-more", ".sellers-list-grid"
)  # navigate to each link, go back, and click the "load more" button
scraper.quit()
