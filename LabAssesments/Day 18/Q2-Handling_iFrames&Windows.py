from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.maximize_window()

# Step 1: Open site
driver.get("https://the-internet.herokuapp.com/iframe")
time.sleep(2)

# Step 2: Switch to iframe
driver.switch_to.frame("mce_0_ifr")
print("Switched to iframe")

# Step 3: Locate editor body
text_area = driver.find_element(By.ID, "tinymce")

# Step 4: Check if editable
if text_area.get_attribute("contenteditable") == "true":
    text_area.clear()
    text_area.send_keys("Text entered inside iframe")
    print("Text entered successfully")
else:
    print("Iframe editor is read-only, skipping typing")

# Step 5: Switch back to main page
driver.switch_to.default_content()
print("Switched back to main content")

# Step 6: Open new window
driver.find_element(By.LINK_TEXT, "Elemental Selenium").click()
time.sleep(2)

# Step 7: Handle windows
parent_window = driver.current_window_handle
all_windows = driver.window_handles

for window in all_windows:
    driver.switch_to.window(window)
    print("Window title:", driver.title)

# Step 8: Close child window
for window in all_windows:
    if window != parent_window:
        driver.switch_to.window(window)
        driver.close()

# Step 9: Return to parent
driver.switch_to.window(parent_window)
print("Returned to parent window")

driver.quit()
