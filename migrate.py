import pymysql
import oss2
import time
import random
from os import walk

import requests

conn = pymysql.connect(host='127.0.0.1', user='root', passwd="961007Jiayali...", db='xxn')
cur = conn.cursor()

endpoint = 'http://oss-cn-beijing.aliyuncs.com'  # Suppose that your bucket is in the Hangzhou region.

auth = oss2.Auth('LTAI6mJmneGieajf', 'r0PWO9N4hAB0mydHHllSB9PqMfqiYM')
bucket = oss2.Bucket(auth, endpoint, 'xxndev')

file_path = './downloads/piaocanlie/'
prefix = 'https://xxndev.oss-cn-beijing.aliyuncs.com/'
file_urls = []


def upload():
    for (dirpath, dirnames, filenames) in walk(file_path):
        fl = open('./piaocanlie-oss.txt', 'a+')
        for f in filenames:
            print(f)
            name = str(int(round(time.time() * 10000))) + str(int(random.random() * 10e5)) + '.jpg'
            oss2.resumable_upload(bucket, name, file_path + f)
            file_urls.append(prefix + name)
            fl.write(prefix + name + '\n')

        r = requests.post('http://xxn.test/api/admin/upload-picture',
                          json={'picture_url': file_urls, 'category': [1, 17, 91]})

        fl.close()


upload()

cur.close()
conn.close()
