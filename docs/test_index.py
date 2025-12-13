from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("file:///C:/Users/hanna/PyCharmProjects/PythonProject/docs/index.html")

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "a"))
)

driver.find_element(By.ID, "a").send_keys("2")
driver.find_element(By.ID, "b").send_keys("3")
driver.find_element(By.ID, "btn").click()

time.sleep(5)
driver.quit()

