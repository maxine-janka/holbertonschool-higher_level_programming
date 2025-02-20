#!/usr/bin/python3
"""Fetching, printing and saving data using the Public API JSONPlaceholder"""

import requests
import csv

url = 'https://jsonplaceholder.typicode.com/posts'


def fetch_and_print_posts():
    """Sends a request to JSONPlaceholder API to fetch the data and print
      the title of each post"""

    # Sends the request to API and stores it
    response = requests.get(url)

    # Print the status code of the response
    print("Status Code: {}".format(response.status_code))

    # If status OK, store as JSON object
    if response.status_code == 200:
        json_object = response.json()

    # Iterate parsed data and print value for the key "title"
    for post in json_object:
        print(post["title"])


def fetch_and_save_posts():
    """Sends a request to the JSONPlaceholder API to fetch the data
      and write extracted data to a CSV file"""

    response = requests.get(url)

    if response.status_code == 200:
        json_object = response.json()

        # empty list to store extracted data from each post
        filtered_data = []

        # Create a dictionary from each post and assign key values
        # by extracting from json object
        for post in json_object:
            extracted_fields = {
                'id': post.get('id'),
                'title': post.get('title'),
                'body': post.get('body')
            }
            # Append each post dict to the list
            filtered_data.append(extracted_fields)

        column_titles = ['id', 'title', 'body']

        # Create CSV file
        with open("posts.csv", mode='w', encoding='utf-8') as posts_file:
            # Create CSV writer and define column headers
            writer = csv.DictWriter(posts_file, fieldnames=column_titles)
            # writes the column names to the file
            writer.writeheader()
            # writes each dictionary ih the list as a row
            writer.writerows(filtered_data)
