# coding=utf-8
from selenium import webdriver
import time
from login import login
from zhengzaixiecha import ZheZaiXieChaPage

class XieChaViewPage(object):

    def __init__(self, driver):
        self.driver = driver

    # 上传文件
    def upload_file(self, filepath):
        self.driver.find_element_by_id("InputFile").send_keys(filepath)

    # 点击保存
    def click_savebtn(self):
        self.driver.find_element_by_class_name("SaveBtn").click()

    # 选择协查结果，result是名称
    def click_xiechajieguo(self, result):
        if result == "未查中":
            self.driver.find_element_by_id("radio1").click()
        elif result == "已查中":
            self.driver.find_element_by_id("radio2").click()
        else:
            self.driver.find_element_by_id("radio3").click()

    # 选择专家建议
    def click_zhuanjiajianyi(self, value):
        self.driver.find_element_by_class_name("SelectList").find_element_by_xpath(
            "//option[@value='" + value + "']").click()

    # 复核确认反馈
    def click_querenfankui(self):
        self.driver.find_element_by_class_name("btn_2").click()

    # 返回
    def click_fanhui(self):
        self.driver.find_element_by_class_name("btn_1").click()


if __name__=="__main__":
    driver = webdriver.Firefox()
    driver.maximize_window()
    login(driver, "wzpt", "123456")
    driver.implicitly_wait(10)
    driver.find_element_by_partial_link_text("正在协查").click()
    zzxcpage = ZheZaiXieChaPage(driver)
    # zzxcpage.click_show_condition()
    zzxcpage.fill_search_condition(delegationnum="20160408015")
    zzxcpage.click_search_btn()
    zzxc_handle = driver.current_window_handle
    print zzxc_handle
    zzxcpage.click_view_btn()
    time.sleep(3)
    all_handles = driver.window_handles
    for handle in all_handles:
        if handle != zzxc_handle:
            driver.switch_to.window(handle)
            print handle
            xiechaviewpage = XieChaViewPage(driver)
            driver.execute_script("var q=document.documentElement.scrollTop=100000")
            xiechaviewpage.upload_file(u"C:\\Users\\Administrator\\Desktop\\测试环境.txt")
            # ActionChains(driver).send_keys(Keys.SPACE)
            xiechaviewpage.click_savebtn()
            xiechaviewpage.click_xiechajieguo("已查中")
            xiechaviewpage.click_zhuanjiajianyi("1")
            xiechaviewpage.click_querenfankui()