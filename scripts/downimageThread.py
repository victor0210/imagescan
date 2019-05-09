# coding=utf-8
import os
import sys
import time, threading
import urllib.request
import cv2
from log import printColor, inputColor
from migrate import upload, insert2DB

threads = []
pictures = []
title = sys.argv[1]
url_path = None
done_url_path = None
download_path = None

if title:
    url_path = "./imageUrl/" + title + ".txt"
    done_url_path = "./imageUrlDone/" + title + ".txt"
    download_path = './downloads/' + title + '/'

if not os.path.exists(download_path):
    os.mkdir(download_path)

def getUrls():
    fo = open(url_path, "r")

    while 1:
        line = fo.readline().strip()
        if line:
            print("将图片原地址写入数组", line)
            pictures.append(line)

        if not line:
            break
        pass  # do something

    fo.close()

def down(url):
    filepath = download_path + url.split('/')[-1].strip()
    urllib.request.urlretrieve(url, filepath)
    s = "下载图片: " + url
    printColor('1;32;40m', s)

def run_thread():
    while len(pictures) > 0:
        down(pictures.pop())

def filterImages(path):
    printColor('1;36;40m', "开始过滤模糊图片 >>>")

    for (dirpath, dirnames, filenames) in os.walk(path):
        for f in filenames:
            fp = path + f
            definition = filterImageDefinition(fp)

            if definition > 100:
                s = "图片名：" + fp + " 清晰度：" + str(filterImageDefinition(fp))
                printColor('1;36;40m', s)
            else:
                s = "图片名：" + fp + " 清晰度：" + str(filterImageDefinition(fp)) + " [Warning]: 清晰度偏低!! 是否删除？(y/n): "
                printColor('1;33;40m', s)
                var = input()

                if var == "" or var == "y" or var == "ye" or var == "yes":
                    os.remove(fp)
                    printColor('1;31;40m', "删除图片：" + fp)
    printColor('1;36;40m', "结束过滤模糊图片 <<<")


def filterImageDefinition(imgPath):
    image = cv2.imread(imgPath)
    img2gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return cv2.Laplacian(img2gray, cv2.CV_64F).var()

# 主逻辑代码流程
getUrls()

for i in range(1, 8):
    t = threading.Thread(target=run_thread)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

# 过滤清晰度低的图片
filterImages(download_path)

print("移动url源文本到已完成目录", url_path)
os.rename(url_path, done_url_path)
print("移动url源文本到已完成目录", done_url_path)

insert2DB(
    upload(download_path, title)
)