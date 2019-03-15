# -*- coding: utf-8 -*-
import urllib.request


def down():
    fo = open("dilireba.txt", "r")

    while 1:
        line = fo.readline().strip()
        if line:
            name = line.split('/')[-1].strip()
            print(line, name)
            urllib.request.urlretrieve(line, './downloads/dilireba/' + name)

        if not line:
            break
        pass  # do something
    fo.close()


down()
