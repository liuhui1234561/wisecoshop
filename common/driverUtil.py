#coding = utf-8


# 防止每次执行.py文件都要重新启动一次app


# 方法一：将driver初始化写在全局变量中，所有的测试.py文件都引用这个全局变量。 from driverUtile import driver便可使用driver
from common.desired_caps import *

driver = appium_desired()   # 初始化driver



# 方法二：单例模式可以确保某个类只有一个实例存在。让所有的.py文件公用一个driver，就可以避免多次启动app。
# import threading
# class DriverUtil(object):
#     """driver工具类"""
#
#     __instance = None  # 定义一个类属性
#     __instance_lock = threading.Lock()  # 加锁
#
#     @classmethod
#     def get_driver(cls):
#         """获取driver"""
#         with DriverUtil.__instance_lock:
#             if not DriverUtil.__instance:
#                 DriverUtil.__instance == appium_desired()
#         return DriverUtil.__instance

#使用时
# import unittest
# class SetTest(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.driver = DriverUtil.get_driver() # 单例
#         cls.set_view = SetView(cls.driver)