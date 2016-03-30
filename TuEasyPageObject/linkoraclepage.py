# coding=utf-8

class LinkOraclePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.serverip = self.driver.find_element_by_xpath("//h5[text()='服务器']/following-sibling::input")
        self.port = self.driver.find_element_by_xpath("//h5[text()='端口']/following-sibling::input")
        self.servicename = self.driver.find_element_by_xpath("//h5[text()='服务']/following-sibling::input")
        self.win_identity_radio = self.driver.find_element_by_xpath("//span[@value='使用Windows身份验证']")
        self.specific_identity_radio = self.driver.find_element_by_xpath("//span[@value='使用特定用户名和密码']")
        self.oracle_username = self.driver.find_element_by_xpath("//h5[text()='用户名']/following-sibling::input")
        self.oracle_password = self.driver.find_element_by_xpath("//h5[text()='密码']/following-sibling::input")
        self.confirm_btn = self.driver.find_element_by_xpath("//input[@value='确定']")
        self.cancel_btn = self.driver.find_element_by_xpath("//input[@value='取消']")

    def click_win_radio(self):
        self.win_identity_radio.click()

    def click_specific_radio(self):
        self.specific_identity_radio.click()

    def loginoracle(self, serverip, port, servicename, oracle_username, oracle_password):
        self.serverip.clear()
        self.serverip.send_keys(serverip)
        self.port.clear()
        self.port.send_keys(port)
        self.servicename.clear()
        self.servicename.send_keys(servicename)
        self.click_specific_radio()
        self.oracle_username.clear()
        self.oracle_username.send_keys(oracle_username)
        self.oracle_password.clear()
        self.oracle_password.send_keys(oracle_password)
        self.confirm_btn.click()

    def canclelogin(self):
        self.cancel_btn.click()