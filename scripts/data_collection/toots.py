# Author: Lucía María Álvarez Crespo (GitHub: @luciamariaalvarezcrespo)
# Last modified: 26/06/2023
# Description: Get all public toots from an instance and save them to a CSV file
# Python version: 3.10.6

import csv
import datetime
import os
import pytz
from mastodon import Mastodon

# Instantiate Mastodon object
mastodon = Mastodon(access_token='YOUR_ACCESS_TOKEN_HERE', api_base_url='https://mastodon.gal')

# Get local timezone
local_timezone = pytz.timezone('Europe/Madrid')

def get_local_date(toot_date):
    """
    Get the local date and time of a toot.

    Args:
        toot_date (str): The date and time of the toot in UTC format ("%Y-%m-%dT%H:%M:%S.%fZ").

    Returns:
        str: The local date and time of the toot in the format "%Y-%m-%d %H:%M:%S".

    """
    utc_date = datetime.datetime.strptime(toot_date, '%Y-%m-%dT%H:%M:%S.%fZ')
    local_date = utc_date.replace(tzinfo=pytz.utc).astimezone(local_timezone)
    return local_date.strftime('%Y-%m-%d %H:%M:%S')

def timeline_and_save():
    """
    Get all public toots from the instance and save them to a CSV file.

    """
    output_file = os.path.dirname(__file__) + "/../corpus/toots_february.csv" # Change this to the name of the file you want to save the toots to
    batch_size = 1000

    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = None
        writer = None

        toots = mastodon.timeline_local(limit=batch_size)

        while len(toots) > 0:
            print(f'Processing batch of {batch_size} toots...')
            all_toots = mastodon.fetch_remaining(toots)

            if not writer:
                fieldnames = all_toots[0].keys()
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()

            for toot in all_toots:
                local_date = get_local_date(toot['created_at'].strftime('%Y-%m-%dT%H:%M:%S.%fZ'))
                if local_date.startswith('2023-02'): # Change this to the month you want to get the toots from
                    writer.writerow(toot)

            toots = mastodon.timeline_local(limit=batch_size, max_id=all_toots[-1]['id']-1)

    print('All toots saved to toots_february.csv')

if __name__ == '__main__':
    timeline_and_save()