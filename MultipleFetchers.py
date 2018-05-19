import sys,pprint
import os
import io
import socket
import socks
import time
import requests
import _thread
import urllib

try:
    from urlparse import urljoin
    from urllib import urlretrieve
except ImportError:
    from urllib.parse import urljoin
    from urllib.request import urlretrieve

from urllib.request import ProxyHandler, build_opener
from urllib.error import URLError


def fetchFile(FileUrl,LocalFile,Locker):

    socket.setdefaulttimeout(30)
    proxies = {
        'https': 'https://127.0.0.1:1080',
        'http': 'http://127.0.0.1:1080'
    }
    opener = urllib.request.build_opener(urllib.request.ProxyHandler(proxies))
    urllib.request.install_opener(opener)

    try:
        urllib.request.urlretrieve(FileUrl, LocalFile)
    except Exception as E:
        print(E)
    finally:
        Locker.release()


