from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path = "c:\selenium browser drivers\chromedriver.exe")

driver.get("https://sesorafrica.org/")
driver.maximize_window()

instagram_btn = driver.find_element_by_xpath("//*[@class='fab fa-instagram']")
instagram_btn.click()

facebook_btn = driver.find_element_by_xpath("//*[@class='fab fa-facebook-f']")
facebook_btn.click()

twitter_btn = driver.find_element_by_xpath("//*[@class='fab fa-twitter-square']")
twitter_btn.click()

home_btn = driver.find_element_by_xpath("//*[@id='menu-item-175']")
home_btn.click()

terms_conditions_btn = driver.find_element_by_xpath("//*[@id='menu-item-177']")
terms_conditions_btn.click()

contact_us_btn = driver.find_element_by_xpath("//*[@id='menu-item-176']")
contact_us_btn.click()


