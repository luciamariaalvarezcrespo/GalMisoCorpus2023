# Author: Lucía María Álvarez Crespo (GitHub: @luciamariaalvarezcrespo)
# Last modified: 26/06/2023
# Description: Get all public tweets given a list of tweet IDs and save them to a CSV file
# Python version: 3.10.6

import time
import csv
import os
from pyvirtualdisplay import Display
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium import webdriver
from webdriver_manager.core.utils import ChromeType
from webdriver_manager.chrome import ChromeDriverManager

def get_tweet_ids(file_path):
    """
    Read tweet IDs from a file.

    Args:
        file_path (str): The path to the file containing tweet IDs.

    Returns:
        list: A list of tweet IDs.

    """
    with open(file_path, 'r', encoding='utf-8') as f:
        tweet_ids = f.read().splitlines()
    return tweet_ids


def save_tweet_to_csv(tweet_id, tweet_text, output_file):
    """
    Save a tweet to a CSV file.

    Args:
        tweet_id (str): The ID of the tweet.
        tweet_text (str): The text content of the tweet.
        output_file (str): The path to the CSV file.

    """
    with open(output_file, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([tweet_id, tweet_text])

def scrape_tweets(tweet_ids, output_file):
    """
    Scrape tweets given a list of tweet IDs and save them to a CSV file.

    Args:
        tweet_ids (list): A list of tweet IDs.
        output_file (str): The path to the output CSV file.

    """
    display = Display(visible=0, size=(800, 600))
    display.start()

    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument('--headless')
    options.add_argument("--remote-debugging-port=9222")
    options.binary_location = "/usr/bin/chromium-browser"

    driver = webdriver.Chrome(options=options, service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

    for tweet_id in tweet_ids:
        url = f'https://twitter.com/anyone/status/{tweet_id}'
        driver.get(url)
        time.sleep(5)

        text_elements = driver.find_elements(By.CSS_SELECTOR, '[data-testid="tweetText"]')

        if len(text_elements) != 0:
            tweet_text = " [response] ".join([t.text for t in text_elements])
            save_tweet_to_csv(tweet_id, tweet_text, output_file)

    driver.quit()
    display.stop()

if __name__ == '__main__':
    tweet_ids_file = os.path.dirname(__file__) + "/../MisoCorpus/sela-spain-misogyny.txt" # Change this path to the file containing the tweet IDs
    output_csv_file = os.path.dirname(__file__) + "/../data/tweets.csv"
    tweet_ids = get_tweet_ids(tweet_ids_file)
    scrape_tweets(tweet_ids, output_csv_file)
