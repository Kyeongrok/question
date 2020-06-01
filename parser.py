#문자열에서 데이터 받아오기

#1
from bs4 import BeautifulSoup

#3
def getProductInfo(li):
    name = li.find("div", {"class":"name"})
    regularPrice = ""
    try:
        li.find("del", {"class":"base-price"})
    except:
        print("regulatPrice 없음")
    salePrice = ""
    try:
        li.find("em").find("strong", {"class":"price-value"})
    except:
        print("salePrice 없음")
    discount = ""
    try:
        li.find("span", {"class":"discount-percentage"})
    except:
        print("discount 없음")
    link = li.find("a", {"class":"baby-product-link"})
    img = li.find("img")
    src = img['src']

    return {"name":name.text, "regularPrice":regularPrice.find().text.replace(",", ""), "salePrice":salePrice.find().text.replace(",", ""), "discount":discount.find().text, "img":src, "link":link['href']}

#2
def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    ul = bsObj.find("ul", {"id":"productList"})
    lis = ul.findAll("li", {"class":"baby-product renew-badge"})

#4
    products = []
    for li in lis:
        product = getProductInfo(li)
        products.append(product)
    return products