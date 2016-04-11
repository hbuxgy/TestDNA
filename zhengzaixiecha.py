# coding=utf-8
from dengdaishouli import DengDaiShouLiPage
from selenium import webdriver
from login import login

class ZheZaiXieChaPage(DengDaiShouLiPage):

    def __init__(self, driver):
        super(ZheZaiXieChaPage, self).__init__(driver)

    # 点击显示查询条件按钮
    def click_show_condition(self):
        show_condition_btn = self.driver.find_element_by_xpath(
            "//legend[text()='正在协查查询']/following-sibling::button")
        show_condition_btn.click()

    # 获得委托单位信息
    def get_text_delegation_org(self):
        return self.driver.find_element_by_xpath("//tbody/tr[1]/td[5]")

    # 点击“查看”按钮
    def click_view_btn(self):
        self.driver.find_element_by_xpath("//tbody/tr[1]/td[7]/a").click()


if __name__ == "__main__":

    driver = webdriver.Firefox()
    driver.maximize_window()
    login(driver, "test2", "123456")
    driver.implicitly_wait(10)
    driver.find_element_by_partial_link_text("正在协查").click()
    zzxcpage = ZheZaiXieChaPage(driver)
    # zzxcpage.click_show_condition()
    zzxcpage.fill_search_condition(delegationnum="20160301001")
    zzxcpage.click_search_btn()
    zzxcpage.click_view_btn()
    zzxcpage.goto_page("综合查询")