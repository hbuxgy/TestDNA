# coding=utf-8
from dengdaishouli import DengDaiShouLiPage
from selenium import webdriver
from login import login

class YiJingQianShouPage(DengDaiShouLiPage):

    def __init__(self, driver):
        super(YiJingQianShouPage, self).__init__(driver)

    # 点击显示查询条件按钮
    def click_show_condition(self):
        show_condition_btn = self.driver.find_element_by_xpath(
            "//legend[text()='已经签收查询']/following-sibling::button")
        show_condition_btn.click()

    # 获得委托单位信息
    def get_text_delegation_org(self):
        return self.driver.find_element_by_xpath("//tbody/tr[1]/td[5]")

    # 点击“查看”按钮
    def click_view_btn(self):
        self.driver.find_element_by_xpath("//tbody/tr[1]/td[8]/a").click()