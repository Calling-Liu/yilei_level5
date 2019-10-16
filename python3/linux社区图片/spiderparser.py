from bs4 import BeautifulSoup
import requests
import re

class SpiderParser(object):
    def get_pic(self, pics):
        count = 0
        r = []
        for pic in pics:
            link = (pic['src'])[5:]
            pic_link = "https://www.linuxidc.com" + link
            #print(pic_link)
            header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
            r.append(requests.get(pic_link, headers=header))
            count = count + 1
        return r, count
    def parser(self, cont):
        soup = BeautifulSoup(cont,"html.parser")
        pic = soup.find('div', class_='mframe mR').find('div',class_='wrapper').find('div', class_='mm').find('div', id='content').find_all('img',src=re.compile("../../upload/\w+_\w+/\w+.jpg"))
        print(pic)
        data = self.get_pic(pic)

        return data
