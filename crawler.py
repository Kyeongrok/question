import requests

def crawl(url):
    url = "https://www.coupang.com/np/categories/186764"
    headers = {"User-Agent": "User-Agent':'Mozilla/5.0 (X11; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0"}
    data = requests.get(url, headers=headers)
    print(data.status_code, url)
    return data.content