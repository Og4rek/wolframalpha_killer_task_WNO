import time
import urllib.request
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

text_to_send = input("Podaj tekst do wyslania: ")

driver = webdriver.Chrome('/Users/piti/PycharmProjects/wolframalpha_killer_task_WNO/chromedriver')
driver.implicitly_wait(0.5)

form_url = "https://www.wolframalpha.com/"
driver.get(form_url)

driver.find_element(By.CLASS_NAME, "_O3dq").send_keys(text_to_send)
element = driver.find_element(By.CLASS_NAME, "_1w_c._2hsI._3HqA._29RU")
ActionChains(driver).click(element).perform()

time.sleep(5)

folder_name = 'img'

images = driver.find_elements(By.TAG_NAME, 'img')
counter = 0
for img in images:
    with open(str(counter)+'.png', 'wb') as file:
        file.write(img.screenshot_as_png)
    counter += 1

time.sleep(2)
driver.close()
driver.quit()
