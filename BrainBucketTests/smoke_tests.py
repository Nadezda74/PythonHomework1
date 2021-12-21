from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path = "c:\selenium browser drivers\chromedriver.exe")

driver.get("https://cleveronly.com/brainbucket/index.php?route=account/login")

email_field = driver.find_element_by_name("email")
email_field.send_keys("Nikitos@gmail.com")

password_field = driver.find_element_by_name("password")
password_field.send_keys("Chelyabinsk74")

login_field = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//body//div[2]//form/input")))
login_field.click()
