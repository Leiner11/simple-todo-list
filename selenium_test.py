from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

options = Options()
options.binary_location = "/snap/firefox/current/firefox.launcher"  # Ensure this points to the correct Firefox binary

# Set the path to your Selenium profile
profile_path = "/home/rubuntu/snap/firefox/common/.mozilla/firefox/Selenium"  # Update this path

options.set_preference("profile", profile_path)

service = Service()

driver = webdriver.Firefox(service=service, options=options)

# Test by opening a site
driver.get("https://www.google.com")
print(driver.title)

# Close the browser
driver.quit()
