from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()
# Start the browser
browser = webdriver.Chrome(service=Service(driver_path))

browser.get('https://gettop.us/')

browser.find_element(By.XPATH, "//a[text()='Phones' and @class='nav-top-link']").click()

expected_result = 'HOME / SMARTPHONE'
actual_result = browser.find_element(By.XPATH, "//nav[contains(@class, 'breadcrumbs')]").text

assert actual_result == expected_result, f'Error! Actual {actual_result} did not match expected {expected_result}'
print('Phone Test cases passed')

browser.find_element(By.XPATH, "//a[text()='Laptops' and @class='nav-top-link']").click()

expected_result = 'HOME / LAPTOP'
actual_result = browser.find_element(By.XPATH, "//nav[contains(@class, 'breadcrumbs')]").text

assert actual_result == expected_result, f'Error! Actual {actual_result} did not match expected {expected_result}'
print('Laptop Test cases passed')

browser.quit()
