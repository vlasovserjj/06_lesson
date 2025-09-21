from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

browser.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
browser.implicitly_wait(25)

browser.find_element(By.CSS_SELECTOR, "#landscape")

elemetn_3 = browser.find_element(By.CSS_SELECTOR, "#award")

txt = elemetn_3.get_attribute("src")
print(txt)

browser.quit()
