# -*- coding:utf-8 -*-
import HttpUtils
import json
import datetime
import os


def download_image(image_url, end_date, copy_right):
    path = os.getcwd()
    save_path = path + "/images/" + copy_right[:copy_right.index('(')] + ".jpg"
    print('downloading: ' + copy_right)
    if os.path.exists(save_path):
        print(save_path + " has already existed!")
        return
    file = open(save_path, 'wb+')
    image_content = HttpUtils.get(image_url)
    if image_content is not None:
        file.write(image_content)
    else:
        print("download %s failed" % image_url)
    file.close()


if __name__ == '__main__':
    md_path = os.getcwd() + '/bing-wallpaper.md'
    file = open(md_path, "r")
    lines = file.readlines()
    file.close()
    for line in lines:
        if '](' in line:
            copy_right = line[line.index('| [') + len('| ['): line.index(' (©')]
            image_url = line[line.index('](') + len(']('): line.index('.jpg') + len('.jpg')]
            if '/' in copy_right:
                copy_right = copy_right.replace('/', '｜')
            save_path = os.getcwd() + "/images/" + copy_right + ".jpg"

            print('downloading: ' + copy_right)
            if os.path.exists(save_path):
                print(save_path + " has already existed!")
                continue
            file = open(save_path, 'wb+')
            image_content = HttpUtils.get(image_url)
            if image_content is not None:
                file.write(image_content)
            else:
                print("download %s failed" % image_url)
            file.close()

