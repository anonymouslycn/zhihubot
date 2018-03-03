# -*- coding: utf-8 -*-
import requests
from parsel import Selector
import json
import time
from copyheaders import headers_raw_to_dict
import execjs
from requests_toolbelt.multipart.encoder import MultipartEncoder
import urllib
import gzip
import io
import demjson
import os
import http.cookiejar
import re
from bs4 import BeautifulSoup
import random
import csv
import codecs


aaa=open("search2.json","r")
file = aaa.read()

a = json.loads(file)
a = a['htmls']


soup = BeautifulSoup(str(a), "lxml")
# aut = soup.find_all('a',class_='author')
# cont = soup.find_all('script',class_='content')
# print (len(aut),len(cont))
# for i in range(len(cont)):
#   try:
#       print (aut[i].get_text())
#   except:
#       print ("+++")
#   print (cont[i].get_text())

dr = re.compile(r'<[^>]+>',re.S)

cont = soup.find_all('div',class_='entry-body')
for i in range(len(cont)):
    soups = BeautifulSoup(str(cont[i]), "lxml")
    const = soups.find_all('script',class_='content')

    aut1 = soups.find_all('div',class_='author-line summary-wrapper')
    aut2 = soups.find_all('a',class_='author')
    dd1 = dr.sub("",str(aut1))
    dd2 = dr.sub("",str(aut2))
    if len(dd2) != 2:
        dd = dd2
    else:
        dd = dd1
    print (dd)


