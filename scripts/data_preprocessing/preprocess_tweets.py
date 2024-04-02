# Author: Lucía María Álvarez Crespo (GitHub: @luciamariaalvarezcrespo)
# Last modified: 01/04/2024
# Description: Detect the language of the tweets and add a 'language' field to the CSV file
# Python version: 3.10.6
# License: Mozilla Public License Version 2.0

import csv
import os
from langdetect import detect

def process_tweets(input_file, output_file):
    """
    Process tweets from the input file, detect their language, and write them to the output file.

    Args:
        input_file (str): Path to the input CSV file containing tweets.
        output_file (str): Path to the output CSV file to write the processed tweets.

    """
    # Define the header for the output file
    header = ['id', 'language', 'content']

    # Open the input file and create a CSV reader
    with open(input_file, 'r', encoding='utf-8') as csv_input:
        reader = csv.reader(csv_input)

        # Open the output file and create a CSV writer
        with open(output_file, 'w', encoding='utf-8', newline='') as csv_output:
            writer = csv.writer(csv_output)

            # Write the header to the output file
            writer.writerow(header)

            # Process each row in the input file
            for row in reader:
                tweet_id = row[0]
                content = row[1]

                # Detect the language of the tweet
                language = 'gl' if detect(content) != 'ca' else 'ca'

                # Write the row with id, language, and content to the output file
                writer.writerow([tweet_id, language, content])

# Name of the input file
input_file = os.path.dirname(__file__) + "/../corpus/tweets-galician.csv"
output_file = os.path.dirname(__file__) + "/../corpus/tweets.csv"

# Process the tweets
process_tweets(input_file, output_file)
