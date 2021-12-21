from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path = "c:\selenium browser drivers\chromedriver.exe")

driver.get("https://cleveronly.com/brainbucket/index.php?route=account/login")

continue_button = WebDriverWait(driver, 15)\
    .until(EC.element_to_be_clickable(((By.XPATH,'//html/body/div[2]//div/div[1]//a'))))
continue_button.click()

register_title = WebDriverWait(driver,15).until(EC.visibility_of_element_located((By.XPATH,"/html/body//h1")))


