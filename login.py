# coding=utf-8
from selenium import webdriver

def login(username, password):
    driver = webdriver.Firefox()
    driver.get("http://123.56.71.197:8080/DNA/dna/index.html#/?_k=03ur62")
    driver.implicitly_wait(10)
    driver.find_element_by_id("userName").send_keys(username)
    driver.find_element_by_id("passWord").send_keys(password)
    driver.find_element_by_class_name("btn_login").click()
    driver.find_element_by_xpath("//img[@data-reactid='.0.1.1.1.0']").click()