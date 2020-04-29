from selenium import webdriver
import time
import requests
driver = webdriver.Chrome()
driver.get("http://120.197.235.93/dqpt/glzt/dist/#/login")
# driver.find_element_by_xpath("//ul[@class = 'tab-start']/li[@class = 'account-tab-account on']").click()
element = driver.find_elements_by_class_name("el-input__inner")
element[0].send_keys("cmicnb")
element[1].send_keys("111111")
time.sleep(5)
driver.find_element_by_css_selector("[class = 'el-button login_btn el-button--primary']").click()

cookie= driver.get_cookies()#获取cookie
cookies = {i["name"] : i["value"] for i in cookie}
print(cookies)
time.sleep(3)
