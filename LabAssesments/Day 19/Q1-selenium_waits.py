from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

# Step 1: Launch browser
driver = webdriver.Chrome()
driver.maximize_window()

# 1. IMPLICIT WAIT
driver.implicitly_wait(10)

driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

print("Implicit wait applied (10 seconds)")

start_button = driver.find_element(By.XPATH, "//button[text()='Start']")
start_button.click()

# 2. EXPLICIT WAIT
wait = WebDriverWait(driver, 10)

hello_text = wait.until(
    EC.element_to_be_clickable((By.ID, "finish"))
)

print("Explicit wait: Element is clickable")

# 3. FLUENT WAIT (with polling interval)
fluent_wait = WebDriverWait(
    driver,
    timeout=15,
    poll_frequency=2,
    ignored_exceptions=[NoSuchElementException]
)

element = fluent_wait.until(
    EC.visibility_of_element_located((By.ID, "finish"))
)

# 4. PRINT MESSAGE WHEN ELEMENT IS READY
print("Fluent wait: Element is available for interaction")
print("Text displayed:", element.text)

time.sleep(3)
driver.quit()
