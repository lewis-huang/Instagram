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
import time
try:
    from urlparse import urljoin
    from urllib import urlretrieve
except ImportError:
    from urllib.parse import urljoin
    from urllib.request import urlretrieve

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
for objScroller in range(0,5):
    driver.execute_script(js)
    time.sleep(1)

soup = BeautifulSoup(driver.page_source,"html.parser")
picURLs = soup.find_all("img",class_="_2di5p")
i = 0
socket.setdefaulttimeout(30)
for objURL in picURLs:
    print(objURL.attrs["src"])
    print(str(len(objURL.attrs["src"])))
    filename = "g:\\Catoon\\desktop\\"+str(i)+".jpg"
    i=i+1
'''
    #urllib.request.urlretrieve(objURL.attrs["src"],filename)#
urllib.request.urlretrieve(r"https://scontent-lax3-2.cdninstagram.com/vp/550fadc88f6bcdf8c7be8e9697eae12c/5B64BC61/t51.2885-15/s150x150/e35/c0.135.1080.1080/30602695_1589476304504802_2630712544481771520_n.jpg","001.jpg")


'''
