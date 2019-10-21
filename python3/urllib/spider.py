from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener, ProxyHandler, HTTPCookieProcessor
import http.cookiejar

url = "https://www.baidu.com"
user = "15191413512"
password = "71765897"

#验证
p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, user, password)
auth = HTTPBasicAuthHandler(p)
opener = build_opener(auth)

response1 = opener.open(url)

print(response1.read().decode('utf-8'))

#代理端口记得自己设置
proxy_handler = ProxyHandler({'http':'http://127.0.0.1:5000',
                              'https':'https://127.0.0.1:5000',})
opener = build_opener(proxy_handler)

response2 = opener.open(url)

print(response2.read().decode('utf-8'))

#cookie
cookie = http.cookiejar.CookieJar()
handler = HTTPCookieProcessor(cookie)
opener = build_opener(handler)

response3 = opener.open(url)

print(response3.read().decode('utf-8'))

