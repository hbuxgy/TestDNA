# coding=utf-8
from selenium import webdriver
import unittest
from loginpage import LoginPage
from templatepage import TemplatePage
from editpagehead import EditPageHead
import time
from editpageleft import EditPageLeft
from editpageblank import EditPageBlank

class TestEdit(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://192.168.0.6/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_edit(self):
        loginpage = LoginPage(self.driver)
        loginpage.login("yujiezhang", "yujiezhang")
        time.sleep(5)
        assert "graph" in self.driver.current_url, "登录失败!"
        temppage = TemplatePage(self.driver)
        temppage.click_document_radio()
        temppage.click_editbtn("测试")
        time.sleep(3)
        # editpage = EditPageLeft(self.driver)
        # tag = editpage.get_title_tag("导入数据")
        # tag.click()
        # time.sleep(3)
        # editpage.uploadfile("C:\Users\Administrator\Desktop\\testdata.xlsx")
        # editpage.click_link_oracle()
        a = EditPageBlank(self.driver)
        a.click_minbutton("文本域")
        self.assertEqual(a.get_ctrl_show("文本域").size, {'width': 0, 'height': 0})
        time.sleep(5)