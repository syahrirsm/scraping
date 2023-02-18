from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd
import time

def get_text(x):
    o = x.split(">")
    if len(o) > 1:
        o = o[1].split("<")
        o = o[0]
    else:
        o = o[0]
    return o

# opsi = webdriver.ChromeOptions()
# opsi.add_argument('--headless')
# servis = Service('/usr/local/bin/chromedriver')
# driver = webdriver.Chrome(service = servis, options=opsi)

driver = webdriver.Chrome()
shoope_link = "https://www.yell.com/ucs/UcsSearchAction.do?scrambleSeed=2033442120&keywords=hotels&location=UK"
driver.set_window_size(1300, 800)
driver.get(shoope_link)
driver.save_screenshot("Web Scraping/Yell/yell.png")
time.sleep(5)
content = driver.page_source
driver.quit()
data = BeautifulSoup(content,'html.parser')

i = 1
list_hotels,list_location,list_rating,list_link=[],[],[],[]
for area in data.find_all('div',class_="row businessCapsule--mainRow"):
    print(str(i))
    name = str(area.find('h2', class_="businessCapsule--name text-h2"))
    name = get_text(name)

    street = str(area.find('span', itemprop="streetAddress"))
    street = get_text(street)
    address = str(area.find('span', itemprop="addressLocality"))
    address = get_text(address)
    postal = str(area.find('span', itemprop="postalCode"))
    postal = get_text(postal)
    location = street+address+', '+postal

    rating = str(area.find('span', class_="starRating--average"))
    rating = get_text(rating)

    list_hotels.append(name)
    list_location.append(location)
    list_rating.append(rating)


    print(name)
    print(location)
    print(rating)
    print("--------------------")
    i += 1

df = pd.DataFrame({'Hotels':list_hotels,'Location':list_location, 'Rating':list_rating})
writer = pd.ExcelWriter('Web Scraping/Yell/Hotels.xlsx')
df.to_excel(writer,'Sheet1',index=False)
writer.close()