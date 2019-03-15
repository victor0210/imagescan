import os
import sys
import time, threading
import urllib.request

# 表情包进度 市民头像

pictures = list()
# title = sys.argv[1]
files = []
file_path = './dilireba/'
queue = []


# url_path = "bqburl/" + title + ".txt"
# download_path = './downloads/sougoubqb/' + title + '/'
# os.mkdir(download_path)


def getUrls():
    count = 0
    for (dirpath, dirnames, filenames) in os.walk(file_path):
        for f in filenames:
            urls = []
            fo = open(dirpath + f, "r")

            os.mkdir('./downloads/dilireba/' + f + '/')

            while 1:
                line = fo.readline().strip()
                if line:
                    urls.append(line)

                if not line:
                    break
                pass  # do something

            for url in urls:
                queue.append(dict({
                    "title": f,
                    "url": url
                }))

            count += 1
            fo.close()


getUrls()

downloads = []
count = 0


def down(item):
    global count
    title = item['title']
    _url = item['url']

    down_load_path = './downloads/dilireba/' + title + '/'
    name = _url.split('/')[-1].strip()
    try:
        urllib.request.urlretrieve(_url, down_load_path + name)
        count += 1
        print("down: " + title, " ====== count: " + str(count))
    except:
        print("down error:" + title)


def run_thread_down():
    while len(queue) > 0:
        down(queue.pop())


threads = []

for i in range(1, 8):
    t = threading.Thread(target=run_thread_down)
    t.start()
    threads.append(t)
    print(i)

for t in threads:
    t.join()
