# coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://123.56.71.197:8080/DNA/dna/index.html#/?_k=ob8aam")
driver.implicitly_wait(10)
driver.find_element_by_id("userName").send_keys("test2")
driver.find_element_by_id("passWord").send_keys("123456")
driver.find_element_by_class_name("btn_login").click()
driver.find_element_by_xpath("html/body/div[1]/div/section/div[2]/div[2]/img").click()
driver.find_element_by_link_text("填写委托单").click()
driver.find_element_by_name("proID").find_element_by_xpath("//option[text()='河北省']").click()
driver.find_element_by_name("cityId").find_element_by_xpath("//option[text()='保定市']").click()
driver.find_element_by_name("countryId").find_element_by_xpath("//option[text()='望都县']").click()
time.sleep(5)
driver.quit()