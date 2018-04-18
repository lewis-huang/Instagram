from __future__ import division

import argparse
import codecs
from collections import defaultdict
import json
import os
import re
import sys
import time
try:
    from urlparse import urljoin
    from urllib import urlretrieve
except ImportError:
    from urllib.parse import urljoin
    from urllib.request import urlretrieve

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
driver.get("http://www.baidu.com")
elem=driver.find_element_by_name("wd")
elem.clear()
elem.send_keys("网络爬虫")
elem.send_keys(Keys.RETURN)
time.sleep(3)
assert "网络爬虫." not in driver.page_source
driver.close()

