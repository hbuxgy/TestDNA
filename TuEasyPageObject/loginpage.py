# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

'''登陆页面'''
class LoginPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.username_loc = (By.ID, 'userName')
        self.password_loc = (By.ID, 'passWord')
        self.loginbtn_loc = (By.ID, 'btnLogin')

    def login(self, username, password):
        self.driver.find_element(*self.username_loc).send_keys(username)
        self.driver.find_element(*self.password_loc).send_keys(password)
        self.driver.find_element(*self.loginbtn_loc).click()