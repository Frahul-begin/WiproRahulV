from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

GRID_URL = "http://localhost:4444/wd/hub"

browsers = ["chrome", "firefox", "edge"]

for browser in browsers:

    if browser == "chrome":
        options = ChromeOptions()

    elif browser == "firefox":
        options = FirefoxOptions()

    elif browser == "edge":
        options = EdgeOptions()

    else:
        continue

    driver = webdriver.Remote(
        command_executor=GRID_URL,
        options=options
    )

    # Navigate to website
    driver.get("https://www.google.com")

    # Verify page title
    assert "Google" in driver.title

    # Print browser name and platform
    capabilities = driver.capabilities
    print(f"Browser: {capabilities['browserName']}")
    print(f"Platform: {capabilities.get('platformName', 'Unknown')}")
    print("-" * 40)

    driver.quit()
