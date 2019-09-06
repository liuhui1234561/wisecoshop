#encoding = utf-8

from common.desired_caps import *
from common.element_action import *
import config.readConfig as readConfig
from common.driverUtil import driver
from database.connDB import *
from common.element_action import *
import time
import unittest

localReadConfig = readConfig.ReadConfig()


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        isUpdate("com.wiseco.wisecoshop:id/cancel")

        clickAction("com.wiseco.wisecoshop:id/navigation_home_user")
        print("进入个人中心模块")


    def testLogin(self):


        try:


            isElementExist("com.wiseco.wisecoshop:id/user_phone_num")
            mobile = driver.find_element_by_id("com.wiseco.wisecoshop:id/user_phone_num").text


            # 未登录状态下，进行登录操作
            if mobile == "登录":
                driver.find_element_by_id("com.wiseco.wisecoshop:id/user_phone_num").click()
                print("未登录状态，点击登录按钮去登录")

                mobile = driver.find_element_by_id("com.wiseco.wisecoshop:id/login_phone_number")
                print("输入手机号,获取验证码")
                mobile.send_keys(localReadConfig.get_user("mobile"))
                time.sleep(1)
                driver.find_element_by_id("com.wiseco.wisecoshop:id/login_now").click()

                code = driver.find_element_by_id("com.wiseco.wisecoshop:id/login_phone_number")
                print("输入验证码,确认登录")
                code.send_keys(localReadConfig.get_user("valicode"))
                time.sleep(1)
                driver.find_element_by_id("com.wiseco.wisecoshop:id/login_now").click()



                # 判断用户是否已设置密码
                time.sleep(2)
                a = localReadConfig.get_user("mobile")[0:3] + "******" + localReadConfig.get_user("mobile")[9:11]
                sql1 = "select password from user_extension where mobileNumber = '%s'" %a
                if (queryOneData(sql1,"database_diversion")[0] is None):
                    print("未设置密码，点击以后再设置")
                    clickAction("com.wiseco.wisecoshop:id/login_password_after")
                else:
                    print("已是登录状态")


            else:
                print("已是登录状态")


        except Exception as e:
            print(e)
