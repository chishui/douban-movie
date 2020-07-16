# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from bs4 import NavigableString
import requests
import urllib
import json
import sys

SEARCH_URL='https://movie.douban.com/j/subject_suggest?q='
PAGE_URL='https://movie.douban.com/subject/%s/'

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,zh-TW;q=0.6',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
}

class Movie(object):
    def __init__(self):
        self.id = ''
        self.title = ''
        self.score = 0
        self.director = ''
        self.actor = ''
        self.year = ''
        self.sub_title = ''

    def __str__(self):
        text =  '===============   Douban Movie   ===============\n'+\
                'Title: ' + self.title + '\n' +\
                'Score: ' + str(self.score) + '\n' +\
                'Year: ' + self.year + '\n' +\
                'Director: ' + self.director + '\n' +\
                'Actors: ' + self.actor + '\n' +\
                '================================================'
        return text

def search(text):
    text = urllib.parse.quote(text)
    url = SEARCH_URL + text
    r = requests.get(url, headers=HEADERS)
    if r.status_code != 200:
        return

    data = r.text.encode('utf-8')
    items = json.loads(data)
    if len(items) == 0:
        return
    movies = []
    for item in items:
        if item['type'] != 'movie':
            continue
        movie = Movie()
        movie.id = item['id']
        movie.title = item['title']
        movie.year = item['year']
        movie.sub_title = item['sub_title']
        movies.append(movie)
    return movies

def parse(movie):
    url = PAGE_URL % movie.id
    r = requests.get(url, headers=HEADERS)
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
    print(movie)

def get_movie(text):
    movies = search(text)
    if movies and len(movies):
        parse(movies[0])
    else:
        print('cound not find movie: ' + text)

