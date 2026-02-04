from selenium import webdriver

# Open Firefox browser
driver = webdriver.Firefox()

# Navigate to website
driver.get("https://example.com")

# Print page title and URL
print("Page Title:", driver.title)
print("Page URL:", driver.current_url)

# Close the browser
driver.quit()
