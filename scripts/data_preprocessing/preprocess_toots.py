# Author: Lucía María Álvarez Crespo (GitHub: @luciamariaalvarezcrespo)
# Last modified: 01/04/2024
# Description: Combine the data from the CSV files containing the toots and write it to a single CSV file
# Python version: 3.10.6
# License: Mozilla Public License Version 2.0

import os
import csv

def combine_csv_data(folder_path, output_file):
    """
    Combine data from multiple CSV files in a folder and write it to a single CSV file.

    Args:
        folder_path (str): Path to the folder containing the CSV files.
        output_file (str): Path to the output CSV file.

    """
    # List to store the combined data
    combined_data = []

    # Obtaining the list of CSV files in the folder
    csv_files = [file for file in os.listdir(folder_path) if file.startswith('toots_') and file.endswith('.csv')]

    # Loop through the files and append their data to the combined_data list
    for file in csv_files:
        file_path = os.path.join(folder_path, file)
        with open(file_path, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                # Obtain the values from each row
                id_value = row.get('id')
                language_value = row.get('language')
                content_value = row.get('content')
                # Append the values to the combined_data list
                combined_data.append({'id': id_value, 'language': language_value, 'content': content_value})

    # Write the combined data to the output CSV file
    with open(output_file, 'w', encoding='utf-8', newline='') as csv_output:
        fieldnames = ['id', 'language', 'content']
        writer = csv.DictWriter(csv_output, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(combined_data)

# Path to the folder containing the CSV files
folder_path = os.path.dirname(__file__) + "/../data/"
# Path to the output CSV file
output_file = os.path.dirname(__file__) + "/../data/toots_all.csv"

# Combine the CSV data
combine_csv_data(folder_path, output_file)
