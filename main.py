# y''-y=0, y(0)=1, y(1)=0
import shutil
import time

import numpy as np
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from matplotlib import pyplot as plt
import cv2
import os
import math


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
try:
    os.mkdir(folder_name)
except:
    pass

time.sleep(3)

solution = None
x = driver.find_elements(By.CLASS_NAME, "_gtUC._3WIS")
for e in x:
    to_print = e.accessible_name.replace("Step-by-step solution", "")
    to_print = e.accessible_name.replace(" Autonomous equation »", "")
    if "Plots of sample" in to_print or "Sample solution family" in to_print:
        pass
    else:
        print(to_print)
        if "Step-by-step solution" in to_print:
            solution = to_print.split("Step-by-step solution", 1)[1]

# print("Rozwiazanie:", solution)
if "c_1" in solution:
    images = driver.find_elements(By.TAG_NAME, 'img')
    counter = 0
    for img in images:
        src = img.get_attribute("src")
        if "MSP" in src:
            with open(folder_name+'/'+str(counter)+'.png', 'wb') as file:
                file.write(img.screenshot_as_png)
            counter += 1

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
else:
    print(solution)
    solution = solution.split("= ", 1)[1]
    print(solution)

    math_solution = [char.replace('^', '**') for char in solution]
    math_solution = [char.replace('e', '2.7182') for char in math_solution]
    i = 0
    for char in solution:
        if char == ' ' and solution[i-1] != '+' and solution[i-1] != '-' and solution[i+1] != '+' and solution[i+1] != '-':
            math_solution[i] = '*'
        i += 1
    str1 = ""
    math_solution = str1.join(math_solution)
    print(math_solution)

    x_list = np.arange(0.1, 2.0, 0.1)
    y_list = []
    math_solution = [char.replace('x', '0.0') for char in math_solution]
    last_x = '0.0'
    str1 = ""
    math_solution = str1.join(math_solution)
    y_list.append(eval(math_solution))
    for x in x_list:
        math_solution = math_solution.replace(last_x, str(x))
        last_x = str(x)
        y_list.append(eval(math_solution))

    print(y_list)
    x_list = np.arange(0.0, 2.0, 0.1)
    plt.plot(x_list, y_list)
    plt.show()

driver.close()
driver.quit()
shutil.rmtree(folder_name)
