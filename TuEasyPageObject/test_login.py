# coding=utf-8
from selenium import webdriver
import unittest
import loginpage
import time

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://192.168.0.6/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        loginpage = loginpage.LoginPage(self.driver)
        loginpage.login("yujiezhang", "yujiezhang")
        time.sleep(5)
        assert "graph" in self.driver.current_url, "登录失败!"