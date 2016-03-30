# coding=utf-8

class EditPageBlank(object):

    def __init__(self, driver):
        self.driver = driver
        # 画布区域
        self.blankarea = self.driver.find_element_by_xpath("//section")

    # 获取画布中存在的图例或控件
    def get_graphorctrl_inblank(self, name):
        graphorctrl_inblank = self.driver.find_element_by_xpath("//div[@name='" + name + "']")
        return graphorctrl_inblank

    # 获取图例或控件上的三个按钮
    # 收起按钮
    def get_minbutton(self, name):
        graphorctrl_inblank = self.get_graphorctrl_inblank(name)
        minbutton = graphorctrl_inblank.find_element_by_xpath("./div/div[1]/div")
        return minbutton

    # 编辑按钮
    def get_editbutton(self, name):
        graphorctrl_inblank = self.get_graphorctrl_inblank(name)
        editbutton = graphorctrl_inblank.find_element_by_xpath("./div/div[1]/img[2]")
        return editbutton

    # 删除按钮
    def get_delbutton(self, name):
        graphorctrl_inblank = self.get_graphorctrl_inblank(name)
        delbutton = graphorctrl_inblank.find_element_by_xpath("./div/div[1]/img[1]")
        return delbutton

    # 图表组件的展示区域
    def get_graph_show(self, name):
        return self.get_graphorctrl_inblank(name).find_element_by_xpath("./div/div[3]/div/div/canvas[3]")

    # 控件的展示区域
    def get_ctrl_show(self, name):
        return self.get_graphorctrl_inblank(name).find_element_by_xpath("./div/div[3]")

    # 点击收起按钮
    def click_minbutton(self, name):
        # self.driver.execute_script("arguments[0].click();", self.get_graphorctrl_inblank(name))
        # 需要新建
        self.get_graphorctrl_inblank(name).click()

    # 点击编辑按钮
    def click_editbutton(self, name):
        self.get_editbutton(name).click()

    # 点击删除按钮
    def click_delbutton(self, name):
        self.get_delbutton(name).click()