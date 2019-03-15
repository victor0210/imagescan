import os
import sys
import time, threading
import urllib.request


# 表情包进度 市民头像

pictures = []
# title = sys.argv[1]

# if title:
# url_path = "bqburl/" + title + ".txt"
url_path = "mx/zhoudongyu.txt"
download_path = './downloads/zhoudongyu/'
os.mkdir(download_path)


def getUrls():
    fo = open(url_path, "r")

    while 1:
        line = fo.readline().strip()
        if line:
            pictures.append(line)

        if not line:
            break
        pass  # do something

    fo.close()


getUrls()


def down(url):
    name = url.split('/')[-1].strip()
    urllib.request.urlretrieve(url, download_path + name)
    print(url)


def run_thread():
    while len(pictures) > 0:
        down(pictures.pop())


threads = []

for i in range(1, 8):
    t = threading.Thread(target=run_thread)
    t.start()
    threads.append(t)
    print(i)

for t in threads:
    t.join()
