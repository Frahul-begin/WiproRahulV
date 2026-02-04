from selenium import webdriver
import time

driver = webdriver.Firefox()

driver.get("https://tutorialsninja.com/demo/")
print("page 1 Title:", driver.title)
time.sleep(1)

driver.get("https://www.google.com/")
print("title is",driver.title)
time.sleep(2)

driver.back()
print("After Back:",driver.title)
time.sleep(1)

driver.forward()
print("After Forward:",driver.title)
time.sleep(1)

driver.quit()