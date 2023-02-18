from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd
import time

opsi = webdriver.ChromeOptions()
opsi.add_argument('--headless')
servis = Service('/usr/local/bin/chromedriver')
driver = webdriver.Chrome(service = servis, options=opsi)
shoope_link = "https://shopee.co.id/search?keyword=macbook"
driver.set_window_size(1300, 800)
driver.get(shoope_link)

rentang = 500
for i in range(1,7):
    akhir = rentang * i 
    perintah = "window.scrollTo(0,"+str(akhir)+")"
    driver.execute_script(perintah)
    print("loading ke-"+str(i))
    time.sleep(1)

# time.sleep(5)

driver.save_screenshot("Shopee/shoope.png")
content = driver.page_source
driver.quit()

data = BeautifulSoup(content,'html.parser')
# print(data.encode("utf-8"))
i=1

def get_text(x):
    o = x.split(">")
    if len(o) > 1:
        o = o[1].split("<")
        o = o[0]
    else:
        o = o[0]
    return o

list_nama,list_harga, list_terjual=[],[],[]

for area in data.find_all('div',class_="col-xs-2-4 shopee-search-item-result__item"):
    print(str(i))
    nama = str(area.find('div', class_="ie3A+n bM+7UW Cve6sh"))
    nama = get_text(nama)
    harga = str(area.find('span', class_="ZEgDH9"))
    harga = get_text(harga)
    terjual = str(area.find('div', class_="r6HknA uEPGHT"))
    terjual = get_text(terjual)

    list_nama.append(nama)
    # list_gambar.append(gambar)
    list_harga.append(harga)
    # list_link.append(link)
    list_terjual.append(terjual)

    print(nama)
    print(harga)
    print("---------------")
    i+=1

df = pd.DataFrame({'Nama':list_nama,'Harga':list_harga, 'Terjual':list_terjual })
writer = pd.ExcelWriter('Shopee/macbook.xlsx')
df.to_excel(writer,'Sheet1',index=False)
writer.close()