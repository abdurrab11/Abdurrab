import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from concurrent.futures import ThreadPoolExecutor
import logging
from cryptography.fernet import Fernet
import json
import time
import os

# Set up logging
logging.basicConfig(filename='advanced_script.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Encryption key for sensitive data
ENCRYPTION_KEY = Fernet.generate_key()
cipher_suite = Fernet(ENCRYPTION_KEY)

# Function to encrypt data
def encrypt_data(data):
    return cipher_suite.encrypt(data.encode())

# Function to decrypt data
def decrypt_data(encrypted_data):
    return cipher_suite.decrypt(encrypted_data).decode()

# Function to scrape data from a website
def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        titles = [title.text for title in soup.find_all('h2')]
        logging.info(f"Scraped {len(titles)} titles from {url}")
        return titles
    except Exception as e:
        logging.error(f"Error scraping {url}: {e}")
        return []

# Function to interact with an API
def fetch_api_data(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        logging.info(f"Fetched data from API: {api_url}")
        return data
    except Exception as e:
        logging.error(f"Error fetching API data: {e}")
        return {}

# Function to automate browser tasks using Selenium
def automate_browser(url):
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # Run in headless mode
        service = Service(executable_path='/path/to/chromedriver')  # Update with your chromedriver path
        driver = webdriver.Chrome(service=service, options=options)
        driver.get(url)
        time.sleep(3)  # Wait for page to load
        element = driver.find_element(By.TAG_NAME, 'h1')
        logging.info(f"Automated browser fetched element: {element.text}")
        driver.quit()
        return element.text
    except Exception as e:
        logging.error(f"Error automating browser: {e}")
        return None

# Function to process data using pandas
def process_data(data):
    try:
        df = pd.DataFrame(data, columns=['Title'])
        df['Length'] = df['Title'].apply(len)
        logging.info("Processed data using pandas")
        return df
    except Exception as e:
        logging.error(f"Error processing data: {e}")
        return pd.DataFrame()

# Function to save data to a file
def save_data(data, filename):
    try:
        if filename.endswith('.csv'):
            data.to_csv(filename, index=False)
        elif filename.endswith('.json'):
            with open(filename, 'w') as f:
                json.dump(data, f)
        logging.info(f"Data saved to {filename}")
    except Exception as e:
        logging.error(f"Error saving data to {filename}: {e}")

# Main function to run all tasks
def main():
    # URLs and API endpoints
    website_url = 'https://example.com'
    api_url = 'https://api.example.com/data'
    browser_url = 'https://example.com'

    # Scrape website data
    scraped_data = scrape_website(website_url)

    # Fetch API data
    api_data = fetch_api_data(api_url)

    # Automate browser tasks
    browser_data = automate_browser(browser_url)

    # Process scraped data
    processed_data = process_data({'Title': scraped_data})

    # Save processed data to a CSV file
    save_data(processed_data, 'output.csv')

    # Encrypt sensitive data
    sensitive_data = "This is a secret message."
    encrypted_data = encrypt_data(sensitive_data)
    logging.info(f"Encrypted data: {encrypted_data}")

    # Decrypt sensitive data
    decrypted_data = decrypt_data(encrypted_data)
    logging.info(f"Decrypted data: {decrypted_data}")

    # Use multithreading for parallel tasks
    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.submit(scrape_website, website_url)
        executor.submit(fetch_api_data, api_url)
        executor.submit(automate_browser, browser_url)

if __name__ == "__main__":
    main()