from selenium import webdriver
import  time
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
# driver.save_screenshot("C:/")
driver.find_element_by_id("kw").send_keys("python")#定位和操作
driver.find_element_by_id("su").clic

driver.page_source#获取到浏览器中的element的内容
print(driver.current_url)#获取window.location上的url地址
time.sleep(3)
driver.close()#退出当前页面
driver.quit()#退出浏览器
