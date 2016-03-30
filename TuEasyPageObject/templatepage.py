# coding=utf-8

import time

'''模板页面'''
class TemplatePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.template_radio = self.driver.find_element_by_xpath("//span[text()='模板']")
        self.document_radio = self.driver.find_element_by_xpath("//span[text()='文档']")

    # 根据名称获得整个模板元素
    def get_template(self, templatename):
        template = self.driver.find_element_by_xpath(
            "//span[text()='" + templatename + "']/parent::div/preceding-sibling::div/div[@class='spanArea']")
        return template

    '''标题在非编辑状态时获取模板标题元素'''
    def get_title_noteditable(self, templatename):
        template_title = self.driver.find_element_by_xpath("//span[text()='" + templatename + "']")
        return template_title

    '''标题在编辑状态时获取模板标题元素'''
    def get_title_editable(self):
        template_edittitle = self.driver.find_element_by_xpath("//span[@contenteditable='true']")
        return template_edittitle

    # 获取标题编辑按钮
    def get_title_editbtn(self, templatename):
        title_editbtn = self.driver.find_element_by_xpath("//span[text()='" + templatename + "']/following-sibling::i")
        return title_editbtn

    # 点击标题编辑按钮
    def click_title_editbtn(self, templatename):
        editbtn = self.get_title_editbtn(templatename)
        self.driver.execute_script("arguments[0].click();", editbtn)

    # 输入标题名称
    def type_title_name(self, templatename, newname):
        self.get_title_editable(templatename).send_keys(newname)

    # 获得对应模板查看按钮
    def get_lookbtn(self, templatename):
        template = self.get_template(templatename)
        lookbtn = template.find_element_by_xpath("./span[1]")
        return lookbtn

    # 获得对应模板创建按钮
    def get_createbtn(self, templatename):
        template = self.get_template(templatename)
        createbtn = template.find_element_by_xpath("./span[3]")
        return createbtn

    # 获得对应模板删除按钮
    def get_deletebtn(self, templatename):
        template = self.get_template(templatename)
        deletebtn = template.find_element_by_xpath("./span[5]")
        return deletebtn

    # 点击查看按钮
    def click_lookbtn(self, templatename):
        lookbtn = self.get_lookbtn(templatename)
        # lookbtn.click()
        self.driver.execute_script("arguments[0].click();", lookbtn)

    # 点击创建按钮
    def click_createbtn(self, templatename):
        createbtn = self.get_createbtn(templatename)
        self.driver.execute_script("arguments[0].click();", createbtn)

    # 点击删除按钮
    def click_deletebtn(self, templatename):
        deletebtn = self.get_deletebtn(templatename)
        self.driver.execute_script("arguments[0].click();", deletebtn)
        time.sleep(3)

    # 点击模板radio
    def click_template_radio(self):
        self.template_radio.click()

    # 点击文档radio
    def click_document_radio(self):
        self.document_radio.click()

    # 获取编辑按钮
    def get_editbtn(self, docname):
        docment = self.get_template(docname)
        editbtn = docment.find_element_by_xpath("./span[2]")
        return editbtn

    # 获取推荐到模板按钮
    def get_recommendbtn(self, docname):
        docment = self.get_template(docname)
        recommendbtn = docment.find_element_by_xpath("./span[4]")
        return recommendbtn

    # 点击编辑按钮
    def click_editbtn(self, docname):
        editbtn = self.get_editbtn(docname)
        self.driver.execute_script("arguments[0].click();", editbtn)

    # 点击推荐按钮
    def click_recommendbtn(self, docname):
        recommendbtn = self.get_recommendbtn(docname)
        self.driver.execute_script("arguments[0].click();", recommendbtn)
        time.sleep(3)

    '''创建新文档'''
    def create_newdoc(self, templatename, createdocname):
        self.click_createbtn(templatename)
        self.driver.find_element_by_xpath("//input[@placeholder='新建文档名字']").send_keys(createdocname)
        self.driver.find_element_by_xpath("//span[text()='确定']").click()
        time.sleep(3)

    '''删除文档'''
    def delete_doc(self, templatename):
        # 点击删除按钮
        self.click_deletebtn(templatename)
        # 确定
        self.driver.find_element_by_xpath("html/body/div[3]/div/button[1]").click()