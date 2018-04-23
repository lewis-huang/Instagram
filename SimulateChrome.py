from __future__ import division
import urllib
import argparse
import codecs
from collections import defaultdict
import json
import os
import re
import sys
import socket
import socks
import time
try:
    from urlparse import urljoin
    from urllib import urlretrieve
except ImportError:
    from urllib.parse import urljoin
    from urllib.request import urlretrieve
from urllib.request import ProxyHandler, build_opener
from urllib.error import URLError


from bs4 import BeautifulSoup
import requests
import selenium
from selenium import webdriver

from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()
# driver.get(" https://www.instagram.com/accounts/login/")


# time.sleep(15)
# username = driver.find_element_by_name("username")
# password = driver.find_element_by_name("password")
# submitbtn = driver.find_element_by_tag_name("button")
# username.send_keys("huangyun_122@163.com")
# password.send_keys("lewis123456.")
# submitbtn.send_keys(Keys.RETURN)


driver.get("https://www.instagram.com/desktour/")
time.sleep(5)
js = "window.scrollTo(0,document.body.scrollHeight);"
last_height = driver.execute_script("return document.body.scrollHeigth")
while(True):

    driver.execute_script(js)
    time.sleep(5)
    new_height=driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

soup = BeautifulSoup(driver.page_source,"html.parser")
picURLs = soup.find_all("img",class_="_2di5p")
i = 0
socket.setdefaulttimeout(30)


proxies = {
    'https': 'https://127.0.0.1:1080',
    'http': 'http://127.0.0.1:1080'
}
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}

opener = urllib.request.build_opener(urllib.request.ProxyHandler(proxies))
urllib.request.install_opener(opener)



for objURL in picURLs:
    print(objURL.attrs["src"])
    filename = "g:\\Catoon\\desktop\\"+str(i)+".jpg"
    try:
        urllib.request.urlretrieve(objURL.attrs["src"],filename)
    except Exception as E:
        print (E)


    i=i+1

    #urllib.request.urlretrieve(objURL.attrs["src"],filename)#
# urllib.request.urlretrieve(r"https://scontent-lax3-2.cdninstagram.com/vp/550fadc88f6bcdf8c7be8e9697eae12c/5B64BC61/t51.2885-15/s150x150/e35/c0.135.1080.1080/30602695_1589476304504802_2630712544481771520_n.jpg","001.jpg")


#
# print('--------------使用urllib--------------')
# google_url = 'https://www.google.com'

#
# req = urllib.request.Request(google_url, headers=headers)
# response = urllib.request.urlopen(req)
#
# print(response.read().decode())
#
# print('--------------使用requests--------------')
# response = requests.get(google_url, proxies=proxies)
# print(response.text)

# urllib.request.urlretrieve(r"https://scontent-lax3-2.cdninstagram.com/vp/39872026f3148c7d28edf479712154e2/5B55EDC5/t51.2885-15/s640x640/sh0.08/e35/c0.135.1080.1080/30602695_1589476304504802_2630712544481771520_n.jpg",r"G:\Catoon\desktop\001.jpg")

