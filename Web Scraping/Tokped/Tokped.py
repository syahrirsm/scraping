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
tokped_link = "https://www.tokopedia.com/search?st=product&q=macbook&srp_component_id=02.01.00.00&srp_page_id=&srp_page_title=&navsource="
driver.set_window_size(1300, 800)
driver.get(tokped_link)

rentang = 500
for i in range(1,7):
    akhir = rentang * i 
    perintah = "window.scrollTo(0,"+str(akhir)+")"
    driver.execute_script(perintah)
    print("loading ke-"+str(i))
    time.sleep(1)

driver.save_screenshot("Web Scraping/Tokped/macbook.png")
time.sleep(5)
content = driver.page_source

data = BeautifulSoup(content,'html.parser')

i = 0
for area in data.find_all('div',class_="pcv3__container css-gfx8z3"):
    print(str(i))
    nama = str(area.find('div', class_="prd_link-product-name css-3um8ox"))
    nama = get_text(nama)

    print(nama)
    print("---------------")
    i+=1



tokped_link = "https://www.tokopedia.com/search?st=product&q=lenovo&srp_component_id=01.07.00.00&srp_page_id=&srp_page_title=&navsource="
driver.get(tokped_link)

rentang = 500
for i in range(1,7):
    akhir = rentang * i 
    perintah = "window.scrollTo(0,"+str(akhir)+")"
    driver.execute_script(perintah)
    print("loading ke-"+str(i))
    time.sleep(1)
    
driver.save_screenshot("Web Scraping/Tokped/lenovo.png")
time.sleep(5)
content = driver.page_source

data = BeautifulSoup(content,'html.parser')

i = 0
for area in data.find_all('div',class_="pcv3__container css-gfx8z3"):
    print(str(i))
    nama = str(area.find('div', class_="prd_link-product-name css-3um8ox"))
    nama = get_text(nama)

    print(nama)
    print("---------------")
    i+=1

driver.quit()