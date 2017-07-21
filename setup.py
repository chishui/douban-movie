# -*- coding: utf-8 -*-:w
import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

requirements = ['requests', 'bs4', 'lxml', 'urwid']

setup(
    name = "douban-movie",
    version = "0.0.3",
    author = "Liyun Xiu",
    author_email = "chishui2@gmail.com",
    description = "Get movie info from Douban (豆瓣) and display in your terminal",
    license = "MIT",
    keywords = "douban terminal movie",
    url = "https://github.com/chishui/douban-movie",
    packages=['src'],
    long_description=read('README.md'),
    include_package_data=True,
    install_requires=requirements,
    entry_points={'console_scripts': ['douban=src.__main__:main']},
)
