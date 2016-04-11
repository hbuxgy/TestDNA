# coding=utf-8
from selenium import webdriver
from mainpage import MainPage
import time
from login import login

class DengDaiShouLiPage(MainPage):

    def __init__(self, driver):
        MainPage.__init__(self, driver)

    # 点击显示查询条件按钮
    def click_show_condition(self):
        show_condition_btn = self.driver.find_element_by_xpath(
            "//legend[text()='等待受理查询']/following-sibling::button")
        show_condition_btn.click()

    # 点击查询按钮
    def click_search_btn(self):
        self.driver.find_element_by_xpath("//button[text()='查询']").click()

    # 输入查询条件
    def fill_search_condition(self, delegationnum="", casetype="-- 全部 --", casename="", casenature="-- 全部 --",
                              prospectingno="", casenum="", personname="", identityno="", casedate="", province="--省--",
                              city="--市--", county="--区/县--", starttime="", endtime=""):
        self.click_show_condition()
        self.driver.find_element_by_name("delegationNumber").send_keys(delegationnum)
        self.driver.find_element_by_name("caseType").find_element_by_xpath(
            "//option[text()='" + casetype + "']").click()
        self.driver.find_element_by_name("caseName").send_keys(casename)
        self.driver.find_element_by_name("caseNature").find_element_by_xpath(
            "//option[text()='" + casenature + "']").click()
        self.driver.find_element_by_name("prospectingNo").send_keys(prospectingno)
        self.driver.find_element_by_name("caseNum").send_keys(casenum)
        self.driver.find_element_by_name("personName").send_keys(personname)
        self.driver.find_element_by_name("identityNo").send_keys(identityno)
        self.driver.find_element_by_name("caseDate").send_keys(casedate)
        self.driver.find_element_by_name("proID").find_element_by_xpath("//option[text()='" + province + "']").click()
        self.driver.find_element_by_name("cityId").find_element_by_xpath("//option[text()='" + city + "']").click()
        self.driver.find_element_by_name("countryId").find_element_by_xpath("//option[text()='" + county + "']").click()
        self.driver.find_element_by_name("start").send_keys(starttime)
        self.driver.find_element_by_name("end").send_keys(endtime)

    # 查看搜索列表内容
    # 委托号
    def get_text_delegationNumber(self):
        return self.driver.find_element_by_xpath("//tbody/tr[1]/td[2]").text

    # 协查种类
    def get_text_casetype(self):
        return self.driver.find_element_by_xpath("//tbody/tr[1]/td[3]").text

    # 案件名称/被协查人姓名
    def get_text_casenameorperson(self):
        return self.driver.find_element_by_xpath("//tbody/tr[1]/td[4]").text

    # 点击“受理”标签
    def click_accept_lable(self):
        self.driver.find_element_by_xpath("//tbody/tr[1]/td[7]/a").click()


if __name__ == "__main__":

    driver = webdriver.Firefox()
    driver.maximize_window()
    login(driver, "wzgl", "123456")
    driver.implicitly_wait(10)
    driver.find_element_by_partial_link_text("等待受理").click()
    dengdaishouli = DengDaiShouLiPage(driver)
    dengdaishouli.click_show_condition()
    dengdaishouli.fill_search_condition(delegationnum="20160329009")
    dengdaishouli.click_search_btn()
    dengdaishouli.click_accept_lable()
    time.sleep(5)
    driver.quit()