import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

text_to_send = input("Podaj tekst do wyslania: ")

driver = webdriver.Chrome('/Users/piti/PycharmProjects/wolframalpha_killer_task_WNO/chromedriver')

form_url = "https://www.wolframalpha.com/"
driver.get(form_url)

driver.find_element(By.CLASS_NAME, "_O3dq").send_keys(text_to_send)
element = driver.find_element(By.CLASS_NAME, "_1w_c._2hsI._3HqA._29RU")
ActionChains(driver).click(element).perform()

time.sleep(10)
driver.close()
driver.quit()