from selenium import webdriver
import time

# setting out web driver (type of internet browser)
driver = webdriver.Chrome("webdriver location goes here")  # webdriver location
driver.set_page_load_timeout("10")


driver.get("http:/google.com")  # opening website
driver.find_element_by_name("q").send_keys("hello world")  # type into text box
driver.find_element_by_name("btnK").click()  # click on the search bar inspect button name="btnK"

time.sleep(4)
driver.quit()
