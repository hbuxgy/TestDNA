# coding=utf-8
import unittest
import time
import HTMLTestRunner

'''运行全部测试用例第二种方法discover'''
test_dir = "D:\\PyTest\\TuEasyTestCase"
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

if __name__ == "__main__":
    nowtime = time.strftime("%Y-%m-%d %H%M%S")
    filename = 'D:\\PyTest\\' + nowtime + ' TestResult.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='TuEasy_TestReport',
        description=u'图易产品测试报告'
    )
    runner.run(discover)
    fp.close()