# -*- coding:utf-8 -*-
import requests as requests


def get(url):
    r = requests.get(url)
    if r.status_code == requests.codes.ok:
        return r.content
    else:
        return None


def post(url, postdatas):
    r = requests.post(url, postdatas)
    if r.status_code == requests.codes.ok:
        return r.content
    else:
        return None
