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

# Download the picture from the resulting picture link and save it
def SaveImage(link,InputData,count):
    try:
        urllib.request.urlretrieve(link,'./'+InputData+'/'+str(count)+'.jpg')
    except urllib.error.HTTPError as urllib_err:
        print(urllib_err)
    except Exception as err:
        print(err)
        print("Generate unknown error, give up saving")
    else:
        print("picture+1,having" + str(count) + "pictures")
        print('Downloading' + str(count + 1) + 'pictures')

#Find the link to the picture
def FindLink(InputData,word):
    url = 'https://www.google.com.hk/search?q=%s&newwindow=1&safe=strict&source=lnms&tbm=isch&sa=X&ved=0ahUKEwir1MTc6fnWAhWJjJQKHXfECE4Q_AUICigB&biw=1440&bih=769' % InputData
    driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')   # This is a necessary Google driver for Mac
    #driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe') # This is a necessary Google driver for Windowns
          
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
    #Enter keywords to search for
    word='$#%@#^&'
    InputData=urllib.parse.quote(word)
    FindLink(InputData,word)
