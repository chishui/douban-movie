Douban-Movie
====================================
Display movie information retrieved from Douban (豆瓣) in your terminal. 

![alt text](screenshots/douban-movie.png "douban movie" )
![alt text](screenshots/douban-movie-list.png "douban movie list" )


[![PyPI](https://img.shields.io/pypi/v/nine.svg?maxAge=2592000)](https://pypi.python.org/pypi/douban-movie)
[![PyPI](https://img.shields.io/badge/python-2.7-blue.svg?maxAge=2592000)](https://pypi.python.org/pypi/douban-movie)

------------------
# Requirements
- Python 2.7
- [Urwid](https://github.com/urwid/urwid)
- Requests
- BeautifulSoup
- lxml

# Installation
```
$ pip install douban-movie
```
Clone the repository  
```
 $ git clone https://github.com/chishui/douban-movie.git  
 $ cd douban-movie
 $ sudo python setup.py install  
```
# Usage
Display movie infomation
```
$ douban zootopia
```
Output
```
===============   Douban Movie   ===============
Title: 疯狂动物城
Score: 9.2
Year: 2016
Director: 拜伦·霍华德 / 瑞奇·摩尔 / 杰拉德·布什
Actors: 金妮弗·古德温 / 杰森·贝特曼 / 伊德里斯·艾尔巴 / 珍妮·斯蕾特 / 内特·托伦斯 / 邦尼·亨特 / 唐·雷克 / 汤米·钟 / J·K·西蒙斯 / 奥克塔维亚·斯宾瑟 / 艾伦·图代克 / 夏奇拉 / 雷蒙德·S·佩尔西 / 德拉·萨巴 / 莫里斯·拉马奇 / 菲尔·约翰斯顿 / 约翰·迪·玛吉欧 / 凯蒂·洛斯 / 吉塔·雷迪 / 杰西·科尔蒂 / 汤米·利斯特 / 乔希·达拉斯 / 瑞奇·摩尔 / 凯特·索西 / 彼得·曼斯布里奇 / 拜伦·霍华德 / 杰拉德·布什 / 马克·史密斯 / 乔西·特立尼达 / 约翰·拉维尔 / 克里斯汀·贝尔 / 吉尔·科德斯 / 梅利莎·古德温
================================================
```

List all movies which match the name
```
$ douban 星球 -l
```
