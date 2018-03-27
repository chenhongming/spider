#! usr/bin/env python
# -*- coding: utf-8 -*-
import shutil
import urllib.error
import time
import os
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
from selenium import webdriver
import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import sys
import selenium.webdriver.support.ui as ui
import socket
import selenium.webdriver.phantomjs

f=open('url.txt','w',encoding='utf-8')
#从得到的图片链接下载图片，并保存
def SaveImage(link,InputData,count):
    try:
        urllib.request.urlretrieve(link,'./'+InputData+'/'+str(count)+'.jpg')
    except urllib.error.HTTPError as urllib_err:
        print(urllib_err)
    except Exception as err:
        print(err)
        print("产生未知错误，放弃保存")
    else:
        print("图+1,已有" + str(count) + "张图")
        print('正在下载第' + str(count + 1) + '张图片)
#找到图片的链接
def FindLink(InputData,word):
    url = 'https://www.google.com.hk/search?q=%s&newwindow=1&safe=strict&source=lnms&tbm=isch&sa=X&ved=0ahUKEwir1MTc6fnWAhWJjJQKHXfECE4Q_AUICigB&biw=1440&bih=769' % InputData
    driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
    #driver=webdriver.PhantomJS()

    driver.get(url)
    for i in range(20):
        print(i)
        try:
            temp = driver.find_element_by_xpath('//*[@id="smb"]')
            temp.click()
        except:
            print('Not find more!')
        time.sleep(5)
        driver.implicitly_wait(5)
        js = "var q=document.documentElement.scrollTop=%d" % 100000
        driver.execute_script(js)
    soup = BeautifulSoup(driver.page_source, 'lxml')

    if not os.path.exists("./" + word):
            os.mkdir('./' + word)

    for http in soup.select('.rg_meta'):
            link = eval(http.contents[0])['ou']
            #print(link,file=f)
            count = len(os.listdir('./' + word)) + 1
            SaveImage(link,word,count)

if __name__=='__main__':
    #输入需要加载的页数，每页35幅图像
    #PageNum = 10
    #输入需要搜索的关键字
    word='45型驱逐舰'
    InputData=urllib.parse.quote(word)
    FindLink(InputData,word)
