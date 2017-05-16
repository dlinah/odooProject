import requests
import  lxml
from bs4 import BeautifulSoup




class souqScrapper:
    def __init__(self , url):
         self.source = requests.get(url)
         self.soup = BeautifulSoup(self.source.content , "lxml")
         # print soup.prettify()


    def title(self):
         pn = self.soup.find("div", {"class":"small-12 columns product-title"})
         pText = pn.find("h1").text
         return pText

    def price(self):
        price = self.soup.find("div", {"class":"text-default price-container"})
        price_header = price.find("h3", {"class":"price is sk-clr1"})
        pValue = price.find("h3").text
        return pValue


    def description(self):
        description = self.soup.find("div", {"class":"item-details-mini"})
        desc = description.find("p").text
        return desc


    def image_url(self):
        image = self.soup.find("div", {"class":"img-bucket"})
        imgUrl = image.find('img').get('src')
        return imgUrl


scrapper = souqScrapper('https://egypt.souq.com/eg-en/samsung-grand-prime-plus-dual-sim-8gb-1-5gb-ram-4g-lte-gold-11871414/i/')

print('title is ' + scrapper.title())
print('price is ' + scrapper.price())
print('description is ' + scrapper.description())
print('image is ' + scrapper.image_url())








# # condition = soup.find("dl", {"class":"stats clearfix"})
# # cond = condition.find("dd").next_sibling
# # soldBy = condition.find("dt").next_sibling
# # print cond
# # print soldBy

 
























 
