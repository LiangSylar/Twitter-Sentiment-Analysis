from selenium import webdriver
from time import sleep
# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com/")
# sleep(3)
# driver.quit()

options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome()
driver.get('https://twitter.com/home') 

# 先在网页上登陆自己的twitter账号，然后把cookies取出来并
cookies=[] # Your cookies
for cookie in cookies:
    driver.add_cookie(cookie)
driver.quit()
