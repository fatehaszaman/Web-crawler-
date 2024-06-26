# -*- coding: utf-8 -*-
"""Untitled13.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bZNlYLAt-ny1XFh2NxjNCkvx_kjX81K9
"""

import requests
from bs4 import BeautifulSoup
import random
import re

def get_random_pages(limit):
    unique_links = set()
    while len(unique_links) < limit:
        response = requests.get("https://en.wikipedia.org/wiki/Special:Random")
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            link = soup.find("link", rel="canonical")
            if link:
                unique_links.add(link['href'])
    return unique_links

unique_links = get_random_pages(5000)
for link in unique_links:
    print(link)
