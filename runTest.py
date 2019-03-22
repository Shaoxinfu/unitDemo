import os
import time
import unittest

from BeautifulReport import BeautifulReport


if __name__ == '__main__':
    # discover(case_dir,pattern,top_level_dir)
    # discover方法里面有三个参数：1、表示待执行用例的目录；2、匹配脚本名称的规则；3、顶层目录的名称，一般默认为None
    suite_tests = unittest.defaultTestLoader.discover("test_case", pattern="mathTest.py",top_level_dir=None)
    BeautifulReport(suite_tests).report(filename='report', description='测试报告', log_path="report")  # log_path='.'把report放到当前目录下
