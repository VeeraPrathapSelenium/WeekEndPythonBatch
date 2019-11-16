from bs4 import BeautifulSoup as soup

from urllib.request import urlopen as Orequest

url="https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

client=Orequest(url)

pagesource=client.read()

client.close()

page_soup=soup(pagesource,'html.parser')

mobiles=page_soup.findAll("div",{"class":"_3O0U0u"})




print(len(mobiles))

print(soup.prettify(mobiles[0]))

print(mobiles[0].div.img['alt'])


productname=page_soup.findAll("div",{"class":"_3wU53n"})

print(productname[2].text)
