#-*- coding: utf-8 -*-
import urllib
from bs4 import BeautifulSoup



html = urllib.urlopen('http://bbs.ruliweb.com/community/board/300143/read/33025805')
soup = BeautifulSoup(html, "lxml")

tag_a = soup.find_all('a')

f = open("result.txt", 'w')
for i in tag_a:
    f.write(str(i))
f.close()
