from selenium import webdriver

driver = webdriver.Chrome(executable_path = "c:\selenium browser drivers\chromedriver.exe")
driver.get("https://cleveronly.com/brainbucket/index.php?route=account/register")

firstname_input = driver.find_element_by_name("firstname")
firstname_input.send_keys("Nikita")

lastname_input = driver.find_element_by_name("lastname")
lastname_input.send_keys("Chesnakov")

email_input = driver.find_element_by_name("email")
email_input.send_keys("Nikitos@gmail.com")

tel_input = driver.find_element_by_name("telephone")
tel_input.send_keys("9128968227")

address_input = driver.find_element_by_name("address_1")
address_input.send_keys("Pushkin Street house 1 appartment 15")

city_input = driver.find_element_by_name("city")
city_input.send_keys("Kaliningrad")

country_input = driver.find_element_by_name("country_id")
country_input.send_keys("Russia")

# region_input = driver.find_element_by_name("zone_id")
# region_input.send_keys("Kaliningrad Region")

password_input = driver.find_element_by_name("password")
password_input.send_keys("Chelyaba@174")

confirm_input = driver.find_element_by_name("confirm")
confirm_input.send_keys("Chelyaba@174")