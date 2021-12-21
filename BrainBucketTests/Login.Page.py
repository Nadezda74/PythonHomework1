from selenium import webdriver

driver = webdriver.Chrome(executable_path = "c:\selenium browser drivers\chromedriver.exe")

driver.get("https://cleveronly.com/brainbucket/index.php?route=account/login")

email_field = driver.find_element_by_name("email")
email_field.send_keys("Nikitos@gmail.com")

password_field = driver.find_element_by_name("password")
password_field.send_keys("Chelyabinsk74")

login_field = driver.find_element_by_xpath("//body//div[2]//form/input")
login_field.click()