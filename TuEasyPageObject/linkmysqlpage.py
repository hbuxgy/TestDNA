# coding=utf-8

class LinkMysqlPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.serverip = self.driver.find_element_by_xpath("//h5[text()='服务器']/following-sibling::input")
        self.port = self.driver.find_element_by_xpath("//h5[text()='端口']/following-sibling::input")
        self.databasename = self.driver.find_element_by_xpath("//h5[text()='数据库']/following-sibling::input")
        self.mysql_username = self.driver.find_element_by_xpath("//h5[text()='用户名']/following-sibling::input")
        self.mysql_password = self.driver.find_element_by_xpath("//h5[text()='密码']/following-sibling::input")
        self.needssl = self.driver.find_element_by_xpath("//span[@value='需要SSL']")
        self.confirm_btn = self.driver.find_element_by_xpath("//input[@value='确定']")
        self.cancel_btn = self.driver.find_element_by_xpath("//input[@value='取消']")

    def loginmysql(self, serverip, port, databasename, mysql_username, mysql_password):
        self.serverip.clear()
        self.serverip.send_keys(serverip)
        self.port.clear()
        self.port.send_keys(port)
        self.databasename.clear()
        self.databasename.send_keys(databasename)
        self.mysql_username.clear()
        self.mysql_username.send_keys(mysql_username)
        self.mysql_password.clear()
        self.mysql_password.send_keys(mysql_password)
        self.confirm_btn.click()

    def canclelogin(self):
        self.cancel_btn.click()