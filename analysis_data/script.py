#!/usr/bin/python3
import facebook
import requests
from bs4 import BeautifulSoup
import numpy as np
import re
from itertools import chain

URL = 'https://www.facebook.com/'




def found_str(soup):
    """this function it will find the category of the page"""
    for child in soup.findAll('div', re.compile("_4bl9")):
        result = child.find_all('a', {'href': re.compile('(pages/category/*|/search/*)')})
        if result:
            return result


def mining_data(url):
    """This function is for mining data into the webpage"""
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    try:
        soup = [word.text for word in found_str(soup)]
    except:
        soup = []
    finally:
        return soup


def get_info(permissions):
    """This function is for get the token and return the likes into the page"""
    graph = facebook.GraphAPI(permissions)
    profile = graph.get_object('me', fields='likes.limit(1000)')
    fan_page = [profile['likes']['data'][num]['id'] for num in range(len(profile['likes']['data']))]
    MUESTRA = np.random.choice(fan_page, int(len(fan_page) / 98.2 * 25))
    fan_page_likes = [mining_data(URL + num) for num in MUESTRA]
    likes = list(chain.from_iterable(fan_page_likes))
    return likes

