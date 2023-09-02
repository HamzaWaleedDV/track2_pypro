# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from time import sleep
# from selenium.webdriver.common.keys import Keys

# option = webdriver.ChromeOptions()
# option.add_experimental_option("debuggerAddress", "localhost:9222")

# browser = webdriver.Chrome()
# browser.get('https://www.youtube.com/')


# search_box = browser.find_element(By.NAME, "search_query")
# search_box.send_keys("@LearnCodeEasily")
# sleep(2)

# search_box.submit()
# sleep(2)

# search = browser.find_element(By.CSS_SELECTOR, '#search-icon-legacy > yt-icon')
# search.click()
# sleep(3)

# clicker = browser.find_element(By.CSS_SELECTOR, '#thumbnail > yt-image > img')
# clicker.click()
# sleep(2)

# screen_shot = browser.get_screenshot_as_png()
# browser.save_screenshot('LCE.png')
# sleep(2)

# like = browser.find_element(By.CSS_SELECTOR, '#segmented-like-button > ytd-toggle-button-renderer > yt-button-shape > button > yt-touch-feedback-shape > div > div.yt-spec-touch-feedback-shape__fill')
# like.click()
# sleep(2)

# screenShot = browser.get_screenshot_as_png()
# browser.save_screenshot('LCE1.png')
# sleep(2)

# login = browser.find_element(By.CSS_SELECTOR, '#button > yt-button-shape > a > yt-touch-feedback-shape > div > div.yt-spec-touch-feedback-shape__fill')
# login.click()
# sleep(2)

# fill_email = browser.find_element(By.CSS_SELECTOR, '#identifierId')
# fill_email.send_keys('hamzanasr412@gmail.com')
# sleep(2)

# fill_submit = browser.find_element(By.CSS_SELECTOR, '#identifierNext > div > button')
# fill_submit.click()
# sleep(2)

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# إعداد متصفح Chrome وفتح موقع Google
browser = webdriver.Chrome()
browser.get('https://www.google.com/login')

# العثور على حقل البريد الإلكتروني وإدخال البريد الإلكتروني الخاص بك
email_field = browser.find_element(By.ID, 'identifierId')
email_field.send_keys('hamzanasr412@gmail.com')

# النقر على زر التالي للانتقال إلى صفحة إدخال كلمة المرور
next_button = browser.find_element(By.ID, 'identifierNext')
next_button.click()

# الانتظار لبضع ثوانٍ لتمكين صفحة إدخال كلمة المرور
sleep(2)

# العثور على حقل كلمة المرور وإدخال كلمة المرور الخاصة بك
password_field = browser.find_element(By.NAME, 'password')
password_field.send_keys('hamza@nasr456')

# النقر على زر تسجيل الدخول
login_button = browser.find_element(By.ID, 'passwordNext')
login_button.click()

# الانتظار لبعض الوقت للانتقال إلى صفحة الرئيسية بعد تسجيل الدخول
sleep(100)

# قم بالتلاعب بصفحة الرئيسية كما تحتاج

# إغلاق المتصفح بعد الانتهاء
browser.quit()
