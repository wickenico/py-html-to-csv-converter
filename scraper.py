from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
    ElementClickInterceptedException,
)
import csv
import time


class Scraper:
    def __init__(self, driver):
        self.driver = driver

    def load_page(self, url):
        self.driver.get(url)

    def handle_overlay(self, overlay_selector):
        try:
            overlay = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, overlay_selector))
            )
            self.driver.execute_script(
                "arguments[0].style.visibility='hidden'", overlay
            )
        except (NoSuchElementException, TimeoutException):
            pass  # ignore if the overlay is not found

    def click_button(self, button_selector, content_selector):
        content = ""
        while True:
            self.handle_overlay(".onetrust-pc-dark-filter")

            try:
                button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, button_selector))
                )
                button.click()
                time.sleep(2)  # wait for the page to load

                new_content = self.driver.find_element(
                    By.CSS_SELECTOR, content_selector
                ).get_attribute("innerHTML")
                content += new_content
            except (
                NoSuchElementException,
                TimeoutException,
                ElementClickInterceptedException,
            ):
                break

        return content

    def navigate_and_go_back(self, link_selector, button_selector, content_selector):
        with open("output.csv", "w", newline="") as f:
            writer = csv.writer(f, delimiter=";")  # use semicolon as delimiter
            writer.writerow(
                ["Seller", "Link", "Address", "Phone"]
            )  # write the column header

            visited_links = set()

            while True:
                links = self.driver.find_elements(By.CSS_SELECTOR, link_selector)

                for link in links:
                    url = link.get_attribute("href")

                    if url in visited_links:
                        continue

                    visited_links.add(url)

                    self.driver.execute_script("arguments[0].click();", link)
                    time.sleep(2)  # wait for the page to load

                    seller_name = self.get_text(".seller-name")
                    feedback_link = self.get_attribute(".seller-feedback a", "href")
                    address = self.get_text(".address address").replace("\n", " ")
                    phone = self.get_text(".phone").split("\n")[-1]

                    writer.writerow([seller_name, feedback_link, address, phone])

                    self.driver.back()
                    time.sleep(2)  # wait for the page to load

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

    def get_text(self, selector):
        try:
            return self.driver.find_element(By.CSS_SELECTOR, selector).text
        except NoSuchElementException:
            return "Not found"

    def get_attribute(self, selector, attribute):
        try:
            return self.driver.find_element(By.CSS_SELECTOR, selector).get_attribute(
                attribute
            )
        except NoSuchElementException:
            return "Not found"

    def write_content_to_file(self, content, filename):
        with open(filename, "w") as f:
            f.write(content)

    def quit(self):
        self.driver.quit()
