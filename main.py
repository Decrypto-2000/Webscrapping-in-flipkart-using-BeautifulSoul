import pandas as pd
import requests
from bs4 import BeautifulSoup
Product_name=[]
Prices =[]
Description=[]
Reviews=[]

#for i in range(2,10):
    # url =cnp
    # r=requests.get(url)
    # soup =BeautifulSoup(r.text ,"lxml")
for i in range(2,12):    
    url = "https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)
    r = requests.get(url)

    soup = BeautifulSoup(r.text ,"lxml")
box = soup.find("div", class_ ="DOjaWF gdgoEp")

names =box.find_all("div",class_ = "KzDlHZ")

for i in names:
    name=i.text
    Product_name.append(name)
# print(Product_name)


prices =box.find_all("div", class_ = "Nx9bqj _4b5DiR")

for i in prices:
    price=i.text
    Prices.append(price)
# print(Prices)


reviews=box.find_all("div", class_="XQDdHH")

for i in reviews:
    review=i.text
    Reviews.append(review)
# print(len(Reviews))

df = pd.DataFrame({"Product":Product_name,"Price":Prices,"Review":Reviews })
print(df)

#df.to_csv("flipkart_mobiles_under_50k.csv")






# nxtpage = soup.find("a",class_ ="_9QVEpD").get("href")
# cnp ="https://www.flipkart.com"+nxtpage
# print(cnp)
