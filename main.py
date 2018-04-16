import requests
import json

import sys

origin_url = 'https://www.instagram.com'
login_url = origin_url + '/accounts/login/ajax/'
user_agent = 'Chrome/59.0.3071.115'

print(sys.platform)

username = "huangyun_122"
password = "lewis123456."
target_id = "alabasterfox"


# login ig and get cookies
session = requests.Session()
session.headers = {'user-agent': user_agent}
session.headers.update({'Referer': origin_url})

req = session.get(origin_url)
try:
    req.raise_for_status()
except Exception as exc:
    print('problem occur: %s' % (exc))
    exit()

session.headers.update({'X-CSRFToken': req.cookies['csrftoken']})
login_data = {'username': username, 'password': password}
login = session.post(login_url, data=login_data, allow_redirects=True)
try:
    login.raise_for_status()
except Exception as exc:
    print('problem occur: %s' % (exc))
    exit()

session.headers.update({'X-CSRFToken': login.cookies['csrftoken']})
cookies = login.cookies
login_text = json.loads(login.text)

