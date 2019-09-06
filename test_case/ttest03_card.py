#coding = utf-8

from appium import webdriver
from common.driverUtil import driver
from common.element_action import *
from common.swipe_app import *
import unittest
import time



class CardPage(unittest.TestCase):


    @classmethod
    def setUpClass(cls):

        isUpdate("com.wiseco.wisecoshop:id/cancel")

        # 点击信用卡进入信用卡模块，校验页面title是否正确
        print("点击信用卡进入信用卡模块")
        clickAction("com.wiseco.wisecoshop:id/navigation_home_card")
        titleCheck("信用卡")


    # 用卡优惠
    def test01CardDiscount(self):
        print("点击用卡优惠进入信用卡优惠页面")
        clickAction("com.wiseco.wisecoshop:id/card_life")

        # 校验定位是否正常
        if driver.find_element_by_id("com.wiseco.wisecoshop:id/location_text").text == "null":
            raise "信用卡优惠页面定位显示为null"
        else:
            print("定位显示正常")


        print("点击美食图标进入下一页面")
        clickAction("com.wiseco.wisecoshop:id/life_channel_text")

        if dataCheck():
            print("数据列表正常")
        else:
            print("列表无数据")

        returnInit(1)
        titleCheck("信用卡优惠")

        clickAction("com.wiseco.wisecoshop:id/life_vip_discounts")
        clickAction("com.wiseco.wisecoshop:id/confirm_dialog_log_out")

        titleCheck("添加信用卡")

        if isElementExist("com.wiseco.wisecoshop:id/commit"):
            print("添加信用卡页面信息正常")
        else:
            raise "添加信用卡页面提交信息按钮不存在"

        returnInit(2)

    # 信用卡代还
    def test02CardPay(self):
        print("点击信用卡代还模块")
        driver.find_element_by_id("com.wiseco.wisecoshop:id/card_help").click()

        toastCheck("敬请","敬请期待")




    # 热卡推荐模块,列表-详情-全部-回到列表
    def test03HotCard(self):
        time.sleep(2)
        listid = "com.wiseco.wisecoshop:id/name"
        infoid = "com.wiseco.wisecoshop:id/appay"
        inid = "cardListBox"
        print("热卡推荐列表数据操作，列表-详情-下一页面-返回到列表")
        listAction(listid,infoid,inid)

        # 返回2次，才能返回到信用卡初始页面
        returnInit(2)
        titleCheck("信用卡")


    # 查看更多热卡，列表-详情-全部-回到列表
    def test04MoreHotCard(self):
        time.sleep(2)
        print("点击热卡推荐后的更多按钮，进入信用卡列表")
        clickAction("com.wiseco.wisecoshop:id/fragmeng_card_more")

        listid = 'com.wiseco.wisecoshop:id/card_backname'
        infoid = 'com.wiseco.wisecoshop:id/appay'
        inid = 'images'
        print("热卡推荐-更多模块操作，更多-列表-详情-下一页面-返回到更多页面")
        listAction(listid,infoid,inid)

        # 返回3次，才能回到信用卡初始页面
        returnInit(3)
        titleCheck("信用卡")



    # 热门银行，列表-详情-全部-回到列表
    def test05HotBank(self):
        swipeUtilElementAppear("com.wiseco.wisecoshop:id/gridview_partner", "up")
        time.sleep(2)
        print("点击热门银行下的第一个银行图标")
        clickAction('com.wiseco.wisecoshop:id/image1')


        if findElement('com.wiseco.wisecoshop:id/bar_tittle').text == '信用卡列表':
            print("页面成功跳转到信用卡列表")

            listid = 'com.wiseco.wisecoshop:id/card_backname'
            infoid = 'com.wiseco.wisecoshop:id/appay'
            listAction(listid,infoid)

            # 返回3次，才能回到信用卡初始页面
            returnInit(3)
            titleCheck("信用卡")

        else:
            raise "点击银行后，页面title不是信用卡列表，需手动检测页面是否正常"



    # 信用卡攻略，列表-详情-回到列表
    def test06CardStrategy(self):

        swipeUtilElementAppear("com.wiseco.wisecoshop:id/title")
        time.sleep(2)
        clickAction("com.wiseco.wisecoshop:id/title")
        swipeEnd("js_view_source1")
        clickAction("js_view_source")
        print("详情页面正常")
        returnInit()

        titleCheck("信用卡")

    # 信用卡攻略-更多，列表-详情-回到列表-回到信用卡模块
    def test07MoreCardtrategy(self):
        swipeUtilElementAppear("com.wiseco.wisecoshop:id/title")
        print("点击信用卡攻略后的更多按钮，进入资讯列表")
        clickAction("com.wiseco.wisecoshop:id/fragmeng_card_more_help")

        time.sleep(2)
        clickAction("com.wiseco.wisecoshop:id/title")
        swipeEnd("js_view_source1")
        clickAction("js_view_source")
        print("详情页面正常")
        returnInit(2)

        titleCheck("信用卡")










