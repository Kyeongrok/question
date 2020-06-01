import pandas as pd

df = pd.read_json("./products.json")

writer = pd.ExcelWriter("productsCategory.xlsx")
df.to_excel(writer, "sheet1")
writer.save()

#openpyxl