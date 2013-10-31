#!/usr/bin/env python3
# Copyright rejuvyesh <rejuvyesh@gmail.com>, 2013
# License: GNU GPL 3 <http://www.gnu.org/copyleft/gpl.html>

import requests
import re
import pickle
from subprocess import call
from bs4 import BeautifulSoup

url = 'http://172.26.142.66:4040/Common/CourseListing.asp'

response = requests.get(url)

soup = BeautifulSoup(response.content)
print(soup.prettify)

regex = re.compile("^[\s]+([A-Z]+[A-Z]*[0-9]+[A-Z0-9]*)[\n]", re.MULTILINE)
cont = regex.findall(soup.prettify())
pickle.dump(cont, open('sublist.p', 'wb'))
print(cont)

response.close
scrap = 'y'
obj = pickle.load(open('sublist.p', 'rb'))
if scrap == 'y':
    for i in obj:
        url = "http://172.26.142.66:4040/Utils/CourseInfoPopup2.asp?Course=" + i
        oars = requests.get(url, timeout=1)
        soup = BeautifulSoup(oars.content)
        fout = open(i + ".html", "wt")
        print((type(soup.prettify)))
        fout.write(oars.text)
        oars.close
        #fout.write(soup.get_text())
        # Still not working, using zsh for now
        if call("html2text " + i + ".html" + ">" + i + ".txt", shell=True) == 0:
            print("yay")
            #call("rm -f " + i + ".html", shell=True)
        else:
            print(i)
