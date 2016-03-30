# coding=utf-8
import time

class EditPageHead(object):

    def __init__(self, driver):
        self.driver = driver
        # 分辨率标签
        self.fbllable = self.driver.find_element_by_class_name("size")
        # 演示标签
        self.yanshilable = self.driver.find_element_by_xpath("//span[text()='演示']")
        # 保存标签
        self.baocunlable = self.driver.find_element_by_xpath("//span[text()='保存']")
        # 下载标签
        self.xiazailable = self.driver.find_element_by_xpath("//span[text()='下载']")
        # 画布区域
        # self.section = self.driver.find_element_by_xpath("//section")
        # 扩大标签
        self.kuoda = self.driver.find_element_by_xpath("//span[@title='放大']")
        # 缩小标签
        self.suoxiao = self.driver.find_element_by_xpath("//span[@title='缩小']")
        # 编辑区域缩略图查看框
        self.demoframe = self.driver.find_element_by_xpath("//span[@title='缩小']/preceding-sibling::div")
        # 增加一页ppt标签
        self.addppt = self.driver.find_element_by_xpath("//span[@titile='增加一页']")
        # 删除此页ppt标签
        self.delppt = self.driver.find_element_by_xpath("//span[@title='删除此页']")
        # 前一页标签
        self.prevppt = self.driver.find_element_by_xpath("//span[@title='前一页']")
        # 后一页标签
        self.nextppt = self.driver.find_element_by_xpath("//span[@title='后一页']")
        # 当前被选中的ppt缩略图
        self.pptshot = self.driver.find_element_by_xpath("//li[@class='selected']/img")

    # 点击分辨率标签
    def click_fbllable(self):
        self.fbllable.click()

    # 点击演示
    def click_yanshilable(self):
        self.yanshilable.click()

    # 点击保存
    def click_baocunlable(self):
        self.baocunlable.click()
        time.sleep(10)

    # 点击下载
    def click_xiazailable(self):
        self.xiazailable.click()

    # 点击扩大标签
    def click_kuoda(self):
        self.kuoda.click()

    # 点击缩小标签
    def click_suoxiao(self):
        self.suoxiao.click()

    # 点击增加一页标签
    def click_addppt(self):
        self.addppt.click()

    # 点击删除此页标签
    def click_delppt(self):
        self.delppt.click()

    # 点击前一页
    def click_prevppt(self):
        self.prevppt.click()

    # 点击后一页
    def click_nextppt(self):
        self.nextppt.click()