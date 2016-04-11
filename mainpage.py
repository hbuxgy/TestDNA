# coding=utf-8

from selenium import webdriver
import time
from login import login

class MainPage(object):

    def __init__(self, driver):
        self.driver = driver

    def goto_page(self, labletext):
        pagelable = self.driver.find_element_by_partial_link_text(labletext)
        self.driver.execute_script("arguments[0].click();", pagelable)


if __name__ == "__main__":
    driver = webdriver.Firefox()
    mainpage = MainPage(driver)
    driver.maximize_window()
    login(driver, "test2", "123456")
    driver.implicitly_wait(10)
    mainpage.goto_page("等待受理")
    time.sleep(5)
    mainpage.goto_page("尚未签收")
    time.sleep(5)
    mainpage.goto_page("已经签收")
    time.sleep(5)
    mainpage.goto_page("综合查询")
    time.sleep(5)
    mainpage.goto_page("综合统计")
    time.sleep(5)
    driver.quit()
