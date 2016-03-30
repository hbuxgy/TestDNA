# coding=utf-8
from selenium import webdriver
import unittest
from loginpage import LoginPage
from templatepage import TemplatePage
import time
from editpagehead import EditPage

class TestTemplate(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://192.168.0.6/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_template(self):
        loginpage = LoginPage(self.driver)
        loginpage.login("yujiezhang", "yujiezhang")
        time.sleep(5)
        assert "graph" in self.driver.current_url, "登录失败!"
        temppage = TemplatePage(self.driver)

        '''创建空白文档'''
        temppage.create_newdoc("空白模板", u"测试")
        editpage = EditPage(self.driver)
        editpage.click_baocunlable()
        self.driver.back()
        time.sleep(3)
        self.driver.back()
        time.sleep(5)
        temppage1 = TemplatePage(self.driver)
        temppage1.click_document_radio()
        time.sleep(5)
        assert u"测试" in self.driver.page_source