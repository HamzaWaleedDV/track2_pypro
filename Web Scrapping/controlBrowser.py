from selenium import webdriver
import chromedriver_binary
import geckodriver_autoinstaller

#Google chrome
# browser = webdriver.Chrome()
# browser.get('https://www.google.com/')

browser = webdriver.Firefox()
browser.get('https://www.google.com/')