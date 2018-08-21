from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = 'https://www.trivago.com/?aDateRange%5Barr%5D=2018-08-22&aDateRange%5Bdep%5D=2018-08-23&aPriceRange%5Bfrom%5D=0&aPriceRange%5Bto%5D=0&iPathId=350&aGeoCode%5Blat%5D=6.933832&aGeoCode%5Blng%5D=79.847237&iGeoDistanceItem=0&aCategoryRange=0%2C1%2C2%2C3%2C4%2C5&aOverallLiking=1%2C2%2C3%2C4%2C5&sOrderBy=relevance%20desc&bTopDealsOnly=false&iRoomType=7&cpt=35003&iIncludeAll=0&iViewType=0&bIsSeoPage=false&bIsSitemap=false&'

uClient = uReq(my_url)
page_html = uClient.read()
#uClient.close()
#page_soup = soup(page_html, "lxml")

page_soup = soup(page_html, 'lxml')

#containers = page_soup.find("div" , {})
#print(page_soup.title.string)
#print(page_soup.li.string)


for li in page_soup.find_all('li', class_='hotel item-order__list-item js_co_item'):
   print(page_soup.li.string)

#print(page_soup.get_text())

#for url in page_soup.find_all('a'):
 #   print(url.get('href'))

#nav = page_soup.nav
#print(nav )

#body = page_soup.body
#for p in body.find_all('p'):
 #   print(p.text)

for div in page_soup.find_all('div', class_= ''):
    print(div.text)
'''
print(page_soup.get('class'))



for d in page_soup('div', class_='sl-info-desc'):
    print(d.text)
'''
