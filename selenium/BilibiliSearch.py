from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib

driver = webdriver.Chrome()
url = 'https://search.bilibili.com/'
keyword = input("keywords:")
driver.get(url + 'video?keyword=' + urllib.parse.quote(keyword))
print (driver.page_source)
input("enter any key")
driver.close()



