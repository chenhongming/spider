#! usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.error
import time
import os
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
#Download the picture from the resulting picture link and save it
f=open('out.txt','w',encoding='utf-8')
def SaveImage(link,InputData,count):
    try:
        time.sleep(0.2)
        urllib.request.urlretrieve(link,'./'+InputData+'/'+str(count)+'.jpg')
    except urllib.error.HTTPError as urllib_err:
        print(urllib_err)
    except Exception as err:
        time.sleep(1)
        print(err)
        print("Generate unknown error, give up saving")
    else:
        print("picture+1,having" + str(count) + "pictures")
#Find the link to the picture
def FindLink(PageNum,InputData,word):
    for i in range(PageNum):
        print(i)
        try:
            url = 'http://cn.bing.com/images/async?q={0}&first={1}&count=35&relp=35&lostate=r&mmasync=1&dgState=x*175_y*848_h*199_c*1_i*106_r*0'
            agent = {'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.165063 Safari/537.36 AppEngine-Google."}
            page1 = urllib.request.Request(url.format(InputData, i*35+1), headers=agent)
            page = urllib.request.urlopen(page1)
            soup = BeautifulSoup(page.read(), 'html.parser')
            print(type(soup))
            print(soup,file=f)
            #print(soup.decode('utf-8'))
            if not os.path.exists("./" + word):
                os.mkdir('./' + word)

            for StepOne in soup.select('.mimg'):
                print(type(StepOne))
                link=StepOne.attrs['src']
                count = len(os.listdir('./' + word)) + 1
                SaveImage(link,word,count)
        except:
            print('URL OPENING ERROR !')
if __name__=='__main__':
    #Enter the numbers of pages to load, 35 images per page
    PageNum = 10
    #Enter keywords to search for
    word='keywords'
    InputData=urllib.parse.quote(word)
    FindLink(PageNum,InputData,word)
