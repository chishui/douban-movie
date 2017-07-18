# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from bs4 import NavigableString
import requests
import urllib
import json
import sys

SEARCH_URL='https://movie.douban.com/j/subject_suggest?q='
PAGE_URL='https://movie.douban.com/subject/%s/'

class Movie(object):
    def __init__(self):
        self.id = ''
        self.title = ''
        self.score = 0
        self.director = ''
        self.actor = ''
        self.year = ''

    def __str__(self):
        text =  '===============   Douban Movie   ===============\n'+\
                'Title: ' + self.title + '\n' +\
                'Score: ' + str(self.score) + '\n' +\
                'Year: ' + self.year + '\n' +\
                'Director: ' + self.director + '\n' +\
                'Actors: ' + self.actor + '\n' +\
                '================================================'
        return text.encode('utf-8')

def search(text):
    text = urllib.quote(text)
    url = SEARCH_URL + text
    r = requests.get(url)
    if r.status_code != 200:
        return

    data = r.text.encode('utf-8')
    items = json.loads(data)
    if len(items) == 0:
        return
    movie = Movie()
    movie.id = items[0]['id']
    movie.title = items[0]['title']
    movie.year = items[0]['year']
    return movie

def parse(movie):
    url = PAGE_URL % movie.id
    r = requests.get(url)
    soup = BeautifulSoup(r.text.encode('utf-8'), 'lxml')
    movie.score = soup.find('strong', 'rating_num').text
    info = soup.find('div', {'id': 'info'})
    for linebreak in info.find_all('br'):
        linebreak.extract()
    for span in info.contents:
        if isinstance(span, NavigableString): continue
        if span.contents[0]:
            if span.contents[0].string == u'导演':
                if isinstance(span.contents[1], NavigableString):
                    movie.director = span.contents[2].text
            elif span.contents[0].string == u'主演':
                if isinstance(span.contents[1], NavigableString):
                    movie.actor = span.contents[2].text
    print movie

def get_movie(text):
    movie = search(text)
    if movie:
        parse(movie)
    else:
        print 'cound not find movie: ' + text

