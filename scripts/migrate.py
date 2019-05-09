# coding=utf-8
import oss2
import time
import random
from log import printColor
import os

import requests

# oss config
endpoint = 'http://oss-cn-beijing.aliyuncs.com'  # Suppose that your bucket is in the Hangzhou region.
prefix = 'https://xxndev.oss-cn-beijing.aliyuncs.com/'
auth = oss2.Auth('LTAI6mJmneGieajf', 'r0PWO9N4hAB0mydHHllSB9PqMfqiYM')
bucket = oss2.Bucket(auth, endpoint, 'xxndev')

file_urls = []

# download images and insert to db
def upload(file_path, title):
    for (dirpath, dirnames, filenames) in os.walk(file_path):
        newFP = './ossUrl/' + title + '-oss.txt'

        if os.path.exists(newFP):
            os.remove(newFP)

        fl = open(newFP, 'a+')
        for f in filenames:
            name = str(int(round(time.time() * 10000))) + str(int(random.random() * 10e5)) + '.jpg'
            oss2.resumable_upload(bucket, name, file_path + f)
            file_urls.append(prefix + name)
            fl.write(prefix + name + '\n')
            printColor('1;34;40m', "上传oss：" + f + "成功，在线地址：" + prefix + name)

        fl.close()

    return file_urls

def insert2DB(urls):
    print("插入到db", urls)

    # 请求插入接口
    # r = requests.post('http://xxn.test/api/admin/upload-picture',
    #                  json={'picture_url': urls, 'category': [1, 17, 91]})