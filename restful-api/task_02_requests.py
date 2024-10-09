#!/usr/bin/python3
"""
Script to fetch the posts from the API and print the titles of the posts    
using the requests module of python.
"""
import requests
import csv


def fetch_and_print_posts():
    """
    The function fetches the posts from the API and prints the titles of the posts.
    1. Sends a GET request to the URL 
    https://jsonplaceholder.typicode.com/posts to retrieve JSON data.
    2. Displays the status code of the HTTP response.
    3. If the status code is 200 (meaning the request was successful), 
    it converts the JSON response into a list of posts.
    4. For each post in the list, it displays the post title.
    """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f'Status Code: {response.status_code}')
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """
    The function fetches the posts from the API and saves the posts in a CSV file.
    1. Sends a GET request to the URL
    https://jsonplaceholder.typicode.com/posts to retrieve JSON data.
    2. Displays the status code of the HTTP response.
    3. If the status code is 200 (meaning the request was successful),
    it converts the JSON response into a list of posts.
    4. It writes the posts to a CSV file called posts.csv.
    5. The CSV file has columns corresponding to the dictionary keys
    """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f'Status Code: {response.status_code}')
    if response.status_code == 200:
        posts = response.json()
        keys = posts[0].keys()

        with open('posts.csv', 'w') as file:
            writer = csv.DictWriter(file, fieldnames=keys)
            writer.writeheader()
            for post in posts:
                writer.writerow(post)
