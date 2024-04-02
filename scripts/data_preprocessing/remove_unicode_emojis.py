# Author: Lucía María Álvarez Crespo (GitHub: @luciamariaalvarezcrespo)
# Last modified: 01/04/2024
# Description: Remove emojis and HTML tags from the 'content' field of the toots
# Python version: 3.10.6
# License: Mozilla Public License Version 2.0

import csv
import os
import re
import emoji

from bs4 import BeautifulSoup
from mastodon import Mastodon

# Instantiate Mastodon object
mastodon = Mastodon(access_token='YOUR_ACCESS_TOKEN_HERE', api_base_url='https://mastodon.gal') # Change this to the instance you want to get the toots from

def get_emoji_regexp():
    """
    Get a regular expression pattern to match and remove emojis.

    Returns:
        re.Pattern: The compiled regular expression pattern for matching emojis.

    """
    emojis = sorted(emoji.EMOJI_DATA, key=len, reverse=True)
    custom_emojis = mastodon.custom_emojis()
    emojis.extend([emoji['shortcode'].encode('utf-8').decode('utf-8') for emoji in custom_emojis])
    pattern = u'(' + u'|'.join(re.escape(u) for u in emojis) + u')'
    return re.compile(pattern)

input_file_path = os.path.join(os.path.dirname(__file__), "../corpus/toots.csv")
output_file_path = os.path.join(os.path.dirname(__file__), "../corpus/toots_processed.csv")

# Open input CSV file for reading and output CSV file for writing
with open(input_file_path, 'r', newline='', encoding='utf-8') as input_file, \
     open(output_file_path, 'w', newline='', encoding='utf-8') as output_file:
    
    # Create DictReader and DictWriter
    reader = csv.DictReader(input_file)
    fieldnames = reader.fieldnames
    writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    writer.writeheader()

    # Loop through all rows in the CSV file
    for row in reader:
        # Delete emojis from the 'content' field
        row['content'] = get_emoji_regexp().sub(r'', row['content'])

        # Remove HTML tags from the 'content' field
        html_content = row['content']
        soup = BeautifulSoup(html_content, 'html.parser')
        CLEAN_TEXT = soup.get_text()
        row['content'] = CLEAN_TEXT
        
        # Write row to output file
        writer.writerow(row)
