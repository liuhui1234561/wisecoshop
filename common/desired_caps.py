#coding=utf-8

from appium import webdriver
import config.readConfig as readConfig

localReadConfig = readConfig.ReadConfig()

def appium_desired():
    desired_caps = {}
    """
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '8.1.0'
    #desired_caps['deviceName'] = 'AQOVFYKZCA899PTC'
    desired_caps['deviceName'] = 'LREIHYTKKBEA85GY'
    desired_caps['appPackage'] = 'com.wiseco.wisecoshop'
    desired_caps['appActivity'] = '.activity.SplashActivity'
    desired_caps['noReset'] = 'true'
    desired_caps['fullReset'] = 'false'
    """

    desired_caps['platformName'] = localReadConfig.get_remote("platformName")
    desired_caps['platformVersion'] = localReadConfig.get_remote("platformVersion")
    desired_caps['deviceName'] = localReadConfig.get_remote("deviceName")
    desired_caps['appPackage'] = localReadConfig.get_remote("appPackage")
    desired_caps['appActivity'] = localReadConfig.get_remote("appActivity")
    desired_caps['noReset'] = localReadConfig.get_remote("noReset")
    desired_caps['fullReset'] = localReadConfig.get_remote("fullReset")
    desired_caps['automationName'] = localReadConfig.get_remote("automationName")
    # 使用unicodeKeyboard的编码方式来发送字符串
    #desired_caps['unicodeKeyboard'] = localReadConfig.get_remote("unicodeKeyboard")
    # 将键盘隐藏起来
    #desired_caps['resetKeyboard'] = localReadConfig.get_remote("resetKeyboard")

    try:
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        print("连接成功！")
        return driver
    except  Exception as e:
        print(e)

