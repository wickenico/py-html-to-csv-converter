from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
    ElementClickInterceptedException,
)
import time, csv


class Scraper:
    def __init__(self, driver):
        self.driver = driver

    def load_page(self, url):
        self.driver.get(url)

    def click_button(self, button_selector, content_selector):
        content = ""
        while True:
            try:
                # Handle the overlay
                overlay_selector = ".onetrust-pc-dark-filter"
                try:
                    overlay = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located(
                            (By.CSS_SELECTOR, overlay_selector)
                        )
                    )
                    self.driver.execute_script(
                        "arguments[0].style.visibility='hidden'", overlay
                    )
                except (NoSuchElementException, TimeoutException):
                    pass  # ignore if the overlay is not found

                # Click the button
                button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, button_selector))
                )
                button.click()
                time.sleep(2)  # wait for the page to load
                new_content = self.driver.find_element(
                    By.CSS_SELECTOR, content_selector
                ).get_attribute("innerHTML")
                print(f"New content: {new_content}")  # print the new content
                content += new_content
            except (
                NoSuchElementException,
                TimeoutException,
                ElementClickInterceptedException,
            ) as e:
                print(f"Exception: {e}")  # print the exception
                break
        print(f"Total content: {content}")  # print the total content
        return content

    def navigate_and_go_back(self, link_selector, button_selector, content_selector):
        with open("output.csv", "w", newline="") as f:
            writer = csv.writer(f, delimiter=";")  # use semicolon as delimiter
            writer.writerow(
                ["Seller", "Feedback Link", "Address", "Phone"]
            )  # write the header

            visited_links = set()  # keep track of visited links

            while True:
                # Find all the links
                links = self.driver.find_elements(By.CSS_SELECTOR, link_selector)

                for link in links:
                    url = link.get_attribute("href")

                    if url in visited_links:
                        continue

                    visited_links.add(url)  # mark this link as visited

                    # Navigate to the link using JavaScript
                    self.driver.execute_script("arguments[0].click();", link)
                    time.sleep(2)  # wait for the page to load

                    # Extract the seller's name and the feedback link
                    try:
                        seller_name = self.driver.find_element(
                            By.CSS_SELECTOR, ".seller-name"
                        ).text
                    except NoSuchElementException:
                        seller_name = "Not found"

                    try:
                        feedback_link = self.driver.find_element(
                            By.CSS_SELECTOR, ".seller-feedback a"
                        ).get_attribute("href")
                    except NoSuchElementException:
                        feedback_link = "Not found"

                    try:
                        address = self.driver.find_element(
                            By.CSS_SELECTOR, ".address address"
                        ).text.replace("\n", " ")
                    except NoSuchElementException:
                        address = "Not found"

                    try:
                        phone = self.driver.find_element(
                            By.CSS_SELECTOR, ".phone"
                        ).text.split("\n")[
                            -1
                        ]  # get the last line of the phone div
                    except NoSuchElementException:
                        phone = "Not found"

                    writer.writerow(
                        [seller_name, feedback_link, address, phone]
                    )  # write the data

                    # Go back to the previous page
                    self.driver.back()
                    time.sleep(2)  # wait for the page to load

                # Click the "Load More" button
                try:
                    load_more_button = WebDriverWait(self.driver, 20).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, button_selector))
                    )
                    self.driver.execute_script(
                        "arguments[0].click();", load_more_button
                    )
                    time.sleep(5)  # wait for the page to load
                except (NoSuchElementException, TimeoutException):
                    break  # exit the loop if the "Load More" button is not found

    def write_content_to_file(self, content, filename):
        print(f"Writing to file: {filename}")  # print the filename
        with open(filename, "w") as f:
            f.write(content)
        print("Done writing to file")  # print a message when done writing to the file

    def quit(self):
        self.driver.quit()
