import requests

class SpiderDownloader(object):
    def download(self, url):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
        r = requests.get(url, headers=headers)
        r.encoding = 'utf-8'
        return r.text
