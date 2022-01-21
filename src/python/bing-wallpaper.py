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
    BING_API = "https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=10&nc=1612409408851&pid=hp&FORM=BEHPTB&uhd=1&uhdwidth=3840&uhdheight=2160"
    BING_URL = "https://cn.bing.com"
    content = HttpUtils.get(BING_API)
    json_dic = json.loads(str(content, encoding='utf-8'))

    # 获取图片URL
    for image in json_dic['images']:
        url = BING_URL + image['url']
        url = url[0: url.index("&")]
        # 获取图片时间
        end_date = json_dic['images'][0]['enddate']
        end_date = datetime.datetime.strptime(end_date, "%Y%m%d").strftime("%Y-%m-%d")
        # 获取图片版权
        copy_right = image['copyright']
        # 下载图片
        download_image(url, end_date, copy_right)
