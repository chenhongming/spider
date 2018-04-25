# -*- coding: utf-8 -*-
import requests
import os

def getManyPages(keyword,pages):
    params=[]
    for i in range(30,30*pages+30,30):
        params.append({
                      'tn': 'resultjson_com',
                      'ipn': 'rj',
                      'ct': 201326592,
                      'is': '',
                      'fp': 'result',
                      'queryWord': keyword,
                      'cl': 2,
                      'lm': -1,
                      'ie': 'utf-8',
                      'oe': 'utf-8',
                      'adpicid': '',
                      'st': -1,
                      'z': '',
                      'ic': 0,
                      'word': keyword,
                      's': '',
                      'se': '',
                      'tab': '',
                      'width': '',
                      'height': '',
                      'face': 0,
                      'istype': 2,
                      'qc': '',
                      'nc': 1,
                      'fr': '',
                      'pn': i,
                      'rn': 30,
                      'gsm': '1e',
                      '1488942260214': ''
                  })
    url = 'https://image.baidu.com/search/acjson'
    urls = []
    for i in params:
        urls.append(requests.get(url,params=i).json().get('data'))
    return urls

def getImg(dataList, localPath):
    if not os.path.exists(localPath):  # new folder
        os.mkdir(localPath)
    x = 0
    for list in dataList:
        for i in list:
            if i.get('thumbURL') != None:
                print('Downloading：%s' % i.get('thumbURL'))
                ir = requests.get(i.get('thumbURL'))
                open(localPath + '%d.jpg' % x, 'wb').write(ir.content)
                x += 1
            else:
                print('Image link does not exist')

if __name__ == '__main__':
    dataList = getManyPages('keywords',numbers)  # Parameter 1: keyword, parameter 2: number of pages to download
    getImg(dataList,'/Users/chenhongming/Desktop/') # Parameter 2: Specify the saved path
