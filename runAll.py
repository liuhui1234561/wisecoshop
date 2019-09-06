#coding=utf-8


from test_case.test02_loan import *
from test_case.ttest01_login import *
from HTMLTestRunner import HTMLTestRunner
import os
import unittest

test_dir = './test_case'
discover = unittest.defaultTestLoader.discover(start_dir='./test_case', pattern="test*.py")

if __name__ == "__main__":
    report_dir = './test_report'
    os.makedirs(report_dir, exist_ok=True)
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    report_name = '{0}/{1}.html'.format(report_dir, now)

    with open(report_name, 'wb')as f:
        runner = HTMLTestRunner(stream=f, title="测试报告", description="本测试报告内容包含快易省app基本功能回归")
        runner.run(discover)