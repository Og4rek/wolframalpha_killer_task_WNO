from selenium import webdriver

driver = webdriver.Chrome('/Users/piti/PycharmProjects/wolframalpha_killer_task_WNO/chromedriver')

form_url = "https://www.wolframalpha.com/"
driver.get(form_url)

driver.close()
driver.quit()