from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
browser.implicitly_wait(20)

browser.get("http://uitestingplayground.com/textinput")
element = browser.find_element(By.CSS_SELECTOR, "#newButtonName")
element.send_keys("SkyPro")
browser.find_element(By.CSS_SELECTOR, "#updatingButton").click()

txt = browser.find_element(By.CSS_SELECTOR, "#updatingButton").text
print(txt)

browser.quit()