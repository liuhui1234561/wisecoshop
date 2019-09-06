#encoding = utf-8


from common.element_action import *
from test_case.ttest03_card import *
import config.readConfig as readConfig
from database.connDB import *
import unittest
import time


localReadConfig = readConfig.ReadConfig()

class LoanPage(unittest.TestCase):


    @classmethod
    def setUpClass(cls):

        isUpdate("com.wiseco.wisecoshop:id/cancel")
        print("点击贷款进入为您推荐模块")
        clickAction("com.wiseco.wisecoshop:id/navigation_home_life")
        titleCheck("为您推荐")


    def test01List(self):

        titleCheck("为您推荐")

        if dataCheck():
            listid = "com.wiseco.wisecoshop:id/money_backname"
            infoid = "com.wiseco.wisecoshop:id/appay"
            inid = "com.wiseco.wisecoshop:id/commit"
            listAction(listid,infoid,inid)

            realinfostatus = self.getStatus("wise_user_exp","database_customer")
            showinfostatus = getText("com.wiseco.wisecoshop:id/text_finish_user")

            realbankstatus = self.getStatus("user_bank_card","database_engine")
            showbankstatus = getText("com.wiseco.wisecoshop:id/tvApplyAttentionBank")

            # 基础资料状态校验
            # if realinfostatus != showinfostatus:
            #     print("基础资料状态显示正确，为",realinfostatus)
            #
            # else:
            #     raise "基本资料状态显示不正确，实际是" + realinfostatus + "显示为" + showinfostatus
            #
            # if realinfostatus == "未完成":
            #     self.doCompleteBaseInfo()

            self.assertTrue(realinfostatus == showinfostatus,"不相同")
            self.verifyValue()
            print("111111")

            # 绑定银行卡状态校验
            if realbankstatus == showbankstatus:
                print("绑定银行卡状态显示正确，为", realbankstatus)

            else:
                raise "绑定银行卡状态显示不正确，实际是" + realbankstatus + "显示为" + showbankstatus

            if realbankstatus == "未完成":
                self.doBindBank()




            # print("点击以下相关借款协议，查看协议内容")
            # clickAction("com.wiseco.wisecoshop:id/user_data")
            # # OPPO R15的手机，协议对应的坐标,点击打开协议
            # target_click(520,1800)
            # titleCheck("协议详情")
            # returnInit(1)
            #
            # # 未勾选协议点击提交按钮
            # driver.find_element_by_id("com.wiseco.wisecoshop:id/commit").click()
            # toastCheck("勾选","请勾选协议")
            #
            # # 勾选协议
            # clickAction("com.wiseco.wisecoshop:id/login_check")

        else:
            print("为您推荐列表无数据")




    def test02AllProduct(self):

        titleCheck("为您推荐")

        clickAction("com.wiseco.wisecoshop:id/more_goods")
        titleCheck("贷款超市")

        if dataCheck():
            listid = "com.wiseco.wisecoshop:id/money_backname"
            infoid = "com.wiseco.wisecoshop:id/appay"
            inid = "com.wiseco.wisecoshop:id/commit"
            listAction(listid,infoid,inid)

            returnInit(3)
        else:
            print("贷款超市列表无数据")



    # 判断状态，返回状态文本
    def getStatus(self,table,database):
        mobile = localReadConfig.get_user("mobile")[0:3] + "******" + localReadConfig.get_user("mobile")[9:11]
        sql1 = "select user_id from user_extension where mobileNumber = '%s'" % mobile
        user_id = queryOneData(sql1, "database_diversion")[0]

        sql2 = "select count(1) from %s where user_id = '%s'" % (table,user_id)
        if queryOneData(sql2, database)[0] > 0:
            return "已完成"
        else:
            return "未完成1"


    # 完成基本资料操作
    def doCompleteBaseInfo(self):
        print("点击基础资料后面的未完成状态，进入基础资料完善页面")
        driver.find_element_by_id("com.wiseco.wisecoshop:id/text_finish_user").click()
        time.sleep(2)
        returnInit()



    # 绑卡操作
    def doBindBank(self):
        pass