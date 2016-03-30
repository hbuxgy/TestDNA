# coding=utf-8

class EditPageLeft(object):

    def __init__(self, driver):
        self.driver = driver
        # 上传框
        self.upload = self.driver.find_element_by_id("uploadInput")
        # 链接Oracle元素
        self.link_oracle = self.driver.find_element_by_xpath("//div[@class='import-icon import-oracle']/img")
        # 链接MySql元素
        self.link_mysql = self.driver.find_element_by_xpath("//div[@class='import-icon import-mysql']/img")

    # 获取标题标签元素
    def get_title_tag(self, tagname):
        title_tag = self.driver.find_element_by_xpath("//dt[text()='" + tagname + "']")
        return title_tag

    # 获取图例或者控件元素
    def get_graph_or_control(self, name):
        graph_or_control = self.driver.find_element_by_xpath("//img[@title='" + name + "']")
        return graph_or_control

    # 获取文档样式元素
    def get_background_setter(self, backgroundname):
        background = self.driver.find_element_by_xpath("//img[@alt='" + backgroundname + "']")
        return background

    # 上传文件
    def uploadfile(self, filepath):
        # 修改元素可见
        self.driver.execute_script("document.getElementById('uploadInput').style.display = 'block';")
        self.upload.send_keys(filepath)

    # 点击链接Oracle数据库元素
    def click_link_oracle(self):
        self.link_oracle.click()

    # 点击链接Mysql数据库元素
    def click_link_mysql(self):
        self.driver.execute_script("arguments[0].click();", self.link_mysql)

    # 点击图表或控件元素
    def click_graph_or_control(self, name):
        graph_or_control = self.get_graph_or_control(name)
        self.driver.execute_script("arguments[0].click();", graph_or_control)







