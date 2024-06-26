# -*- coding: utf-8 -*-
"""Untitled15.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qVCVU4gyUCywBENve4y294QicDDUHUPk
"""

import requests
from bs4 import BeautifulSoup


def get_links():
    LINKS = []
    url = 'https://www.bbc.com'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features='lxml')
    for html in soup.find_all('li', class_='media-list__item'):
        link = html.find('a').get('href')
        if "https://" in link:
            LINKS.append(link)
        else:
            link = url + link
            LINKS.append(link)
    return LINKS


def get_page(url):
    response = requests.get(url)



for link in get_links():
    if "/news/" in link:
        get_page(link)
