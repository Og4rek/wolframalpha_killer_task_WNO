import shutil
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from matplotlib import pyplot as plt
import cv2
import os


text_to_send = input("Podaj tekst do wyslania: ")

driver = webdriver.Chrome('/Users/piti/PycharmProjects/wolframalpha_killer_task_WNO/chromedriver')
driver.implicitly_wait(0.5)

form_url = "https://www.wolframalpha.com/"
driver.get(form_url)

driver.find_element(By.CLASS_NAME, "_O3dq").send_keys(text_to_send)
element = driver.find_element(By.CLASS_NAME, "_1w_c._2hsI._3HqA._29RU")
ActionChains(driver).click(element).perform()

time.sleep(3)

element = driver.find_element(By.CLASS_NAME, "_1w_c._2pr6._2O6V")
ActionChains(driver).click(element).perform()

folder_name = 'img'
os.mkdir(folder_name)

time.sleep(3)

x = driver.find_elements(By.CLASS_NAME, "_gtUC._3WIS")
for e in x:
    to_print = e.accessible_name.replace("Step-by-step solution", "")
    to_print = e.accessible_name.replace(" Autonomous equation »", "")
    if "Plots of sample" in to_print or "Sample solution family" in to_print:
        pass
    else:
        print(to_print)

images = driver.find_elements(By.TAG_NAME, 'img')
counter = 0
for img in images:
    src = img.get_attribute("src")
    if "MSP" in src:
        with open(folder_name+'/'+str(counter)+'.png', 'wb') as file:
            file.write(img.screenshot_as_png)
        counter += 1

driver.close()
driver.quit()

# create figure
fig = plt.figure(figsize=(12, 4))

# reading images
images = []
for filename in os.listdir(folder_name):
    img = cv2.imread(os.path.join(folder_name, filename))
    if img is not None:
        images.append(img)

counter = 1
for img in images:
    fig.add_subplot(1, len(images), counter)

    plt.imshow(img)
    plt.axis('off')

    counter += 1

plt.show()

shutil.rmtree(folder_name)