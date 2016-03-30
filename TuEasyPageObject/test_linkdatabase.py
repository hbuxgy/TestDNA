# coding=utf-8
from linkoraclepage import LinkOraclePage
import unittest
from selenium import webdriver
import time
from loginpage import LoginPage
from templatepage import TemplatePage
from editpageleft import EditPageLeft
from linkmysqlpage import LinkMysqlPage

class TestLinkDatabase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://192.168.0.6/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_link(self):
        loginpage = LoginPage(self.driver)
        loginpage.login("yujiezhang", "yujiezhang")
        time.sleep(5)
        assert "graph" in self.driver.current_url, "登录失败!"
        temppage = TemplatePage(self.driver)
        temppage.click_document_radio()
        temppage.click_editbtn("测试")
        time.sleep(3)
        editpageleft = EditPageLeft(self.driver)
        tag = editpageleft.get_title_tag("导入数据")
        tag.click()
        # editpageleft.click_link_oracle()
        # oraclepage = LinkOraclePage(self.driver)
        # oraclepage.loginoracle("192.168.0.7", "1521", "orcl", "hydata", "hydata")
        # time.sleep(8)
        # self.driver.switch_to_alert().accept()
        # time.sleep(8)
        editpageleft.click_link_mysql()
        mysqlpage = LinkMysqlPage(self.driver)
        mysqlpage.loginmysql("192.168.0.6", "3306", "tueasy", "root", "abc_123456")
        time.sleep(8)