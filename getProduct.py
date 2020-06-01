from crawler import crawl
from parser import parse
import json

pageString = crawl("url")

products = parse(pageString)
print(products)
print(len(products))

file = open("./products.json", "w+")
file.write(json.dumps(products))