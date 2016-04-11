# coding=utf-8
from selenium import webdriver
from mainpage import MainPage
import time
from login import login
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from xiecha_viewpage import XieChaViewPage
from zhengzaixiecha import ZheZaiXieChaPage


class WeiTuoDanPage(MainPage):

    def __init__(self, driver):
        # MainPage.__init__(self, driver)
        super(WeiTuoDanPage, self).__init__(driver)
        # 保存样本按钮
        self.save_sample_btn = self.driver.find_element_by_xpath("//button[text()='保存样本']")

        # 提交委托单按钮
        self.submit_btn = self.driver.find_element_by_xpath("//button[text()='提交委托']")

    # 点击保存样本按钮
    def click_save_sample_btn(self):
        self.save_sample_btn.click()

    # 点击提交委托按钮
    def click_submit_btn(self):
        self.driver.execute_script("arguments[0].click();", self.submit_btn)

    # 选择委托单协查标签，参数为标签名称
    def click_tab(self, tab):
        self.driver.find_element_by_xpath("//button[text()='" + tab + "']").click()

    # 填写案件协查单
    def fill_weituodan_ajxc(self, casename, prospectingno, casenum, casedate, casenature, province,
                       city, county, requestdemand, caserelated):
        self.driver.find_element_by_name("caseName").send_keys(casename)
        self.driver.find_element_by_name("prospectingNo").send_keys(prospectingno)
        self.driver.find_element_by_name("caseNum").send_keys(casenum)
        self.driver.find_element_by_name("caseDate").click()
        self.driver.find_element_by_link_text(casedate).click()
        self.driver.find_element_by_xpath("//span[text()='" + casenature + "']/preceding-sibling::input").click()
        self.driver.find_element_by_name("proID").find_element_by_xpath("//option[text()='" + province + "']").click()
        self.driver.find_element_by_name("cityId").find_element_by_xpath("//option[text()='" + city + "']").click()
        self.driver.find_element_by_name("countryId").find_element_by_xpath("//option[text()='" + county + "']").click()
        self.driver.find_element_by_xpath("//span[text()='" + requestdemand + "']/preceding-sibling::input").click()
        self.driver.find_element_by_name("caseRelated").send_keys(caserelated)

    # 填写人员协查单
    def fill_weituodan_ryxc(self, persontype, personname, identityno, casenum, casedate,
                            province, city, county, requestdemand, caserelated):
        self.click_tab("人员协查")
        self.driver.find_element_by_xpath("//span[text()='" + persontype + "']/preceding-sibling::input").click()
        self.driver.find_element_by_name("personName").send_keys(personname)
        self.driver.find_element_by_name("identityNo").send_keys(identityno)
        self.driver.find_element_by_name("caseNum").send_keys(identityno)
        self.driver.find_element_by_name("caseDate").send_keys(casedate)
        self.driver.find_element_by_name("proID").find_element_by_xpath("//option[text()='" + province + "']").click()
        self.driver.find_element_by_name("cityId").find_element_by_xpath("//option[text()='" + city + "']").click()
        self.driver.find_element_by_name("countryId").find_element_by_xpath("//option[text()='" + county + "']").click()
        self.driver.find_element_by_xpath("//span[text()='" + requestdemand + "']/preceding-sibling::input").click()
        self.driver.find_element_by_name("caseRelated").send_keys(caserelated)

    # 填写未知名尸体协查单
    def fill_weituodan_wzmstxc(self, casename, prospectingno, casenum, casedate, casenature, province,
                       city, county, requestdemand, caserelated):

        self.click_tab("未知名尸体协查")
        self.fill_weituodan_ajxc(casename, prospectingno, casenum, casedate, casenature, province,
                       city, county, requestdemand, caserelated)

    # 填写STR DNA头信息
    def fill_STRDNA(self, samplename, labname, remarks):
        self.driver.find_element_by_name("sampleName").send_keys(samplename)
        self.driver.find_element_by_name("labName").send_keys(labname)
        if(u'本人' in self.driver.page_source):
            self.driver.find_element_by_xpath("//span[text()='" + remarks + "']/preceding-sibling::input").click()
        else:
            self.driver.find_element_by_name("remarks").send_keys(remarks)

    # 上传CODIS文件
    def up_codies_file(self, filepath):
        self.driver.find_element_by_name("myfile").send_keys(filepath)

    # 填充CODIS数据
    def fill_codies_date(self):
        pass

    # 上传文件
    def up_file(self, filepath):
        self.driver.find_element_by_id("componentList").send_keys(filepath)


if __name__ == "__main__":

    driver = webdriver.Firefox()
    driver.maximize_window()
    login(driver, "ptyh", "123456")
    driver.implicitly_wait(10)
    driver.find_element_by_link_text("填写委托单").click()
    time.sleep(5)
    weituodan = WeiTuoDanPage(driver)
    weituodan.fill_weituodan_ajxc(u'0408案', '001', '0020', '8', '盗窃',
                                     '山西省', '太原市', '小店区', '亲缘关系（三联体）比对',
                                     u'朱宇一夜醒来成为了木匠皇帝朱由校，传说中的一代昏君，然而他发现事实并非这么回事')
    # print os.getcwd() + "\\222.dat"
    # weituodan.up_codies_file("C:\\Users\\Administrator\\Desktop\\demoexe\\222.dat")
    weituodan.up_codies_file(os.getcwd() + "\\222.dat")
    driver.find_element_by_xpath("//input[@value='20140305-104451']").click()
    driver.find_element_by_xpath("//button[text()='上传codis']").click()
    weituodan.fill_STRDNA("SDNA001", "KDW000022345", u"生母")
    time.sleep(3)
    weituodan.click_save_sample_btn()
    weituodan.click_submit_btn()
    weituohao = driver.find_element_by_xpath("//span[text()='委托号：']/following-sibling::span").text
    print weituohao
    '''
    time.sleep(5)
    driver.refresh()
    weituodan.goto_page("正在协查")
    zzxcpage = ZheZaiXieChaPage(driver)
    zzxcpage.click_show_condition()
    zzxcpage.fill_search_condition(delegationnum=weituohao)
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
            xiechaviewpage.upload_file(u"C:\\Users\\Administrator\\Desktop\\测试环境.txt")
            # ActionChains(driver).send_keys(Keys.SPACE)
            driver.execute_script("window.scrollBy(0,document.body.scrollHeight)","")
            xiechaviewpage.click_savebtn()
            xiechaviewpage.click_xiechajieguo("已查中")
            xiechaviewpage.click_zhuanjiajianyi("1")
            xiechaviewpage.click_querenfankui()
'''