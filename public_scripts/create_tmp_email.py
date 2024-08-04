from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path
import time

# Set up Firefox options
options = Options()
options.headless = False  # Set to False if you want to see the browser window

# Path to your Firefox profile
profile_path =  Path.home() / 'AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\24k284ql.default-release'  # Update this to your profile path
options.profile = profile_path

# Initialize WebDriver with profile
driver = webdriver.Firefox(options=options)

if __name__ == "__main__":
     # Open the Emailnator website
    driver.get('https://www.emailnator.com/')
    
    # Wait for the checkboxes to be present
    wait = WebDriverWait(driver, 10)
    domain_checkbox = wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'Domain')]")))
    plus_gmail_checkbox = wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(text(), '+Gmail')]")))
    googlemail_checkbox = wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'GoogleMail')]")))
    gmail_checkbox = wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(text(), '.Gmail')]")))

    # Unselect Domain, +Gmail, and GoogleMail so the only selected option is .Gmail
    if not domain_checkbox.is_selected():
        domain_checkbox.click()
    if not plus_gmail_checkbox.is_selected():
        plus_gmail_checkbox.click()
    if not googlemail_checkbox.is_selected():
        googlemail_checkbox.click()
    if gmail_checkbox.is_selected():
        gmail_checkbox.click()

    # Click on "Generate New"
    generate_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Generate New')]")))
    generate_button.click()
    time.sleep(1)

    # Click on "Go!"
    go_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Go')]")))
    go_button.click()

    # Wait for the email to be generated and then copy it
    copy_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Copy')]")))
    copy_button.click()

