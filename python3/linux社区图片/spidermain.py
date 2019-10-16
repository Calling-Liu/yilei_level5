import spiderparser, spiderdownloader, spideroutputer
import threading
import time
import os
class SpiderMain(object):
    def __init__(self):
        self.parser = spiderparser.SpiderParser()
        self.downloader = spiderdownloader.SpiderDownloader()
        self.outputer = spideroutputer.SpiderOutputer()

    def craw(self, url_page):
        try:
            cont = self.downloader.download(url_page)
            data, times = self.parser.parser(cont)
        except:
            print("failed!")
            return

        self.outputer.outputer(data, times)

if __name__ == "__main__":
    url = "https://www.linuxidc.com/Linux/2019-09/160812.htm"
    spider = SpiderMain()
    spider.craw(url)
