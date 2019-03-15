import pymysql
import oss2
import time
import random
from os import walk

import requests

conn = pymysql.connect(host='127.0.0.1', user='root', passwd="961007Jiayali...", db='xxn')
cur = conn.cursor()

file_urls = []


def upload():
    global file_urls
    fo = open("liyifeng-oss.txt", "r")

    while 1:
        line = fo.readline().strip()
        if line:
            file_urls.append(line)

        if not line:
            break
        pass  # do something
    fo.close()
    requests.post('http://xxn.test/api/admin/upload-picture',
                  json={'picture_url': file_urls, 'category': [1, 17, 89]})


upload()

cur.close()
conn.close()
