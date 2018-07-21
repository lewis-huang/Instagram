from __future__ import division
import _thread
import MultipleFetchers
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

def main(columnUrl,columnName):

    driver = webdriver.Chrome()
    picUrlList = []
    ## driver.get("https://www.instagram.com/exoxsoo/")
    driver.get(columnUrl)
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
        picURLs = soup.find_all("img",class_="FFVAD")
        print(picURLs)
        for objUrl in picURLs:
            print("url is %s"%(objUrl))
            picUrlList.append(objUrl)

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

    singleUrlList = []

    for objUrl in picUrlList:
        if (objUrl not in singleUrlList):
            singleUrlList.append(objUrl)
    LockerList = []
    for objURL in singleUrlList:

        print(objURL.attrs["src"])
        localPath = "g:\\Catoon\\desktop\\"+columnName
        filename = localPath +"\\"+str(i)+".jpg"
        fileurl = objURL.attrs["src"]
        if (not os.path.exists(localPath)):
            os.mkdir(localPath)
        print("the file Url is :%s" %(fileurl))
        if ( (i+1) % 10 != 0):

            lock = _thread.allocate_lock()
            lock.acquire()
            LockerList.append(lock)

            try:
                _thread.start_new_thread( MultipleFetchers.fetchFile,(fileurl,filename,lock))
            except Exception as E:
                print (E)
        else:
            for j in range(len(LockerList)):
                while LockerList[j].locked(): pass
        i=i+1




columnUrl = "https://www.instagram.com/joshkathey/"
columnName = "joshkathey"
main(columnUrl,columnName)


