"""
This script implements a web crawler for collecting fashion product data and reviews from Tiki.vn.
It uses Selenium with undetected-chromedriver to bypass anti-bot measures and collect data efficiently.
"""

import csv
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from undetected_chromedriver import Chrome, ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import numpy as np
import random

class Crawler:
    def __init__(self, url, driver_path):
        """
        Initialize the Crawler class with the given URL and driver path.
        
        Args:
            url (str): The base URL to start crawling from
            driver_path (str): Path to the ChromeDriver executable
        """
        self.url = url
        self.driver_path = driver_path
        self.hrefs = []  # Store collected product URLs
        self.count = 0   # Track number of comments collected
        self.scroll_pause_time = 2  # Time to wait between scrolls

    def crawl_product_href(self, num_product_pages):
        """
        Crawl the product listing page to collect product links.
        - Scrolls down the page incrementally and clicks 'Load more' to paginate.
        - Collects the hrefs of product links.
        
        Args:
            num_product_pages (int): Number of pages to scroll through and load.
        """
        # Configure Chrome options for stealth crawling
        options = ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--disable-web-security")
        options.add_argument("--incognito")
        options.add_argument("--headless")
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

        # Initialize the Chrome driver with configured options
        self.driver = Chrome(service=Service(self.driver_path), options=options)
        self.driver.get(self.url)
        print("Start collecting product links!")

        # Implement progressive scrolling to load content gradually
        time.sleep(random.uniform(4, 5))  # Random initial wait to appear more human-like
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 4);")
        time.sleep(self.scroll_pause_time)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 2);")
        time.sleep(self.scroll_pause_time)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 4 * 3);")
        time.sleep(self.scroll_pause_time)

        # Load more products by clicking the 'Load more' button
        for i in range(num_product_pages):
            time.sleep(self.scroll_pause_time)
            try:
                # Wait for and click the 'Load more' button
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.styles__Button-sc-143954l-1.gVFXpZ')))
                button = self.driver.find_element(By.CSS_SELECTOR, '.styles__Button-sc-143954l-1.gVFXpZ')
                self.driver.execute_script("arguments[0].click();", button)
            except:
                break  # Exit if no more 'Load more' button is found

        # Collect all product links from the page
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.style__ProductLink-sc-139nb47-2.cKoUly.product-item')))
            links = self.driver.find_elements(By.CSS_SELECTOR, '.style__ProductLink-sc-139nb47-2.cKoUly.product-item')
            self.hrefs = [link.get_attribute('href') for link in links]
        except Exception as e:
            print(e)

        print(f"Finished collecting product links! {len(self.hrefs)} links")
        self.driver.quit()

    def crawl_product_data(self, num_comment_pages):
        """
        Visit each product link to collect product information and comments.
        - Extracts details like title, price, sold quantity, rating, and comments.
        - Handles multiple pages of comments for each product.

        Args:
            num_comment_pages (int): Number of comment pages to crawl per product.
        """
        previous_html = None  # Track page content to detect when no new content is loaded
        
        # Create CSV file to store the crawled data
        with open('raw_data.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Url', 'Title', 'Price', 'Selled Quantity', 'Overall Rating', 'Comment'])

            # Process each product URL
            for index, href in enumerate(self.hrefs, 1):
                print(f"Processing link {index}")
                
                # Configure Chrome options for each product page
                options = ChromeOptions()
                options.add_argument("--disable-blink-features=AutomationControlled")
                options.add_argument("--disable-dev-shm-usage")
                options.add_argument("--no-sandbox")
                options.add_argument("--ignore-certificate-errors")
                options.add_argument("--disable-web-security")
                options.add_argument("--incognito")
                options.add_argument("--headless")
                options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

                # Initialize driver and load product page
                self.driver = Chrome(service=Service(self.driver_path), options=options)
                self.driver.get(href)
                time.sleep(random.uniform(4, 5))

                # Scroll through the product page to load all content
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 4);")
                time.sleep(self.scroll_pause_time)
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 2);")
                time.sleep(self.scroll_pause_time)
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 4 * 3);")
                time.sleep(self.scroll_pause_time)

                # Wait for product title to load
                try:
                    WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.Title__TitledStyled-sc-c64ni5-0.iXccQY')))
                except Exception as e:
                    print(e)

                # Extract product information and comments
                self.get_info_data(href, writer)

                # Navigate through comment pages
                for i in range(1, num_comment_pages):
                    try:
                        current_html = self.driver.page_source

                        # Check if new content is loaded
                        if previous_html and current_html == previous_html:
                            print("No more new content to load! Stop crawling.")
                            break

                        previous_html = current_html

                        # Navigate to next comment page
                        next_button = self.driver.find_element(By.CSS_SELECTOR, '.btn.next')
                        self.driver.execute_script("arguments[0].click();", next_button)
                        time.sleep(self.scroll_pause_time)

                        # Extract data from the new page
                        self.get_info_data(href, writer)

                    except Exception as e:
                        print(f"No more pages to crawl!")
                        break

                self.driver.quit()

    def get_info_data(self, href, writer):
        """
        Helper function to extract product details and comments.
        - Extracts title, price, quantity sold, rating, and user comments.

        Args:
            href (str): The URL of the current product page.
            writer (csv.writer): CSV writer object to save the data.
        """
        # Extract product URL
        try:
            url = self.driver.current_url
        except:
            url = np.nan

        # Extract product title
        try:
            title = self.driver.find_element(By.CSS_SELECTOR, '.Title__TitledStyled-sc-c64ni5-0.iXccQY').text
        except:
            title = np.nan

        # Extract product price
        try:
            price = self.driver.find_element(By.CSS_SELECTOR, '.product-price__current-price').text
        except:
            price = np.nan

        # Extract quantity sold
        try:
            selled_quantity = self.driver.find_element(By.CSS_SELECTOR, '.styles__StyledQuantitySold-sc-1onuk2l-3.eWJdKv').text
        except:
            selled_quantity = np.nan

        # Extract overall rating
        try:
            overall_rating = self.driver.find_element(By.CSS_SELECTOR, 'div.styles__StyledReview-sc-1onuk2l-1.dRFsZg > div:first-child').text
        except:
            overall_rating = np.nan

        # Extract product comments
        try:
            product_comments_element = self.driver.find_elements(By.CSS_SELECTOR, '.review-comment__content')
            product_comments = [comment.text for comment in product_comments_element]
        except:
            print(f"No comment in link: {href}")
            return
        
        # Write each comment to CSV with associated product information
        for comment in product_comments:
            if comment != "":
                self.count += 1
                writer.writerow([url, title, price, selled_quantity, overall_rating, comment])
                print(f"Successfully crawled {self.count}")

# Main execution block
if __name__ == "__main__":
    # Initialize crawler with Tiki.vn sports fashion category URL
    crawler = Crawler("https://tiki.vn/trang-phuc-the-thao/c67647", "C:/Users/Asus/chromedriver_win64/chromedriver.exe")
    
    # Collect product links from 20 pages
    crawler.crawl_product_href(num_product_pages=20)
    
    # Collect data and comments from each product (up to 50 comment pages per product)
    crawler.crawl_product_data(num_comment_pages=50)