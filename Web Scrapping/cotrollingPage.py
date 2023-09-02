from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_binary
import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('https://en.wikipedia.org/wiki/Main_Page')

try:
    # elem = browser.find_element(By.CSS_SELECTOR, '#ca-viewsource > a > span')
    # elem.click()
    # time.sleep(5)

    elem = browser.find_element(By.CSS_SELECTOR, '#searchInput')
    elem.send_keys('Python')
    time.sleep(3)

    button = browser.find_element(By.CSS_SELECTOR, '#searchform > div > button')
    button.click()
    time.sleep(5)

    time.sleep(3)
    htmlEle = browser.find_element(By.TAG_NAME, 'html')
    htmlEle.send_keys(Keys.END)
    time.sleep(3)
    htmlEle.send_keys(Keys.HOME)
    time.sleep(3)
except:
    print('Was not able to find an element with that name.')