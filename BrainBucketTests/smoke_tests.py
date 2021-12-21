from selenium import webdriver

driver = webdriver.Chrome(executable_path = "c:\selenium browser drivers\chromedriver.exe")

driver.get("https://cleveronly.com/brainbucket/index.php?route=account/login")

email_field = driver.find_element_by_name("email")
email_field.send_keys("mashka@gmail.com")

password_field = driver.find_element_by_name("password")
password_field.send_keys("ulianka88")

login_button = driver.find_element_by_xpath("//body//div/div[2]/div/form/input")
login_button.click()