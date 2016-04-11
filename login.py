# coding=utf-8

def login(driver, username, password):

    driver.get("http://192.168.0.8:8080/DNA/dna/index.html")
    driver.implicitly_wait(10)
    driver.find_element_by_id("userName").send_keys(username)
    driver.find_element_by_id("passWord").send_keys(password)
    driver.find_element_by_class_name("btn_login").click()
    # 专家协查
    driver.find_element_by_xpath("//img[@data-reactid='.0.1.1.1.0']").click()