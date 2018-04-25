from selenium import webdriver
import time
import urllib
from bs4 import BeautifulSoup as bs
import re
import os

# ****************************************************
base_url_part1 = 'https://www.google.com/search?q='
base_url_part2 = '&source=lnms&tbm=isch'  # base_url_part1 and base_url_part2 are fixed and there's no need to change
search_query = 'keywords'  # Search keywords, you can enter the keywords you want to retrieve
location_driver = '/usr/local/bin/chromedriver'  # This is a necessary Google driver for Mac
#location_driver = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe' # This is a necessary Google driver for Windowns
          


class Crawler:
    def __init__(self):
        self.url = base_url_part1 + search_query + base_url_part2

    # Launch Chrome browser driver
    def start_brower(self):
        driver = webdriver.Chrome(location_driver)
        driver.maximize_window()
        driver.get(self.url)
        return driver

    def downloadImg(self, driver):
        t = time.localtime(time.time())
        foldername = str(t.__getattribute__("tm_year")) + "-" + str(t.__getattribute__("tm_mon")) + "-" + str(
            t.__getattribute__("tm_mday"))  # Define the folder name
        picpath = '/Users/chenhongming/images/%s' % (foldername)  # Download to local directory
        if not os.path.exists(picpath):
            os.makedirs(picpath)

        # Record downloaded picture address to avoid duplicate pictures
        img_url_dic = {}
        x = 000
        pos = 0
        for i in range(1, 6):  # Here you can set the crawl range for yourself
            pos = i * 500
            js = "document.documentElement.scrollTop=%d" % pos
            driver.execute_script(js)
            time.sleep(2)
            html_page = driver.page_source
            soup = bs(html_page, "html.parser")
            imglist = soup.findAll('img', {'class': 'rg_ic rg_i'})

            for imgurl in imglist:
                try:
                    print(x, end=' ')
                    if imgurl['src'] not in img_url_dic:
                        target = picpath + '\\%s.jpg' % x
                        print ('Downloading image to location: ' + target)
                        img_url_dic[imgurl['src']] = ''
                        urllib.request.urlretrieve(imgurl['src'], target)
                        time.sleep(1)
                        x += 1
                except KeyError:
                    print("ERROR!")
                    break

    def run(self):
        print('Downloading image')

        driver = self.start_brower()
        self.downloadImg(driver)
        driver.close()
        print("Download has finished.")


if __name__ == '__main__':
    craw = Crawler()
    craw.run()
