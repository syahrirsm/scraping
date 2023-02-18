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
shoope_link = "https://www.linkedin.com/search/results/people/?keywords=supervisor&origin=GLOBAL_SEARCH_HEADER&sid=S*R"
driver.set_window_size(1300, 800)
driver.get(shoope_link)
driver.save_screenshot("Web Scraping/LinkedIn/linked.png")
time.sleep(5)
content = driver.page_source
driver.quit()
data = BeautifulSoup(content,'html.parser')

i = 0
for area in data.find_all('div',class_="entity-result__content entity-result__divider pt3 pb3 t-12 t-black--light"):
    print(str(i))
    nama = str(area.find('a')['href'])
    nama = get_text(nama)

    print(nama)
    print("---------------")
    i+=1