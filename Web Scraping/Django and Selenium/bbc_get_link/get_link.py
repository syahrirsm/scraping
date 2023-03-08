from selenium import webdriver
import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bbc_link"
)
cursor = db.cursor()
# inisialisasi WebDriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

driver.get("https://www.bbc.com")

links = driver.find_elements_by_tag_name("a")

for link in links:
    href = link.get_attribute("href")
    print(href)
    print(link.text)
    
    sql = "INSERT INTO tb_link (link, title) VALUES (%s,%s)"
    val = (href,link.text)
    cursor.execute(sql, val)
    db.commit()

db.close()
driver.quit()


