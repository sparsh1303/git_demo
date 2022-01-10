from selenium import webdriver

driver = webdriver.Firefox()
driver.set_window_size(700,600)
driver.get("https://www.google.com")